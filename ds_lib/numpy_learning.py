import numpy as np

def creating_numpy_array():

  ### Numpy Arrays
  print('--------------------------- Numpy Arrays', '\n')
  print('1] np.arange(...)', '\n')
  print(np.arange(0,10), '\n')
  
  print('2] np.zeros(...)', '\n')
  print(np.zeros((5,5)), '\n')

  print('3] np.linspace(...)', '\n')
  print(np.linspace(0,10,11), '\n')

  print('4] np.ones(...)', '\n')
  print(np.ones((3,4)), '\n')

  print('5] np.full(...)', '\n')
  print(np.full((5,5), 77), '\n')

  ### Generate random numbers for models
  print('--------------------------- Randoms', '\n')
  print('1] np.random.rand(...)', '\n')
  print(np.random.rand(1,2,), '\n')

  print('2] np.random.randint(...)', '\n')
  print(np.random.randint(0,100), '\n')
    
  print('3] np.random.randn(...)', '\n')
  print(np.random.randn(2,4), '\n')
  
  print('4] Seeding before generating random numbers', '\n')
  print('First attempt to generate random numbers......')
  np.random.seed(42) # use any number
  print(np.random.rand(5), '\n')

  print('\nSecond attempt......')
  np.random.seed(42)
  print(np.random.rand(5), '\n')



def numpy_basic_attributes():

  ### Numpy Arrays Basic Attributes
  print('--------------------------- Numpy Arrays Basic Attributes', '\n')
  print('1] ndim, size, shape attributes of array', '\n')
  arr = np.random.randint(10, size=(3,4,5))
  print(arr, '\n')
  print('ndim : ', arr.ndim)  
  print('shape : ', arr.shape)
  print('size : ', arr.size, '\n')

  print('2] dtype, itemsize, nbytes attributes of array', '\n')
  print('dtype : ', arr.dtype)
  print('itemsize : ', arr.itemsize, ' bytes')
  print('nbytes : ', arr.nbytes, ' bytes')



def numpy_key_functions():
  ### Other numpy array functions
  print('--------------------------- Few other functions of numpy', '\n')
  arr = np.arange(0,100,10)
  print('Array : ', arr, '\n')
  print('Re-shaping the array arr.reshape(...)', '\n')
  print(arr.reshape(2,5), '\n')
  
  print('Get Max arr.max() : ', arr.max(), '\n')
  print('Get Index of Max arr.argmax() : ', arr.argmax(), '\n')
    
  print('Get Min arr.min() : ', arr.min(), '\n')
  print('Get Index of Min arr.argmin() : ', arr.argmin(), '\n')
  


def numpy_slicing_dicing():
  ### Slicing concepts of array
  print('--------------------------- Array slicing concepts', '\n')
  arr = np.arange(0,10)
  print('Original Array : ', arr, '\n')
  sliced_arr = arr[0:5]
  print('Sliced Array : ', sliced_arr, '\n')
  print('Broadcasting one value in the original array for first 5 elements : ', '\n')
  arr[:5] = 4000
  print('Original Array Updated To : ', arr, '\n')
  print("It's impact on the sliced array : ", sliced_arr, '\n')
  


def numpy_basic_operations():
  arr = np.arange(0,10)
  print('Array : ', arr, '\n')
  print('--------------------------- Arithmetic Operations : ', '\n')
  print('Addition by 5 : ', '\n', arr + 5, '\n')
  print('Substraction by 2: ', '\n', arr - 2, '\n')
  print('Multiplication by itself  : ', '\n', arr * arr, '\n')
  print('Addition by itself : ', '\n', arr + arr, '\n\n')

  print('--------------------------- Other Math Operations', '\n')
  print('Square Root of itself : ', np.sqrt(arr), '\n')
  print('Sin of itself : ', np.sin(arr), '\n')
  print('Log of itself : ', np.log(arr), '\n')
  print('Square Root of itself : ', np.sqrt(arr), '\n')


