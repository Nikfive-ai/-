class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        self.__password = new_password
    def check_password(self, password):
        return self.__password == password
# Создание аккаунта пользователя
user = UserAccount("Nikfive", "Nikfive555666@yandex.ru", "Nikfive1016")
# Проверка старого пароля
print(user.check_password("Nikfive1016"))  #True
# Изменим пароль
user.set_password("Nik5553522")
# Проверим новый пароль
print(user.check_password("Nik5553522"))  #True
# Проверим неправильный пароль
print(user.check_password("gg"))  #False