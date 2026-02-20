#Fraction

class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        temp_num = self.num * other.den + self.den * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    def __sub__(self, other):
        temp_num = self.num * other.den - self.den * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return Fraction(temp_num, temp_den)
    
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print("Addition:", f1 + f2)
print("Subtraction:", f1 - f2)
print("Multiplication:", f1 * f2)
print("Division:", f1 / f2)