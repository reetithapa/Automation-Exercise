def my_first_function(name):     #parametrized
    print("Your name is " + name)
my_first_function("Reeti Thapa")     #argument

def my_second_function(name="Reeti Thapa"):       #default argument
    print("Your name is " + name)
my_second_function()


def sum(a,b,c):
    return a+b+c
c=sum(1, 2, 3)
print(c)

#Taking input from user
print("Enter your name:")

name=input()
print("Welcome"+name)

print("Enter first number:")
num1 = input()
print("Enter second number:")
num2 = input()
print("Multiplication of two numbers is:"+str(int(num1)*int(num2)))

#max and min function
ma= max(1,33,5,7,22,87,44)
mi = min(1,33,5,7,22,87,44)

print(ma,mi)

#Local variable
def my_function():
    name= "Reeti Thapa"
    print(name)
my_function()
print(name)   #doesnot prin reeti as this print statement is outside the function

#Global variable
name= "Reeti Thapa"

def my_function():
    print(name)
my_function()
print(name)        #prints reeti as name is declared outside function

def my_function():
    global name          #using global keyword to make it global but inside function
    name = "Reeti Thapa"
    print(name)
my_function()
print(name)

