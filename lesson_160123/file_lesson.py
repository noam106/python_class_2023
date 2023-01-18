# import string
# alice = 'C:\\Users\\USER001\\PycharmProjects\\fs-7732-3\lesson18\\data\\alice_in_wonderland.txt'
# word = 'alice'
#
#
# with open(alice, 'r') as book:
#     count = 0
#     for line in book:
#         if word in line.lower():
#             count += 1
# print(count)
# with open(alice, 'r') as book:
#     count = 0
#     for line in book:
#         count += line.lower().count("alice")
# print(count)
#
#
# price_file = 'C:\\Users\\USER001\\PycharmProjects\\fs-7732-3\\lesson18\\data\\AAPL.csv'
# min_price: int = 1
#
# with open(price_file, 'r') as apple_stock:
#     apple_stock.readline()
#     for line in apple_stock:
#         temp_list = line.split(',')
#         if float(temp_list[1]) < min_price:
#             min_price = float(temp_list[1])
# print(min_price)

# homework


def scv_search(path: str) -> dict:
    val_dict: dict[str,dict] = {}
    # if '.' not in path:
    #     path = f'{path}\\{file}'
    for file_name in path:
        if '.scv' in file_name:
            with open(file_name, 'r') as f:
                count_line = 0
                column = f.readline()
                count_column = len(column.split(',')) + 1
                for line in f:
                    count_line += 1
                val_dict[file_name] = {'column': count_column, 'line': count_line}





