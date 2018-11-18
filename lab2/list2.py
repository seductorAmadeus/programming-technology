# 1.
# Вх: список чисел, Возвр: список чисел, где
# повторяющиеся числа урезаны до одного
# пример [0, 2, 2, 3] returns [0, 2, 3].

def rm_adj(nums):
    return list(set(nums))



# 2. Вх: Два списка упорядоченных по возрастанию, Возвр: новый отсортированный объединенный список

def concat_list(list1, list2):
    result_list = list1 + list2
    result_list.sort()
    return result_list


if __name__ == '__main__':
    #  task №1
    print("============ task 1 ================")
    test = rm_adj([0, 2, 2, 3])
    print(test)
    test = rm_adj([1, 3, 3, 4, 1, 3, 4])
    print(test)
    test = rm_adj([30, 22, 2, 2, 1])
    print(test)
    #  task №2
    print("============ task 2 ================")
    test = concat_list([8, 10, 242], [9, 10, 11])
    print(test)
