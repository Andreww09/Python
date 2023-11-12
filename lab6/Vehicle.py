
#ex3
class Vehicle:
    def __init__(self,mark,model,year,capacity,mileage):
        self.mark=mark
        self.model=model
        self.year=year
        self.towing=capacity
        self.mileage=mileage

    def towing_capacity(self):
        print(f"This vehicle towing capacity is {self.towing} ")

    def show_mileage(self):
        print(f"This vehicle's mileage is {self.mileage} ")


class Car(Vehicle):
    def __init__(self, mark, model, year):
        super().__init__(mark, model, year,1000,200000)


class Motorcycle(Vehicle):
    def __init__(self, mark, model, year):
        super().__init__(mark, model, year,100,250000)


class Truck(Vehicle):
    def __init__(self, mark, model, year):
        super().__init__(mark, model, year,10000,200_000)

car=Car("Car mark","Car model",2015)
motorcycle=Motorcycle("Motorcycle mark","Motorcycle model",2022)
truck=Truck("Truck mark","Truck model",2020)

car.towing_capacity()
truck.show_mileage()



