class Laptop:
    def __init__(self,name,conf,ram,ssd,os):
        self.name = name
        self.conf = conf
        self.ram = ram
        self.ssd = ssd
        self.os = os

    def display(self):
        print("Name of a Laptop:",self.name)
        print("Configuration of a Laptop:", self.conf)
        print("RAM of a Laptop:", self.ram)
        print("SSD of a Laptop:",self.ssd)
        print("OS of a Laptop:", self.os)
        print("-------------------------------")
        print("-------------------------------")

for i in range(4):

    obj = Laptop('Dell','i7','4gb','1tb','windows')
    obj.display()