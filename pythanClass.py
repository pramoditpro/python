class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        return f"{self.brand} goes {self.speed} km/h"

car  = Vehicle("Tesla", 250)
bike = Vehicle("Kawasaki", 180)
print(car.describe())


################################### Inheritance

class ElectricCar(Vehicle):
    def __init__(self, brand, battery_kw):
        super().__init__(brand, battery_kw)   # ✅ pass battery_kw as speed
        self.battery_kw = battery_kw          # ✅ store it as instance field

    def start(self):
        return f"{self.brand}: silent electric start ⚡"

    def battery_info(self):
        return f"Battery: {self.battery_kw} kWh"

tesla = ElectricCar("Tesla Electric", 100)
print(tesla.start())
print(tesla.battery_info())


############Multiple Inheritance

class Flyable:
    def fly(self): return "I can fly!"

class FlyingCar(ElectricCar, Flyable):   # multiple parents!
    pass

fc = FlyingCar("AirTesla", 120)
print(fc.fly())    # from Flyable
print(fc.start())  # from ElectricCar
