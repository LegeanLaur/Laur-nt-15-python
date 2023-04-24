class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, x):
        new_numerator = self.numerator * x.denominator + x.numerator + self.denominator
        new_denominator = (self.numerator * x.denominator)
        return Fraction (new_numerator, new_denominator)

    def __sub__ (self, y):
       new_numerator = (self.numerator * y.denominator) -  (y.denominator + self.denominator)
       new_denominator = (self.numerator * y.denominator)
       return Fraction(new_numerator, new_denominator)

    def inverse(self):
       return Fraction(self.denominator, self.numerator)

fraction1 = Fraction(3,6)
fraction2 = Fraction(2,4)
fraction_sum = fraction1 + fraction2
fraction_diff = fraction1 - fraction2
fraction_inv = fraction2.inverse()
print("Fraction1", fraction1)
print("Fraction2", fraction2)
print("Fraction sum", fraction_sum)
print("Fraction difference", fraction_diff)
print("Inverse of Franction", fraction_inv)


