"""
УДАЛЕНИЕ ДУБЛИКАТОВ
Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.
Желательно получить решение, которое не считывает входной файл целиком в память, т.е., использует лишь константный
объем памяти в процессе работы.

Формат ввода
Первая строка входного файла содержит единственное число n, n ≤ 1000000.
На следующих n строк расположены числа — элементы массива, по одному на строку. Числа отсортированы по неубыванию.

Формат вывода
Выходной файл должен содержать следующие в порядке возрастания уникальные элементы входного массива.

Пример 1

Ввод	Вывод
5        2
2        4
4        8
8
8
8

Пример 2
Ввод	Вывод
5         2
2         8
2
2
8
8
"""

INPUT_FILENAME = 'input.txt'
OUTPUT_FILENAME = 'output.txt'

if __name__ == '__main__':
    list_nums = []
    with open(INPUT_FILENAME, 'r') as fr:
        c = 0
        n = 1
        cursor = 0  # позиция
        for i in fr:
            if c:
                if cursor < n:
                    cursor += 1  # увеличение позиции
                    value = int(i.split('\n')[0])
                    if list_nums:
                        if list_nums[-1] != value:
                            list_nums.append(value)
                    else:
                        list_nums.append(value)
                else:
                    break
            else:
                c = 1      # для определения первой строки
                n = int(i)  # кол-во строчек для анализа

    # with open(OUTPUT_FILENAME, 'w') as fw:
    #     fw.write(str(list_nums))\
    # list_nums =sorted(list(set(list_nums)))

    with open(OUTPUT_FILENAME, 'w') as fw:
        for item in list_nums:
            fw.write("%s\n" % list_nums)
