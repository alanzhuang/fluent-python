class A:
    def __getitem__(self, item):
        return [1,2][item]
a= A()
for b in a:
    print(b)