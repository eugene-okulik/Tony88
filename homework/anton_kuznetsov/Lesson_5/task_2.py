# исходные данные
string1 = 'результат операции: 42'
string2 = 'результат операции: 514'
string3 = 'результат работы программы: 9'

# извлекли индекс с которого начинается число в срезе
index_of_number = string1.index(':') + 2
num = int(string1[index_of_number:]) + 10
print(num)

# переиспользвали переменные для второй строки
index_of_number = string2.index(':') + 2
num = int(string2[index_of_number:]) + 10
print(num)

# переиспользвали переменные для третьей строки
index_of_number = string3.index(':') + 2
num = int(string3[index_of_number:]) + 10
print(num)
