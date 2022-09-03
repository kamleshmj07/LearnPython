"""


"""














































"""
from ds_lib.series_learning import series_basics
series_basics()
"""

"""

from ds_lib.pandas_learning import *
pd_selection_indexing()
"""


"""
# importing pandas as pd
import pandas as pd
  
# Creating the DataFrame
df = pd.DataFrame({"BrandName":["Parle", "Monaco", "GoodDay", "Parle", "GoodDay", "MarieGold", "GoodDay" ], 
                   "B":[7, 2, 54, 3, None, 47, 12], 
                   "C":[20, 16, 11, 3, 8, 14, 9],
                   "D":[15, 21, 6, 31, 11, 17, 7],
                   "wt":[0.5, 1.5, 0.75, 1.25, 1, 0.25, 1.75],
                   "istrue": [True, False, True, False, True, False, True]})
  
# Create the index
index_ = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5', 'Row_6', 'Row_7']
  
# Set the index
df.index = index_

df = df[df["istrue"] == True]

print(df, '\n')

grpd = df.groupby("BrandName")
# indexing with unique values is mandatory on both data sets
print(grpd[["wt"]].apply(lambda x: x/x.sum()))
"""



