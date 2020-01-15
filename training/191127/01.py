

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def dvi(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4,2)
a.add()
print(a.add())
print(a.mul())
print(a.sub(),a.dvi())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,2)
print(a.pow())


class SafeFourCal(FourCal):
    def dvi(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.dvi())

class family:
    lastname = '박'

print(family.lastname)

a = family()
b = family()
print(a.lastname)
print(b.lastname)
