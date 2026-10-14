# исходные данные
string1 = 'результат операции: 42'
string2 = 'результат операции: 54'
string3 = 'результат работы программы: 209'
string4 = 'результат: 2'


# функция обрабатывающая разные форматы входных данных
def pars_data(*args):
    for argument in args:
        if ':' in argument:
            index_of_number = argument.index(':') + 2
            num = int(argument[index_of_number:]) + 10
            print(num)

pars_data(string1, string2, string3, string4)

