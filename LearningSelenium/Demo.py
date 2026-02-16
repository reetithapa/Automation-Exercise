import Calculator

obj1 = Calculator.A()
print(obj1.addition(5,4))
print(obj1.subtraction(5,4))

obj2 = Calculator.B()
print(obj2.multiplication(5,4))
print(obj2.division(5,4))


text = "programming"
freq = {}
for char in text:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1
