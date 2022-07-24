import numpy as np
import pandas as pd


def pd_basics_01():
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

  print("Let's get some info from dataframe now...", '\n')
  print(df.info(), '\n')

  print("Let's read a csv file into a dataframe...", '\n')
  df = pd.read_csv(r'/home/runner/LearnPython/work/tips.csv')
  print(df, '\n')
  
def pd_basics_02():
  print("Let's read a csv file into a dataframe...", '\n')
  df = pd.read_csv(r'/home/runner/LearnPython/work/tips.csv')
  print(df, '\n')

  print('List the columns...', '\n')
  print(df.columns, '\n')
  print('Print the index...', '\n')
  print(df.index, '\n')

  print('Display first "n" rows, here first 3 rows...', '\n')
  print(df.head(3), '\n')

  print('Display last "n" rows, here last 4 rows...', '\n')
  print(df.tail(4), '\n')

  print('For all numeric columns in the df, display basic statistical information using df.describe() ...')
  print(df.describe(), '\n')

def pd_selection_indexing():
  print("Let's read a csv file into a dataframe...", '\n')
  df = pd.read_csv(r'/home/runner/LearnPython/work/tips.csv')
  print(df, '\n')

  print("1] Picking one column from df and checking it's type...", '\n')
  print(df['total_bill'], '\n')
  print(type(df['total_bill']), '\n')

  print("2] Picking multiple columns from df...", '\n')
  print(df[['total_bill', 'tip']], '\n')

  print('3] Adding a new column...', '\n')
  print('Before we do that, a few vector operations on the dataframe...', '\n')
  print('Get the total of tip and the bill...', '\n')
  print(df['tip'] + df['total_bill'], '\n')

  print('Get value for tip as a % of the bill', '\n')
  print(100* df['tip']/df['total_bill'], '\n')
  print('Assign this value to a new column "tip_percentage"', '\n')
  df["tip_percentage"] = 100* df['tip']/df['total_bill']
  print(df.head(5), '\n')

  print('4] Dropping a column "(axis=1)", here "tip_percentage"','\n')
  # df.drop('tip_percentage') # throws error
  print(df.drop('tip_percentage', axis=1).head(2), '\n')
  print('Printing the orignal df...', '\n')
  print(df.head(2), '\n')
  print('Oops! did not actually drop from the dataframe.... Need "inplace=True"!!!', '\n')
  df.drop('tip_percentage', axis=1, inplace=True)
  print(df.head(2),'\n')
  print('Now it did actually drop from the dataframe... This is better!!!', '\n')


  
  print('3] Grab a row or multiple rows', '\n')

  print('4] Insert a new column', '\n')

  print('5] Insert a new row', '\n')


 



