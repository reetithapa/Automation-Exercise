class Car:
    wheels = 4            #static variable
    def __init__(self,brand,model,price,milage):
        self.brand = brand         #instance variable
        self.model = model
        self.price = price
        self.milage = milage

    def start_car(self):      #instance methods
        print(self.brand+" car having model as "+self.model+" has started")

    @staticmethod
    def print_car_wheels():
        print(Car.wheels)

svdi = Car("Maruti","Swift VDI",800000,24)
hamz = Car("Honda","Amaze",900000,14.5)
print(svdi.brand)
print(svdi.model)
print(svdi.price)      #accessing instance variable
print(svdi.milage)

print(Car.wheels)       #accessing static variablr

svdi.start_car()        #accessing instance methonds
Car.print_car_wheels()   #accessing static methods




