class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.emp_id}"

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}"

class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание в области {self.specialization}"

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = "Список сотрудников в команде:\n"
        for emp in self.team:
            team_info += emp.get_info() + "\n"
        return team_info

# Создание сотрудников
emp = Employee("Иван Иванов", 111)
man = Manager("Никита Петров", 122, "Дизайн")
tech = Technician("Илья Трубитской", 133, "Электрика")

# Создание TechManager
tech_manager = TechManager("Константин", 144, "IT", "Программирование")

# Добавление сотрудников в команду TechManager
tech_manager.add_employee(emp)
tech_manager.add_employee(man)
tech_manager.add_employee(tech)

print(emp.get_info(Employee))
print(man.get_info())
print(man.manage_project())
print(tech.get_info())
print(tech.perform_maintenance())
print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())
# Вывод информации о всей команде
print(tech_manager.get_team_info())

# Вызов методов управления проектами и обслуживания

