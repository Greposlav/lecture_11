import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as f:
        seq = json.load(f)

    return seq[field]


def linear_search(sequence, number):
    position = []
    m = 1
    count = 0
    for i in sequence:
        if i == number:
            count += 1
            position.append(m)
        m += 1
    num = {"position": position, "count": count}
    return num


def main():
    sequence = read_data("sequential.json", "unordered_numbers")

    pos_count = linear_search(sequence, 0)
    print(pos_count)


if __name__ == '__main__':
    main()