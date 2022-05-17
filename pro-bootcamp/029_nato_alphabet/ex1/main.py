# Returns a list of common values in two files using list comprehensions

def get_common_values_in_files(filepath_1:str, filepath_2:str) -> list:
    with open(filepath_1) as f:
        file_1_data = f.read().splitlines()

    with open(filepath_2) as f:
        file_2_data = f.read().splitlines()

    common = [ value for value in file_1_data if value in file_2_data ] 
    return common


if __name__ == '__main__' :
    res = get_common_values_in_files('./file_1.txt', './file_2.txt')
    print(f'common values in files are: {res}')