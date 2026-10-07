my_dict = dict()
my_dict['tuple'] = ('one', 2, 'three', '4', 'five', 6)
my_dict['list'] = [1, 22, 333, 4444, 55555, 666666, 7777777]
my_dict['dict'] = {1: 'city', 2: 'street', 3: 'house', 4: 'apartment', 5: 'phone', 6: 'info'}
my_dict['set'] = {23456, 6678, 23, 456, 777, 890, 567, 11}

# 1 задание
print(my_dict['tuple'][-1])

# 2 задание
my_dict['list'].append(88888888)
my_dict['list'].pop(1)

# 3 задание
my_dict['dict']['i am a tuple'] = 'additional description'
my_dict['dict'].pop(5)

# 4 задание
my_dict['set'].add(20)
my_dict['set'].remove(23456)

print(my_dict)
