import psycopg2
import datetime

#
# def display_movies_info(movie_name: str) -> tuple:
#     with psycopg2.connect(
#             host="localhost",
#             port=5432,
#             database="top_250_movies",
#             user="postgres",
#             password="08aa21366") as conn:
#
#         # create a cursor
#         with conn.cursor() as cur:
#             movie_info = f"""
#             select
#             release_date from imdb_top
#             where
#             movie_name = '{movie_name}';
#             """
#             # print (movie_info)
#             cur.execute(movie_info)
#             result = cur.fetchone()
#     conn.close()
#     return result
#
# def rating_movies_info(movie_name: str) -> tuple:
#     with psycopg2.connect(
#             host="localhost",
#             port=5432,
#             database="top_250_movies",
#             user="postgres",
#             password="08aa21366") as conn:
#         with conn.cursor() as rating:
#             movie_rating = f"""
#             select
#             rating from imdb_top
#             where
#             movie_name = '{movie_name}';
#             """
#             rating.execute(movie_rating)
#             rating_list = rating.fetchone()
#             rating_num = rating_list[0]
#
#         with conn.cursor() as cur:
#             movie_info = f"""
#                    select
#                    movie_name from imdb_top
#                    where
#                    rating < {rating_num} ;
#                    """
#             # print (movie_info)
#             cur.execute(movie_info)
#             result = cur.fetchall()
#     conn.close()
#     return result
#
#
# if __name__ == '__main__':
#     movie_name = input('hello there please enter the name of a movie: ')
#     res = display_movies_info(movie_name)
#     if res is None:
#         print ('your movie is not one of the top 250 sorry.')
#     else:
#         print(f'the year of your movie is{res}')
#         print(rating_movies_info(movie_name))
#

#bank_class

class BankSql:
    def __init__(self):
        self._conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='bank_class',
        user='postgres',
        password='08aa21366')

    def transfer(self, from_account:str, to_account:str, amount:int, initiated_by:str):
        query = f"""
                INSERT INTO public.transactions
                (transaction_type, ts, initiated_by)
                VALUES(%s, %s, %s) returning id;
                """
        query_trans_acuonnt = f"""
                                INSERT INTO public.transaction_accounts
                                (account_role, transaction_id, account_id)
                                VALUES( %s, %s, %s );
                                """
        query_update_account_giver = '''
                                UPDATE public.accounts
                                SET balance= balance - %s
                                WHERE id=%s 
        '''
        query_update_account_reciver = '''
                                        UPDATE public.accounts
                                        SET balance= balance + %s
                                        WHERE id=%s 
                                        '''
        with self._conn:
            with self._conn.cursor() as cur:
                cur.execute(query, ('transfer', datetime.datetime.now(), initiated_by))
                transfer_id = cur.fetchone()[0]
                cur.execute(query_trans_acuonnt, ('reciver',transfer_id, to_account ))
                cur.execute(query_trans_acuonnt, ('giver', transfer_id, from_account))
                cur.execute(query_update_account_giver, (amount, to_account))
                cur.execute(query_update_account_reciver, (amount, from_account))


BankSql().transfer(1,2,200,1)