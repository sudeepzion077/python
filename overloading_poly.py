class A:
    def sum(self,a,b):
        return a+b

    def sum(self,a,b,c=1):
        return a+b+c

# over-loading function in the polymorphism
object=A()
print(object.sum(2,3,10))


