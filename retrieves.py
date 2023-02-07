class student:
    def __init__(self,x,y,z):
        self.name = x
        self.rollno = y
        self.age = z

    def display(self):

        print("name:",self.name)
        print("roll no:",self.rollno)
        print("age:",self.age)

xl = ["sudeep","preethi","raju","krishna","anand"]
yl = [10,20,30,40,50]
zl = [11,12,13,14,15]
objl = []

for i in range(0,5):
    objl.append(student(xl[i],yl[i],zl[i]))

for i in range(0,5):
    objl[i].display()




