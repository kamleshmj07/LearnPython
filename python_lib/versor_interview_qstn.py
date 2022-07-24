import pandas as pd

lst_data = [
  {
    "UserId": 1, "Date": "01-01-2022" ,"SecurityId": "IBM", "Units" : 100
  },
  {
    "UserId": 1, "Date": "01-01-2022" ,"SecurityId": "GOOGL", "Units" : 100
  },
  {
    "UserId": 2, "Date": "01-01-2022" ,"SecurityId": "IBM", "Units" : 300
  },
  {
    "UserId": 1, "Date": "01-02-2022" ,"SecurityId": "AAPL", "Units" : 100
  },
  {
    "UserId": 2, "Date": "01-02-2022" ,"SecurityId": "META", "Units" : 100
  },
  {
    "UserId": 2, "Date": "01-02-2022" ,"SecurityId": "IBM", "Units" : 100
  },
  {
    "UserId": 3, "Date": "01-03-2022" ,"SecurityId": "IBM", "Units" : 100
  },
  {
    "UserId": 4, "Date": "01-03-2022" ,"SecurityId": "GOOGL", "Units" : 100
  },
  {
    "UserId": 4, "Date": "01-03-2022" ,"SecurityId": "IBM", "Units" : 100
  }       
]

"""
Pandas Solution
----------------
df = pd.DataFrame(lst_data)
print(df)
df_final = df[df.groupby(by="Date").count()]
print('\n')
print(df.groupby(by=["Date", "UserId"]).count().sort_values("SecurityId").groupby(level=0).tail(1))
"""

distinct_users_info = set([x["UserId"] for x in lst_data])
disinct_date_info = set([x["Date"] for x in lst_data])
dict = {}

for rw in lst_data:
  dict[str(rw["UserId"] + rw["Date"])] =   1
  print(dict.get(str(rw["UserId"] + rw["Date"])))


print(dict)