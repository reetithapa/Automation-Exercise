from abc import ABC, abstractmethod


class A(ABC):

    def __init__(self,a):
        self.a = a


    @abstractmethod
    def method_one(self):
        pass

    @abstractmethod
    def method_two(self):
        pass

    #non abstract method
    def method_three(self,):
        print("method_three",self.a)

class B(A):
    def method_one(self):
        print("method_one")

class C(B):
    def method_two(self):
        print("method_two")

obj = C(9)
obj.method_one()
obj.method_two()
obj.method_three()

