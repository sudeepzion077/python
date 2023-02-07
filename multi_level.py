# single inheritance
class Parent:
    def fun1(self):
        print("This is Parent class")

class Child(Parent):
    def fun2(self):
        print("This is Child class")

class GrandChild(Child):
    def fun3(self):
        print("This is GrandChild one")

class GrandChild2(GrandChild):
    def fun4(self):
        print("This is GrandChild two")

# Object has been created for the Child . We can access parent from the Child.
obj = GrandChild2()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()

