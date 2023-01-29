def find_csv(directory: str):
    count = 0
    if os.path.exists(directory):
        for file in os.listdir(directory):
            if file.endswith(".csv"):
                count += 1
    return count