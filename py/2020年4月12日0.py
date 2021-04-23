def aa(a=1,b=2):
    print("a",a)
    print("a",b)
    print(f"{a}{b}")
    # return f"{a}{b}"

def bb(**a):
    print(a)

class ClassName():
    pass
    def double(self):
        return 2*self.hw

dd=ClassName()

dd.hw=1

print(dd.double(1))


# print("dd.hw :",dd.hw )

def cc(a, b, c):
    pass

cc(a=1,b=2, c=3)

# bb(a=1, b=2)
tt={"a":1, "b":2}
tt={"c":1, "d":2}

# bb(**tt)

# aa(1,2)
