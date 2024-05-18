import numpy as np

if __name__ == "__main__":
    file = open('data.txt', 'r')
    content = file.read()
    unique_letters = set(content)
    dict_count = dict()
    for key in unique_letters:
        for value in test_values:
            res[key] = value
            test_values.remove(value)
            break
    print(unique_letters)
