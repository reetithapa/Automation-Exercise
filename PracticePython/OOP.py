#creating class

class Car:
    wheels = 4
    def start_car(self):
        print("Car started")

#creating obejcts
hamaze = Car()      #object reference   hamaze is refering to object car()
                   #we use object reference to access variables and methods of class
print(hamaze.wheels)
hamaze.start_car()

svdi = Car()
print(svdi.wheels)
svdi.start_car()
