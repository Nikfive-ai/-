7def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


try:
    uzer_number = int(input('введите число'))
    if is_prime(uzer_number) == True:
        print('число простое')
    else:
        print('число не простое')
except ValueError:
    print('это не число')
