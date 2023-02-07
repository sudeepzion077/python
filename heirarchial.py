# single inheritance
class Parent:
    def fun1(self):
        print("This is Parent class")

class Child1(Parent):
    def fun2(self):
        print("This is Child1")

class Child2(Parent):
    def fun3(self):
        print("This is Child2")


# Object has been created for the Child1 . We cannot call Child2.
obj1 = Child1()
obj1.fun1()
obj1.fun2()

# Object has been created for the Child2 . We cannot call Child1.
obj2 = Child2()
obj2.fun1()
obj2.fun3()



