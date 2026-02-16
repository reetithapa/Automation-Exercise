class A:
    __age = 0
    def set_age(self,age):
        A.__age = age

    def get_age(self):
        return A.__age

obj = A()
obj.set_age(20)
print(obj.get_age())
