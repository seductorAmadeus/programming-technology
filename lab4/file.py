import random
import sys


def read_word_list(filename):
    """
    Возвращает список слов
    :param filename: имя файла
    :return: список слов
    """
    f = open(filename, "r")
    if f.mode == "r":
        contents = f.read()
        # contents.replace("\n", " ")
        return contents.split(" ")


def make_dict(words):
    """
    Возвращает словарь
    :param words: cписок слов
    :return: словарь
    """
    dic = {"": []}
    last = words[0]
    dic[""].append(last)
    words = words[1:]
    for w in words:
        if last in dic:
            dic[last].append(w)
        else:
            dic[last] = [w]
        dic[""].append(w)
        last = w
    dic[last] = [""]
    return dic


def mem_dict(filename):
    """
    Возвращает сгенерированный текст
    :param filename: имя файла
    :return: сгенерированный текст
    """
    word_list = read_word_list(filename)
    dic = make_dict(word_list)
    gen_text_len = len(word_list)
    word = ""
    ret = ""
    while gen_text_len > 0:
        if word != "":
            ret += word + " "
            gen_text_len -= 1
        word = random.choice(dic[word])
    return ret


def main():
    path = sys.argv[1]
    print(mem_dict(path))


if __name__ == '__main__':
    main()
