import pandas as pd


def series_basics():
  
  ### Series
  print('--------------------------- Creating Series', '\n')
  print('1] Creating a series from index list and data list', '\n')
  myindex = ['USA', 'Canada', 'Mexico']
  print('Index : ', myindex, '\n')
  mydata = [1776, 1867, 1821]
  print('Data : ', mydata, '\n')
  myser = pd.Series(data=mydata, index=myindex)
  print('Pandas Series from Index + Data : ', '\n', myser, '\n')
  print('Grab data from Series as if it was an Array ==>', '\n')
  print('Access data by numeric index : ', myser[0], '\n')
  print('Access data by labelled index : ', myser['USA'], '\n')

  print('2] Creating a series from dictionary', '\n')
  ages = {'Sam' : 5, 'Frank' : 10, 'Spike' : 7}
  print('Ages data in dictionary : ', ages, '\n')
  print('Pandas Series from a dictionary : ', '\n', pd.Series(ages), '\n')


  print('--------------------------- Some Series Operations', '\n')
  print('1] .keys() ', '\n')
  q1 = {'Japan' : 80, 'China' : 450, 'India' : 200, 'USA' : 250}
  q2 = {'Brazil' : 100, 'China' : 500, 'India' : 210, 'USA' : 260}
  print('Imaginary Sales data for 2 quarters', '\n\n', q1, '\n\n', q2, '\n')
  sales_q1 = pd.Series(q1)
  sales_q2 = pd.Series(q2)
  print('Converted the above dictionary data into Pandas Series', '\n\n', sales_q1, '\n\n', sales_q2, '\n')
  print('Getting all the keys from q1 series : ', sales_q1.keys(), '\n')

  print('2] Perform broadcasted operations on series : ', '\n')
  print('Multiply q1 sales by 2 : ', '\n\n', sales_q1 * 2, '\n')
  print('Divide q1 sales by 100 : ', '\n\n', sales_q1 / 100, '\n')

  print('2.a] Adding q1 sales and q2 sales for each region : ', '\n')
  print(sales_q1 + sales_q2, '\n\n')
  print('Missing index from either of the series got converted into NaNs...')
  print('So better choice to adjust the two series is use ser1.add(ser2)')
  print(sales_q1.add(sales_q2, fill_value=0))
  print('Similarly you can use built in methods to perform more accurate calculations...')
  









