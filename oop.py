class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def start(self):
        print(f"{self.brand} {self.model} is starting...")
    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")
my_car = Car("Toyota", "Corolla")
my_car.start()
my_car.stop()
##INHERITANCE
class ElectricCar(Car):
    def __init__(self, brand, model, battery_range):
        super().__init__(brand, model)
        self.battery_range = battery_range

    def charge(self):
        print(f"{self.brand} {self.model} is charging. Range: {self.battery_range} km")
        
    #Override Method (Polymorphism)
    def start(self):
        print(f"{self.brand} {self.model} is silently starting (electric power).")
tesla = ElectricCar("Tesla", "Model S", 600)
tesla.start()
tesla.charge()

#🛡️ Step 4: Encapsulation (Private attributes)


class SecureCar:
    def __init__(self, brand):
        self.__brand = brand  # private attribute

    def get_brand(self):
        return self.__brand

secure = SecureCar("BMW")
print(secure.get_brand())  # BMW
#print(secure.__brand)      # ❌ Error (private)
# Abstraction (hide logic, force implementation)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

# Encapsulation (hide data)
class Car(Vehicle):
    def __init__(self, brand):
        self.__brand = brand  # encapsulated/private

    def get_brand(self):
        return self.__brand

    def start(self):  # abstract method implemented
        print(f"{self.__brand} is starting.")

# You cannot do this (will raise an error):
# v = Vehicle()  # ❌ TypeError: Can't instantiate abstract class

# Instead, use a subclass that implements `start`
my_car = Car("Toyota")

# ✅ Access the encapsulated attribute via getter
print(my_car.get_brand())  # Output: Toyota

# ✅ Call the abstract method that was implemented
my_car.start()             # Output: Toyota is starting.

# ❌ Direct access to __brand will fail:
# print(my_car.__brand)    # AttributeError

