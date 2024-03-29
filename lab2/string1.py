# 1.
# Входящие параметры: int <count> ,
# Результат: string в форме
# "Number of: <count>", где <count> число из вход.парам.
#  Если число равно 10 или более, напечатать "many"
#  вместо <count>
#  Пример: (5) -> "Number of: 5"
#  (23) -> 'Number of: many'

def num_of_items(count):
    return "Number of: " + ('many' if count >= 10 else str(count))


# 2.
# Входящие параметры: string s,
# Результат: string из 2х первых и 2х последних символов s
# Пример 'welcome' -> 'weme'.
def start_end_symbols(s):
    s = s[:2] + s[len(s) - 2:]
    return s


# 3.
# Входящие параметры: string s,
# Результат: string где все вхождения 1го символа заменяются на '*'
# (кроме самого 1го символа)
# Пример: 'bibble' -> 'bi**le'
def replace_char(s):
    first_char = s[0]
    replaced_string = s.replace(first_char, '*')
    return replaced_string.replace('*', first_char, 1)


# 4
# Входящие параметры: string a и b,
# Результат: string где <a> и <b> разделены пробелом
# а превые 2 симв обоих строк заменены друг на друга
# Т.е. 'max', pid' -> 'pix mad'
# 'dog', 'dinner' -> 'dig donner'
def str_mix(a, b):
    a, b = a.replace(a[:2], b[:2], 1), b.replace(b[:2], a[:2], 1)
    return a + " " + b


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(res, expt):
    print("result  : ", res)
    print("expected: ", expt)
    print("equals: ", res == expt)
    print("==========================")


if __name__ == '__main__':
    test(num_of_items(5), 'Number of: 5')
    test(num_of_items(10), 'Number of: many')
    test(start_end_symbols('welcomed'), 'weed')
    test(replace_char('bibble'), 'bi**le')
    test(str_mix('dog', 'dinner'), 'dig donner')
