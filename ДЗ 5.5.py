#Создать (программно) текстовый файл, записать в него программно набор чисел,
#разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('ДЗ_5.5.txt', 'w+') as fl:
    line = input('Введите цифры через пробел \n')
    fl.writelines(line)
    n = line.split()

print(sum(map(int, n)))