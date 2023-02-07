class Person:
  def __init__(self,name,age,height,weight,catch_phrase):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
    self.catch_phrase = catch_phrase

  def walk(self):
    print("walking")

  def sleep(self):
    print("sleeping")
    print("eating")

user = Person("salman",55,177,79,"i like to play")

print(user.name)
print(user.age)
print(user.height)
print(user.weight)
print(user.catch_phrase)
user.sleep()
user.walk()

