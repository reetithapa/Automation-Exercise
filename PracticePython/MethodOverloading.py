class A:
    def sample(self,a=None,b=None):
        if a!=None and b!=None:
            print(a*b)
        elif a!=None:
            print(a)
        else:
            print("Nothing")

obj=A()
obj.sample(5,4)