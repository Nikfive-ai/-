def read_file(exemple):
    try:
        with open(exemple, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Файл не найден")
read_file('example.txt')