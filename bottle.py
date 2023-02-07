class bottle:
    def __init__(self,volume,type):
        self.volume = volume
        self.type = type

    def reuse(self):
        print("reuse")

    def recycle(self):
        print("recycle")

    def pour(self):
        print("pour")

user = bottle(80,"i am mineral")

print(user.volume)
user.reuse()
user.recycle()
user.pour()
