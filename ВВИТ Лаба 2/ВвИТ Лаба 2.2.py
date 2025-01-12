import time


'''
Напишите функцию describe_person, принимающую имя и возраст человека,
и печатающую эту информацию в читаемом виде. Сделайте возраст опциональным
аргументом со значением по умолчанию 30.
'''
def describe_person(name, age=30):
    return_text = f'ваше имя - {name}, вам {age} лет'
    for sim in return_text:
        time.sleep(0.15)
        print(sim, end="")

uzer_name = input('как вас зовут?')
describe_person(uzer_name, age=20)