"""
The dunder methods or data-model methods "__ function __"
  >> The python data-models is a means by which you can implement protocols, protocols may have abstract meaning.
  >> There are some "Top level functions" (ex. len(..), repr(..)) that allows us to invoke that protocol

############### main.py ##############
x+y     -->    __add__
init x  -->    __init__
repr(x) -->    __repr__
x()     -->    __call__

from python_lib.data_models import Polynomial


p1 = Polynomial(1, 2, 3) #  x² + 2x + 3
p2 = Polynomial(3, 4, 3) # 3x² + 4x + 3

print(p1+p2)
print(len(p1))
print(repr(p1))
######################################

  >> Reference link: https://docs.python.org/3/reference/datamodel.html#basic-customization

"""

class Polynomial():
  def __init__(self, *coeffs):
    self.coeffs = coeffs

  def __repr__(self):
    return 'Polynomial(*{!r})'.format(self.coeffs)

  def __add__(self, other):
    return Polynomial(*( x + y for x,y in zip(self.coeffs, other.coeffs)))

  def __len__(self):
    return len(self.coeffs)  # Gives degree of the polynomial


