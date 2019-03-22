class example:
    def __init__(self, a):
        self.a = a


obj1 = example(10)
obj2 = example("a")

a = [obj1, obj2]
a[1].a = 1000
b = [obj2, obj1]

for i in b:
    print(i.a)