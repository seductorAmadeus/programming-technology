# 1.
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему

def me(words):
    count = 0
    for string in words:
        if string.endswith(string[:1]) and len(string) > 2:
            count += 1
    return count


# 2.
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']
def fx(words):
    words.sort()
    position = 0
    for string in words:
        if string.startswith('x'):
            temp = words.pop(words.index(string))
            words.insert(position, temp)
            position += 1
    xlist = words
    return xlist


# 3.
# Вх: список непустых кортежей,
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def tuple_sort(numbers):
    return sorted(numbers, key=lambda x: x[-1])


if __name__ == '__main__':
    #  task №1
    print("============ task 1 ================")
    test = me(['f2f', 'afeaf', 'f2ff', 'eafaefaefafe'])
    print(test)

    #  task №2
    print("============ task 2 ================")
    test = fx(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc', 'xzfqfe3', 'felfafae', 'aaeaaaa', 'xaaaaaaaa'])
    print(test)

    #  task №3
    print("============ task 3 ================")
    test = tuple_sort([(1, 7), (1, 3), (3, 4, 57), (2, 2)])
    print(test)