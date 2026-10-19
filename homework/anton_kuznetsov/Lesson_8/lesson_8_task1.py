from random import choice, randint


salary = (int(input('Enter your salary: \n')))
get_bonus = choice([True, False])
# get_bonus = bool(randint(0, 1))

# про граничные значения бонуса ничего не говорилось и я установил их на свое усмотрение
bonus_amount = (salary / 100) * randint(1, 100)
print(f"{salary}, {get_bonus} - '${salary + bonus_amount}'")
