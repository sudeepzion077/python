class static:
    def calculator(x,y):
        return x*y

static.calculator = staticmethod(static.calculator)

z = static.calculator(5,7)

print(z)