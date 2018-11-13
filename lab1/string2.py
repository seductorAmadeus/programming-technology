# 1.
# Вх: строка. Если длина > 3, добавить в конец "ing",
# если в конце нет уже "ing", иначе добавить "ly".
def v(s):
    if len(s) > 3:
        if s.endswith('ing'):
            s += 'ly'
        else:
            s += 'ing'

    return s


# 2.
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!

def nb(s):
    notIndex, badIndex = s.find('not'), s.rfind('bad')
    if (notIndex >= badIndex) or notIndex == -1 or badIndex == -1:
        # return empty string as error
        return ""
    # because strings are immutable
    s = s[:notIndex] + 'good' + s[badIndex + len('bad'):]
    return s


if __name__ == '__main__':
    #  task №1
    print("============ task 1 ================")
    test = v('eafaefaefafeing')
    print(test)
    #  task №2
    print("============ task 2 ================")
    test = nb('This music is n bad  not so g not! bad f')
    print(test)
    test = nb('This music is not so bad!')
    print(test)
    test = nb('This music is n  not not so g not! bad f')
    print(test)



