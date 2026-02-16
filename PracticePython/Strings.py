#ways of creating string
first_name = "Reeti"
last_name = 'Thapa'
location = str("Kirtipur")

print(type(first_name))
print(type(last_name))
print(type(location))

#string works like collection list
first_name = "Reeti"
print(first_name[0])
print(first_name[1])
print(first_name[2])
print(first_name[3])
print(first_name[4])

first_name="Reeti"
for c in first_name:
    print(c)

#length of string text
first_name="Reeti"
print(len(first_name))

first_name="Reeti"
for i in range(len(first_name)):
    print(first_name[i])

#use in and not in operator
first_name="Reeti"
print("eti" in first_name)
print("run" in first_name)

#slicing strings
first_name="Reeti"
print(first_name[1:3])
print(first_name[:])
print(first_name[1:])
print(first_name[:3])

#modifying strings
first_name="Reeti" #uppercase
print(first_name.upper())
print(first_name.lower())   #lowercase

name = "           Reeti Thapa       "
print(name)
print(name.strip())    #removes leading spaces and trailing spaces

name = "Reeti Thapa"
print(name.replace("e","i"))

name = "My name is Reeti Thapa"
words = name.split(" ")

print(words[0])

name = "Reeti Thapa Reeti"
print(name.capitalize())
print(name.title())
print(name.count("Reeti"))
print(name.find("Reeti"))
print(name.find("Python"))

name_one = "Reeti Thapa"
name_two= "Roji Thapa"
print(name_one==name_two)
print(name_one.__eq__(name_two))
print(name_one.casefold()==name_two.casefold())   #eg reeti and Reeti are same...tara mathi ko comparison ma reeti ra Reeti different hunthiyo ysma same hunxa



