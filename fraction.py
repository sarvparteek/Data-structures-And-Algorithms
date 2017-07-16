'''Author: Sarv Parteek Singh
   Course: CISC 610
   Term: Late Summer
   HW: 1
   Problem: 2
'''


# Greatest common Divisor
def gcd(m, n):
  while m % n != 0:
      oldm = m
      oldn = n

      m = oldn
      n = oldm % oldn
  return n


class Fraction:
  #Constructor
  def __init__(self,num,den=1): #add a den of 1 in case of integer (and not fractional) input
      if (isinstance(num,int) and isinstance(den,int)):
          common = gcd(num, den)
          self.num = num//common
          self.den = den//common
      else:
          raise RuntimeError("Neither numerator nor denominator can have a non-integer value")

  #Override string operator
  def __str__(self):
      return str(self.num) + "/" + str(self.den)

  #Override add operator
  def __add__(self,other):
      return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)

  #Override sub operator
  def __sub__(self,other):
      return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)

  #Override mul operator:
  def __mul__(self,other):
      return Fraction(self.num * other.num, self.den * other.den)

  #Override truediv operator
  def __truediv__(self, other):
      return self.num * other.den, self.den * other.num

  # Override eq operator
  def __eq__(self, other):
      return (self.num *other.den == other.num * self.den)

  #Override ne operator
  def __ne__(self, other):
      return (self.num * other.den != other.num * self.den)

  #Override gt operator
  def __gt__(self, other):
      return (self.num * other.den) > (other.num * self.den)

   # Override ge operator
  def __ge__(self, other):
      return (self.num * other.den) >= (other.num * self.den)

  #Override lt operator
  def __lt__(self, other):
      return (self.num * other.den) < (other.num * self.den)

   # Override le operator
  def __le__(self, other):
      return (self.num * other.den) <= (other.num * self.den)

  #Accessor functions
  def getNum(self):
      return self.num
  def getDen(self):
      return self.den

  def show(self):
      print(self.num, "/", self.den)


'''Test cases
frac1 = Fraction(3,4)
frac2 = Fraction(4,7)
print("Fraction 1 is",frac1)
print("Fraction 1's numerator is",frac1.getNum())
print("Fraction 1's denominator is",frac1.getDen())
print("Fraction 2 is", frac2)
print("Fraction 2's numerator is",frac2.getNum())
print("Fraction 2's denominator is",frac2.getDen())
print("Fraction 1 + Fraction 2 =",frac1 + frac2)
print("Fraction 1 - Fraction 2 =",frac1 - frac2)
print("Fraction 1 * Fraction 2 =",frac1 * frac2)
print("Fraction 1 / Fraction 2 =",frac1 / frac2)
print("Fraction 1 == Fraction 2 is",frac1 == frac2)
print("Fraction 1 != Fraction 2 is",frac1 != frac2)
print("Fraction 1 > Fraction 2 is", frac1 > frac2)
print("Fraction 1 >= Fraction 2 is", frac1 >= frac2)
print("Fraction 1 < Fraction 2 is", frac1 < frac2)
print("Fraction 1 <= Fraction 2 is", frac1 <= frac2)
'''