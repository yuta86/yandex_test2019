"""
Последовательно идущие единицы
Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.

Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.

Формат ввода
Первая строка входного файла содержит одно число n, n ≤ 10000. Каждая из следующих n строк содержит ровно одно число —
очередной элемент массива.

Формат вывода
Выходной файл должен содержать единственное число — длину самой длинной последовательности единиц во входном массиве.


Пример
Ввод	Вывод
5         1
1
0
1
0
1

"""

INPUT_FILENAME = 'input.txt'
OUTPUT_FILENAME = 'output.txt'

if __name__ == '__main__':

    with open(INPUT_FILENAME, 'r') as fr:
        c = 0
        n = 1
        max_length = 0
        cur_length = 0
        cursor = 0  # позиция
        for_start = False
        for i in fr:
            if for_start:
                if cursor < n:
                    cursor += 1  # увеличение позиции
                    value = int(i.split('\n')[0])
                    if value == 1:  # 1
                       cur_length +=1
                    else:
                        if cur_length > max_length:
                            max_length = cur_length
                        cur_length = 0

                else:
                    break
            else:
                for_start = True      # для определения первой строки
                n = int(i)  # кол-во строчек для анализа

    if cur_length > max_length:
        max_length = cur_length

    with open(OUTPUT_FILENAME, 'w') as fw:
        fw.write(str(max_length))