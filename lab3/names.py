import re
import sys


def untag(string: str) -> str:
    """
    Вставляет вместо html-тегов пробел (" ")
    :param string: строка, которую нужно очистить
    :return: очищенная строка
    """
    clean_pattern = re.compile(r'<.*?>')
    clean_text = re.sub(clean_pattern, ' ', string)
    return clean_text


def get_names(html: str) -> list:
    """
    Имена расположены в теге <td>...</td> при этом имеется формат:
    <td>rating</td> <td>male_name</td> <td>female_name</td>
    Поэтому сразу ищем такую строку в html документе
    :param html: текст в формате html
    :return: список с вложенным массивом в формате [rate, male, female]
    """
    result = []
    for names in re.findall(r"<td>\w*</td><td>\w*</td><td>\w*</td>", html):
        result.append(untag(names).strip().split())
    return result


def get_year(html: str) -> list:
    """
    Имена расположены в теге <td>...</td> при этом имеется формат:
    <td>rating</td> <td>male_name</td> <td>female_name</td>
    Поэтому сразу ищем такую строку в html документе
    :param html: текст в формате html
    :return: список с вложенным массивом в формате [rate, male, female]
    """
    result = []
    for names in re.findall(r"<input*>", html):
        result.append(untag(names).strip().split())
    return result


def extr_name(filename: str) -> dict:
    """
    Обрабатывает html-файл и возвращает словарь с ключами, которые сожержат:
    all_names - сортированный по алфавиту массив всех имен с указанием рейтинга
    (Сначала перед именами записывается год, полученный из имени файла)
    top_male_names - топ 10 мужских имен
    top_female_names - топ 10 женских имен
    :param filename: имя файла или путь к нему
    :return: словарь содержащий три ключа (all_names, top_male_names, top_female_names)
    """
    html = open(filename, "r").read()

    # get 'year' from tag
    year = re.search(r'Popularity in (([0-9]){4})', html).group(1)
    top_male_names = []
    top_female_names = []
    all_names = [year]
    list_names = get_names(html)
    for line in list_names:
        rate = line[0]
        male_name = line[1]
        female_name = line[2]

        all_names.append(male_name + " " + rate)
        all_names.append(female_name + " " + rate)

        if int(rate) <= 10:
            top_male_names.append(male_name)
            top_female_names.append(female_name)

    return {"all_names": sorted(all_names), "top_male_names": top_male_names, "top_female_names": top_female_names}


def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)

    for file in args:
        names_dict = extr_name(file)

        for name in names_dict["all_names"]:
            print(name, end=", ")

        print("\n")
        print("Топ мужских имён:")
        for male_name in names_dict["top_male_names"]:
            print(male_name, end=", ")

        print("\n")
        print("Топ женских имён:")
        for female_name in names_dict["top_female_names"]:
            print(female_name, end=", ")


if __name__ == '__main__':
    main()
