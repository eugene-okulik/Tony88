from random import choice, randint


salary = (int(input('Enter your salary: \n')))
get_bonus = choice([True, False])
if get_bonus:
    bonus_amount = (salary / 100) * randint(1, 100)
    print(f"{salary}, {get_bonus} - '${salary + bonus_amount}'")
else:
    print(f"{salary}, {get_bonus} - '${salary}'")
