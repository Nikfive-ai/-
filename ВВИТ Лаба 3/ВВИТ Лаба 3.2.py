a = str(input())
with open('Чёто написать.txt', 'w',encoding="UTF-8") as file:
    file.write(a)
file.close()
