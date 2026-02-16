class A:
    __a=5
    def __sample(self):
        print("Inside sample method of class A")

    def print_details(self):
        print(self.__a)
        self.__sample()

obj=A()

obj.print_details()