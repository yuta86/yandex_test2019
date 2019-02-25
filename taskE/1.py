"""
Анаграммы
Даны две строки, состоящие из строчных латинских букв. Требуется определить, являются ли эти строки анаграммами,
т. е. отличаются ли они только порядком следования символов.

Формат ввода
Входной файл содержит две строки строчных латинских символов, каждая не длиннее 100 000 символов.
 Строки разделяются символом перевода строки.

Формат вывода
Выходной файл должен содержать единицу, если строки являются анаграммами, и ноль в противном случае.


Пример 1
Ввод	Вывод
qiu       1
iuq

Пример 2
Ввод	Вывод
zprl      0
zprc

"""

INPUT_FILENAME = 'input.txt'
OUTPUT_FILENAME = 'output.txt'

if __name__ == '__main__':
    with open(INPUT_FILENAME, 'r') as fr:
        one_line = fr.readline()
        two_line = fr.readline()

    one_line = list(one_line.split('\n')[0])  # разделение через '\n' - перевод в список
    two_line = list(two_line.split('\n')[0])  # разделение через '\n' - перевод в список

    result = 0
    if len(one_line) != len(two_line):
        result = 0
    else:
        one_line.sort()
        two_line.sort()
        if one_line == two_line:
            result = 1
        else:
            result = 0

        # for sym in one_line:
        #     if sym in two_line:
        #         result = 1
        #     else:
        #         result = 0
        #         break
        #
        # if result:
        #     for sym in two_line:
        #         if sym in one_line:
        #             result = 1
        #         else:
        #             result = 0
        #             break

    with open(OUTPUT_FILENAME, 'w') as fw:
        fw.write(str(result))
