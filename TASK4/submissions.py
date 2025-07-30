import pandas as pd

#1
s=pd.Series([10,20,30])
print(s)

#2
df=pd.DataFrame(
    {
        'A':[1,2,3],
        'B':[4,5,6]
    }
)
print(df)

#new dataframe
df=pd.DataFrame(
    {
        'A':[1,2,3,4,4,4,4,],
        'B':[4,5,6,4,4,4,4],
        'C':[7,5,6,4,7,4,4],
        'D':[8,9,10,4,4,4,4],
        'E':[11,12,13,4,4,4,4]
    }
)

#3
print(df.head(5))

#4
print(df.tail(3))

#5
print(df.columns.to_list())

#6
print(df.info)

#7
print(df.describe())

#8
s=df["A"]
print(s)

#9
s=df[['A','B']]
print(s)

#10
print(df.iloc(0,2))

#11
print(df["A"]>2)

#12
df["D"]=df["A"]+df["B"]

#13
df=df.drop(columns='C',errors=ignore)

#14
print(df.sort_values(by='B',ascending=True))

#15
df=df.reset_index(drop=True)
print(df)

#16
df=df.set_index("C")
print(df)

#17
df=df.rename(columns={'A':'Alpha'})

#18
print(df.isnull())

#19
print(df.fillna(0))

#20
print(df.dropna())

#21
print(df["C"].unique())

#22
print(df["C"].value_counts())

#23
df=df["A"].astype(str)

#24
df=pd.read_csv("testing.csv")

#25
df_csv.to_csv("output.csv",index=True)

#26
grouped=df.groupby("C")["A","B"].mean(numeric_only=True)
print(df)

#27
df1=df.copy()
merged=pd.merge(df,df1,on="Key")
print(merged)

#28
df1=df.copy()
df.T
df1.T
merged=pd.merge(df,df1,how="outer")
print(merged)

#29
def square(x):
    return x**2
df["A"]=df["A"].apply(square)

#30
df=pd.DataFrame(
    {
        "A":[0,1,2],
        "B":["Hello","Hi","How"],
        "C":[4,5,6]
    }
)
pivot=df.pivot_table(index="A",columns='B',values="C")
print(pivot)

#31
df_hier = df.copy()
df_hier.index = pd.MultiIndex.from_product([['row1', 'row2'], ['one', 'two', 'three']])
print(df_hier)
df_unstack=df_hier.unstack()
print(df_unstack)

#32
dates=pd.date_range("2021-01-01",periods=10)
df=pd.DataFrame(
    {
        'A': [1,2,3,4,5,6,7,8,9,10]
    },
  index=dates
   )
print(df)

#33
df2=df.resample('ME').mean()
print(df2)

#34
df['A'].plot(kind='line')
plt.show()

#35
json_str='{"C":[1,2,3],"D":[4,5,6]}'
df=pd.read_json(json_str)
print(df)

#36

#37

#38


#39
grouped = df.groupby('C').agg({'A': 'sum', 'B': 'mean'})
print(grouped)

#40
pivot_df= pd.pivot_table(df, index='C', values=['A', 'B'], aggfunc={'A': 'sum', 'B': 'mean'})
print(pivot_df)

