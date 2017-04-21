# classes - yay

class Fraction():
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def __str__(self):
		return "%s/%s" % (self.numerator, self.denominator)

	def __float__(self):
		return self.numerator / self.denominator

	def __add__(self, other):
		return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.numerator)

	def __mul__(self, other):
		return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

	def __eq__(self, other):
		return self.numerator == other.numerator and self.denominator == other.denominator

# casses encapsulate internal states and 

myFrac = Fraction(1,2)
print(myFrac)
print(myFrac + Fraction(1,1))
print(myFrac * Fraction(1,2))
print(myFrac == Fraction(1,2))

#print(float(myFrac) * 100)