class Car():
    wheels = 4
    def start_car(self):
        print("Car started")
    def example_car(self):
        print(self.wheels)
        self.start_car()

#using object reference we can access the properties of the class outside the class
car1 = Car()
print(car1.wheels)
car1.start_car()
car1.example_car()

#assigning method parameters to class variables using self keyword
class Car:
    wheels = 4
    def start_car(self):
        print("Car started")

    def sample(self,brand,model,price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage
        print(brand,model,price,milage)

    def sample2(self):
        print(self.wheels)
        print(self.brand, self.model, self.price, self.milage)

    def sample3(self):
        print(self.wheels)
        self.start_car()

car1 = Car()
car1.sample("Honda","Amaze",900000,14.5)
car1.sample2()
car1.sample3()

#intializing class variable using methods
class Car:
    def initialization_method(self,brand,model,price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage

    def start_car(self):
        print(self.brand+" car having model as "+self.model+"has started")

    def stop_car(self):
        print(self.brand+" car having model as "+self.model+"has stopped")

    def print_car_details(self):
        print("Brand of the car is: "+self.brand)
        print("Model of the car is: "+self.model)
        print("Price of the car is: "+self.price)
        print("Milage of the car is: "+self.milage)

svdi = Car()
svdi.initialization_method("Maruti","Swift VDI",800000,24)

hamz = Car()
hamz.initialization_method("Honda","Amaze",900000,14.5)

svdi.start_car()
svdi.stop_car()
svdi.print_car_details()

hamz.start_car()
hamz.stop_car()
hamz.print_car_details()