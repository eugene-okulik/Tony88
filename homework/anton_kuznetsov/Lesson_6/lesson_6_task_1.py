# исходные данные
text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
# распарсили список и добавили ing
phrase_list = text.split()
for i in phrase_list:
    if ',' in i:
        i = i.replace(',', 'ing,')
        print(i, end=' ')
    elif '.' in i:
        i = i.replace('.', 'ing.')
        print(i, end=' ')
    else:
        i = i + 'ing'
        print(i, end=' ')
