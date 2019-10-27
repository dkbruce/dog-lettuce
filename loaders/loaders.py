from pathlib import Path


def load_file(path=Path('data/users.txt')):
    with open(path, 'r') as f:
        output_list = f.readlines()
    output_list = [user.strip('\n') for user in output_list]
    return output_list
