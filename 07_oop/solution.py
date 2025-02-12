class Car:
    total_car = 0
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.__model = usermodel
        Car.total_car += 1
    
    def full_name(self):
        return f"car name: {self.__brand} model: {self.__model}"
    
    def get_brand(self):
        return self.__brand + " !"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Toyota", "Corolla")
# print(my_car.get_brand())
# print(my_car.model)
# print(my_car.full_name())

my_car2 = Car("Tata", "Safari")
# print(my_car2.get_brand())
# print(my_car2.model)
# print(my_car2.fuel_type())

car1 = ElectricCar("Tesla", "Model S", "85kWh")
# print(isinstance(car1, Car))
# print(isinstance(car1, ElectricCar))
# print(car1.get_brand())
# print(car1.model)
# print(car1.battery_size)
# print(car1.full_name())
# print(car1.fuel_type())

# print(Car.total_car)
# print(Car.general_description())


audi = Car("Audi", "R8")
# print(audi.get_brand())
# audi.model = "Q8"
# print(audi.model)
# print(audi.model())



class Battery:
    def battery_info(self):
        return "Battery Info"
    
class Engine:
    def engine_info(self):
        return "Engine Info"
    
class ElectricCar2(Battery, Engine, Car):
    pass

my_tesla = ElectricCar2("Tata", "Maruti")
print(my_tesla.battery_info())
print(my_tesla.engine_info())