class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary} грн."
worker = Employee("Ваня", "Полісмен", 25000)
print(worker.get_salary_info())