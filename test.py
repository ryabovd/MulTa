def read(name_file):
    with open(name_file + '.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def create_list(text):
    text_list = text.split('\n')
    return text_list


def readlines(name_file):
    with open(name_file + '.txt', 'r', encoding='utf-8') as f:
        list = f.readlines()
    return list


print(readlines('users'))