class A:
    a=5

    def sample(self):
        print("inside sample method of class A")

class B(A):
    a=10

    def sample(self):
        print("inside sample method of class B")

    def print_properties(self):
        print(super().a)
        super().sample()

obj = B()
obj.print_properties()