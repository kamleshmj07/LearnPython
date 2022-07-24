""" Demonstrate Python Generator Expression
RefLink: https://www.techbeamers.com/python-generator/
"""

def generator_expr():
  # Define the list
  alist = [4, 16, 64, 256]
  
  # Find square root using the list comprehension
  out = [a**(1/2) for a in alist]
  print(out)
  
  # Use generator expression to calculate the square root
  out = (a**(1/2) for a in alist)
  print(out)
  print(next(out))
  print(next(out))
  print(next(out))
  print(next(out))
  # print(next(out)) # Will throw Error StopIteration




