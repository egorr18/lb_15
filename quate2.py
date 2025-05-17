class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}, Колір: {self.color}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Колір змінено на: {self.color}")

car1 = Car("Toyota", "Camry", 2020, "сірий")
car1.info()

car1.change_color("червоний")
car1.info()
