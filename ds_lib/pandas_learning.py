import numpy as np
import pandas as pd


def pandas_basics():
  print('1] Create a dataframe', '\n')
  np.random.seed(101)
  mydata = np.random.randint(0, 101, (4,3))
  print('Random numpy based array', '\n')
  print(mydata, '\n')
  
  myindex = ['CA', 'NY', 'AZ', 'TX']
  print('Adding index to the data', '\n')
  print(myindex, '\n')
  
  mycolumns = ['Jan', 'Feb', 'Mar']
  print('Adding columns to the data', '\n')
  print(mycolumns, '\n')
  
  print('Now a dataframe without index/columns', '\n')
  df = pd.DataFrame(mydata)
  print(df, '\n')

  print('Now a dataframe with index only', '\n')
  df = pd.DataFrame(mydata, index=myindex)
  print(df, '\n')
  
  print('Now a dataframe with columns only', '\n')
  df = pd.DataFrame(mydata, index=myindex, columns=mycolumns)
  print(df, '\n')

  print("Let's get some info now.....", '\n')
  print(df.info(), '\n')



  
  print('2] Grab a column or multiple columns', '\n')

  print('3] Grab a row or multiple rows', '\n')

  print('4] Insert a new column', '\n')

  print('5] Insert a new row', '\n')






