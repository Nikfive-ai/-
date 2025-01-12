class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):

        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        """Переопределённый метод для получения информации об автомобиле"""
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"

vehicle = Vehicle("Audi", "RS6")
print(vehicle.get_info())
car = Car("BMW", "M8", "Бензин")
print(car.get_info())