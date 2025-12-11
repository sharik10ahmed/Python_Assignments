class Vehicle:
    Vehicle="BMW"
    def Func_Vehicle(Self):
        print("Main Vechicle Factory")
    
class Car(Vehicle):
    Car_Name = "Nissan"
    Car_Name2 = "Audi"
    def Func_Car(Self): #Self is a default keyword if you are creating function under a class and then with Self keyword you can access all variables after that
        print(f"Collection of cars -> {Self.Car_Name} ",) #use Self before the varialble name because you need to maintain privacy
        print(f"Collection of cars -> {Self.Car_Name2} ",)
class Bike(Vehicle):
    # Bike_Name = "At least"
    Bike_Name2 = "Yamaha"
    def Bike_Func(Self):
        print(f"Collecton of Bikes -> {Self.Bike_Name2} ")
Bike_obj = Bike()
print("This my Object ",Bike_obj)
# print(Bike_obj.Bike_Name2)
# Bike_obj.Bike_Func()
# Bike_obj.Func_Vehicle()
# print(Bike_obj.Vehicle)
# Car_obj = Car()
# Car_obj.Func_Vehicle()
# print(Car_obj.Vehicle)
