import csv
import os
import datetime


def scv_search(path_to_file: str) -> dict:
    val_dict: dict[str, dict] = {}
    if os.path.exists(path_to_file):
        for root, dirs, files in os.walk(path_to_file):
            for name in files:
                if name.endswith(".csv"):
                    scv_path = os.path.join(root, name)
                    with open(scv_path, 'r') as f:
                        count_line = 0
                        column = f.readline()
                        count_column = len(column.split(',')) + 1
                        for line in f:
                            count_line += 1
                        val_dict[name] = {'column': count_column, 'line': count_line}
        return val_dict
    else:
        return None


print(scv_search('C:\\Users\\USER001\\PycharmProjects\\fs-7732-3\\lesson18\\data\\files_ex'))


def apple_stock_sum(stock_file_path: str) -> str:

    temp_max = 0
    temp_min = 0
    temp_volumes = 0
    count = 0
    average_dict: dict[datetime, dict] = {}
    year_1 = None
    with open(stock_file_path, 'r') as apple_stock:
        apple_stock.readline()
        for line_1 in apple_stock:
            line = line_1.split(',')

            line_date = datetime.datetime.strptime(line[0], '%d-%m-%Y')
            year = line_date.year
            if year_1 is None:
                year_1 = year
            if year_1 == year:
                temp_min += float(line[1])
                temp_volumes += float(line[4])
                temp_max += float(line[3])
                count += 1
            else:
                average_dict[year_1] = {
                    'Minimum price': str(temp_min/count),
                    'Max price': str(temp_max / count),
                    'volumes': str(temp_volumes / count)
                }
                year_1 = year
                count = 0
                temp_volumes = 0
                temp_min = 0
                temp_max = 0
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['year', 'max price', 'min price', 'volumes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for year_in in average_dict:
            writer.writerow({'year': year_in, 'max price': year_in['Max price'], 'min price': year_in['Minimum price'],
                             'volumes': year_in['volumes']})
    return average_dict


print(apple_stock_sum('C:\\Users\\USER001\\PycharmProjects\\fs-7732-3\\lesson18\\data\\AAPL.csv'))


class EBook:
    def __init__(self, dir_file: str, amount_words_per_page: int):
        self._amount_words_per_page = amount_words_per_page
        self._dir_file = dir_file
        with open(self._dir_file) as file_handler:
            self._content = file_handler.read()

    def get_amount_words_per_page(self):
        return self._amount_words_per_page

    def set_amount_words_per_page(self, new_num: int):
        if new_num > 0:
            self._amount_words_per_page = new_num

    def get_dir_file(self):
        return self._dir_file

    def get_content(self):
        return self._content

    def is_file_exist(self) -> bool:
        if os.path.exists(self._dir_file):
            return True
        else:
            return False

    # how to build a content to every page?
    # what dose it mean bookmark?
    def dividing_to_pages(self) -> int:
        pass

