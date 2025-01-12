'''Напишите функцию greet, которая принимает имя пользователя в качестве аргумента и выводит приветствие с этим именем.'''
def greet(name):
    print(f'приветствую, {name}!!!')

'''Создайте функцию square, которая возвращает квадрат переданного ей числа.'''
def square(number):
    return number ** 2

'''Реализуйте функцию max_of_two, которая принимает два числа в качестве аргументов и возвращает большее из них.'''
def max_of_two(x, y):
    return max(x, y)

user_name = input('как вас зовут?')
(greet(user_name))

try:
    num_for_square = int(input('введите ваше число:'))
    print(square(num_for_square))
except ValueError:
    print('ой, кажется это не число')

try:
    num1_for_max_of_two = int(input('введите первое число:'))
    num2_for_max_of_two = int(input('введите второе число:'))
    print(max_of_two(num1_for_max_of_two, num2_for_max_of_two))
except ValueError:
    print('ой, кажется это не число')



