# исходные данные
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

# цикл
for key, value in words.items():
    print(key * int(value), sep='\n')
