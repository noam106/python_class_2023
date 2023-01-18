import os


def scv_search(path_to_file: str) -> dict:
    val_dict: dict[str,dict] = {}
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