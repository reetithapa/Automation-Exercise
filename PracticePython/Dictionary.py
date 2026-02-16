car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
print(car)
print(type(car))

#get the value of key
car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
print(car.get("Brand"))    #these are two methods to get value of key
print(car["Model"])

#printing all keys of dictionary and values
car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
print(car.keys())
print(car.values())

#updating the values of dictinary
car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
print(car)
car["Price"] = 100000
print(car)

#adding new key vales to the existing dictinary
car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
print(car)
car["Color"]="Black"
print(car)

#using loop with dictionary
car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
for k in car:
    print(k)

for k in car.keys():
    print(k)
    print(car[k])

for k in car:
    print(k,car[k])

for v in car.values():
    print(v)

for k,v in car.items():
    print(k,v)

#removing an item having the specific key from dictionary and returns the value of the removed key
car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
print(car)
car.pop("Brand")
print(car)

del car["Model"]
print(car)

#removing the last item in dictionary and returns the removed element
car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
print(car)
car.popitem()
print(car)

#remove all the key values at a go
car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
print(car)
car.clear()
print(car)

#find the size of dictionary
car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
print(car)
print(len(car))

#delete the compete dictionary
car = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
print(car)

#del car

#print(car)

#comparing dictionary using == and !=      Order of key value pairs doesnot matter
car1 = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.5"
}
car2 = {
    "Brand":"Honda",
    "Model":"Mercedes",
    "Price":"900000",
    "Milage":"14.0"
}
print(car1==car2)










