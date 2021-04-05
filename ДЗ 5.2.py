#Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open("ДЗ_5.2") as fl:
    content = fl.read()
    print(content)
with open("ДЗ_5.2") as fl:
    a = 0
    for i in fl:
        a += 1
print(f'Количество строк {a}')
with open("ДЗ_5.2") as fl:
    content = fl.readlines()
    b = 0
    for i in (content):
        b +=1
        i = i.split()
        l = len(i)
        print(f'Количество слов {b}-ой строки {l}')

