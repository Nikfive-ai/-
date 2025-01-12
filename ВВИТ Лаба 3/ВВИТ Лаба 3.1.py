def read_file(exemple):
    
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)

read_file('example.txt')