import json
import pandas as pd
import numpy as np
import time

with open("student.json","r") as d:
    df=pd.DataFrame(json.load(d))
print(df)
df.loc[1,"Name"]="aryan"
df.loc[2,"Name"]="ayush"
df["Weight"]=[70,56,43]
df["BMI"]=df["Weight"]*2/df["Height"]**2
print(df)
df=df.drop(["Name1","Name2"],axis=1,errors='ignore')
print(df)
json_str=df.to_dict(orient="records")
print(json_str)
with open("student.json","w") as d:
    json.dump(json_str,d,indent=5)
df["A"] = range(1, len(df)+1)
print(df)
json_str=df.to_dict(orient="records")
print(json_str)
with open("student.json","w") as f:
    json.dump(json_str,f,indent=5)


