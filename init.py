class Mobile:
    # init is use for the initialization
    def __init__(self):
        print("Constructor")

    def display(self):
        print("This is method")

# Declaring a object will automatically call the init function. So we call INIT as a constructor.
obj = Mobile()

#Calling the method
obj.display()