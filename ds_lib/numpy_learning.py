import numpy as np


def study_numpy():

  ### Numpy Arrays
  print('--------------------------- Numpy Arrays\n')
  print('1] np.arange(...)\n')
  print(np.arange(0,10))
  print('\n')

  print('2] np.zeros(...)\n')
  print(np.zeros((5,5)))
  print('\n')
  
  print('3] np.linspace(...)\n')
  print(np.linspace(0,10,11))
  print('\n')

  
  ### 1] Generate random numbers for models
  print('--------------------------- Randoms\n')
  print('1] np.random.rand(...)\n')
  print(np.random.rand(1,2,))
  print('\n')

  print('2] np.random.randint(...)\n')
  print(np.random.randint(0,100))
  print('\n')
  
  print('3] np.random.randn(...)\n')
  print(np.random.randn(2,4))
  print('\n')

  ### 2] Seeding the random generation
  print('Seeding before generating random numbers\n')
  print('First attempt......')
  np.random.seed(42) # use any number
  print(np.random.rand(5))

  print('Second attempt......')
  np.random.seed(42)
  print(np.random.rand(5))



"""
  
  ### 3] Other numpy array functions
  arr.reshape(r,c)
  arr.max()
  arr.min()
  arr.argmax() # index of max
  arr.argmin() # index of min


  arr = np.arange(0,10)
  slice_arr = arr[0:5]
  print(slice_arr)
  arr[:5] = 4000
  
  print('\n')
  print(arr)
  print('\n')
  print(slice_arr)

"""

















