import os
import datetime


def scv_search(path_to_file: str) -> dict:
    val_dict: dict[str, dict] = {}
    if os.path.exists(path_to_file):
        for root, dirs, files in os.walk(path_to_file):
            for name in files:
                if os.name.endswith(".scv"):
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


print(scv_search('C:\\Users\\USER001\\Downloads\\D1_TEST'))


def apple_stock_sum(stock_file_path: str) -> str:

    temp_max = 0
    temp_min = 0
    temp_volumes = 0
    count = 0
    average_dict: dict[datetime, dict] = {}
    year_1 = None
    with open(stock_file_path, 'r') as apple_stock:
        apple_stock.readline()
        for line in apple_stock:

            line_date = datetime.datetime.strptime(line[0], '%d-%m-%Y')
            year = line_date.year
            if year_1 is None:
                year_1 = year
                if year_1 == year:
                    temp_min += line[1]
                    temp_volumes += line[4]
                    temp_max += line[3]
                    count += 1
                else:
                    average_dict[year_1] = {
                        'Minimum price': temp_min/count,
                        'Max price': temp_max / count,
                        'volumes': temp_volumes / count
                    }
                    year_1 = year
                    count = 0
                    temp_volumes = 0
                    temp_min = 0
                    temp_max = 0
    return average_dict


print(apple_stock_sum("C:\\Users\\USER001\\Downloads\\AAPL.csv"))



