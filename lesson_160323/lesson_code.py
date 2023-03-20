import psycopg2
from flask import Flask, request, jsonify

app = Flask("bank_web_app")

# bank REST api
# get /customers
# get /customers/id


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bank_class",
    user="postgres",
    password="08aa21366")


@app.route("/api/v1/customers/<int:customer_id>", methods=['GET'])
def get_customer(customer_id):
    print(f"called /customers/customer_id/{customer_id}")
    try:
        with conn:
            with conn.cursor() as cur:
                sql = "SELECT * FROM customers WHERE id = %s"
                cur.execute(sql, (customer_id, ))
                result = cur.fetchone()
                print(f"result from fetchone: {result}")
                if result:
                    ret_data = {
                        'id': result[0],
                        'passport_num': result[1],
                        'name': result[2],
                        'address': result[3]
                    }
                    return jsonify(ret_data)
                else:
                    return {'error': f'customer with id {customer_id} does not exist'}, 404
    except psycopg2.DatabaseError as e:
        return {'error': f"Database error, {e}"}, 500
    except Exception as e:
        return {'error': f"Unexpected error, {e}"}, 500


@app.route("/api/v1/customers/<int:customer_id>/accounts" , methods=['GET'])
def customer_accounts(customer_id):
    try:
        with conn:
            with conn.cursor() as cur:
                sql = "SELECT a.* FROM account_owners ao " \
                      "join accounts a on ao.account_id = a.id " \
                      "WHERE customer_id = %s"
                cur.execute(sql, (customer_id, ))
                result = cur.fetchall()
                print(f"result from fetchone: {result}")
                if result:
                    ret_data = []
                    for i in result:
                        data_dict = {'id': i[0],
                                     'balance': i[1],
                                     'max_limit': i[2]}
                        ret_data.append(data_dict)
                    return jsonify(ret_data)
                else:
                    return {'error': f'customer with id {customer_id} does not exist'}, 404

    except psycopg2.DatabaseError as e:
        return {'error': f"Database error, {e}"}, 500
    except Exception as e:
        return {'error': f"Unexpected error, {e}"}, 500

@app.route("/api/v1/customers" , methods=['POST'])
def create_new_customer():
    new_data = request.form
    allowed_fields = ('name', 'address', 'passport_num')
    if len(new_data) == 3:
        for i in new_data:
            if i in allowed_fields:
                pass
            else:
                raise Exception
    else:
        raise Exception
    sql = f'''INSERT INTO public.customers
            (passport_num, "name", address)
            VALUES(%s, %s, %s);
                                    '''
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, tuple(new_data.values(), ))
            if cur.rowcount == 1:
                # update succeeded
                return app.response_class(status=200)
    return app.response_class(status=500)

# proper way with validation

# @app.route("/api/v1/customers", methods=['POST'])
# def create_customer():
#
#     print(request.form)
#     # validate all the required fields are received
#     required_fields = {
#         'passport_num': int,
#         'name': str,
#         'address': str
#     }
#     if set(request.form.keys()) != set(required_fields.keys()) and \
#             len(request.form.keys()) != len(required_fields):
#         return {'error': 'error in provided fields'}, 400
#
#     str_list = []
#     for field in request.form:
#         try:
#             required_fields[field](request.form[field])
#             str_list.append(field)
#         except:
#             return {'error': f'invalid type for {field}, '
#                              f'expected: {required_fields[field]}, got {type(field)}'}, 400
#
#     sql = f"INSERT INTO customers ({','.join(request.form.keys())}) VALUES ({','.join(['%s'] * 3)})"
#
#     # problem here!
#     # sql = f"INSER4T INTO customers (passport_num, name, address) VALUES (%s, %s, %s)"
#
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute(sql, tuple(request.form.values()))
#             if cur.rowcount == 1:
#                 # create succeeded
#                 return {}, 201
#     return {}, 500


@app.route("/api/v1/customers", methods = ['GET'])
def get_all_customers():
    new_data = request.args
    # num_of_row = new_data['result_per_page']
    # num_page = new_data['page_num']
    # param_tuple = {num_page, num_of_row }
    # print(param_tuple)
    sql = f"select * from customers limit %s offset (%s);"
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, tuple(new_data.values()), )
            result = cur.fetchall()
    if result:
        ret_data = []
        for i in result:
            data_dict = {'id': i[0],
                         'passport': i[1],
                         'name': i[2],
                         'address': i[3]}
            ret_data.append(data_dict)
        return jsonify(ret_data)
    else:
        return {'error': f'customer with id  does not exist'}, 404



if __name__ == '__main__':
    app.run(debug=True)

