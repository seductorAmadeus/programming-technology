# -*- coding: utf-8 -*-

import random
import sys


def mem_dict(filename: str) -> dict:

    """
    Создает словарь, в качестве ключа у которого содержится слово,
    а в значении возможное слово
    :param filename: имя (путь) к файлу
    :return: словарь {слово:[возможные значения...], ...}
    """

    try:
        file = open(filename, "r", encoding="UTF-8")
    except FileNotFoundError:
        print("Указанный файл не найден")
        exit()

    # Считываем все слова из файла
    words = []
    for line in file.read().split("\n"):
        for word in line.split(" "):
            words.append(word)

    word_dict = {}

    for i in range(len(words)-1):
        if word_dict.__contains__(words[i]):
            word_dict[words[i]].append(words[i+1])
        else:
            word_dict[words[i]] = [words[i+1], ""]

    # Если последнее слово не включено в словарь, добавляем значение пустой строки по-умолчанию
    if not word_dict.__contains__(words[-1]):
        word_dict[words[-1]] = [""]

    return word_dict


def create_new_sentence(words_dictionary: dict) -> str:

    """
    Создает новое предложение на основе "Похожего" словаря
    :param words_dictionary: словарь со словами и его возможными значениями
    :return: новое предложение
    """

    # В качестве первого слова выбираем случайное слово из словаря
    string_build = [random.choice(list(words_dictionary.keys()))]

    # Если последнее слово пустая строка, то предложение окончено
    while string_build[-1] != "":
        string_build.append(random.choice(words_dictionary.get(string_build[-1])))

    # Преобразуем массив слов в строку
    result = ""
    for word in string_build:
        result += word
        result += " "

    return result


def main():

    if len(sys.argv) > 1:
        words_dictionary = mem_dict(sys.argv[1])
        print(create_new_sentence(words_dictionary))
    else:
        print("Передайте имя файла в качестве параметра")


if __name__ == '__main__':
    main()