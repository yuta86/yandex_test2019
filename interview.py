
"""
Написать на питоне скрипт, который принимает на вход параметрами имена файлов. В первых двух файлах построчно записаны
числа, отсортированные по возрастанию. В третий нужно записать построчно отсортированный по возрастанию результат
слияния чисел из первых двух файлов
"""

INPUT_FILENAME1 = 'input1.txt'
INPUT_FILENAME2 = 'input2.txt'
OUTPUT_FILENAME = 'output.txt'

read_file = 0
SORT = False

if __name__ == '__main__':
    with open(OUTPUT_FILENAME, 'w') as f:

        with open(INPUT_FILENAME1, 'r') as f1:

            with open(INPUT_FILENAME2, 'r') as f2:
                while not SORT:
                    if read_file == 0:
                        x1 = f1.readline()
                        x2 = f2.readline()
                    else:
                        if read_file == 1:
                            x1 = f1.readline()
                        else:
                            x2 = f2.readline()

                    if x1 and x2:
                        if int(x1) >= int(x2):
                            f.write("%s\n" % int(x2))
                            read_file = 2
                        else:
                            f.write("%s\n" % int(x1))
                            read_file = 1
                    elif x1:
                        f.write("%s\n" % int(x1))
                        read_file = 1
                    elif x2:
                        f.write("%s\n" % int(x2))
                        read_file = 2
                    else:
                        SORT = True
