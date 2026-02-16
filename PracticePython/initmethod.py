class Car:
    def  __init__(self,brand,model,price,milage):
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

svdi = Car("Maruti","Swift VDI",800000,24)
hamz = Car("Honda","Amaze",900000,14.5)

svdi.start_car()
svdi.stop_car()
svdi.print_car_details()

hamz.start_car()
hamz.stop_car()
hamz.print_car_details()