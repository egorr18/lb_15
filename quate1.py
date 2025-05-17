class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Місто: {self.city}")

person = Person("Одуванчік", 18, "Київ")
person.info()
