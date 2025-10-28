class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2025)
car2 = Car("Honda", "Civic", 2025)

car1.display_info()
car2.display_info()
