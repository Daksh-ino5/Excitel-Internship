import pandas as pd
from fuzzywuzzy import process
customA_url='https://raw.githubusercontent.com/Daksh-ino5/Excitel-Internship/refs/heads/main/task%202/customers_a.csv'
customB_url='https://raw.githubusercontent.com/Daksh-ino5/Excitel-Internship/refs/heads/main/task%202/customers_b.csv'
a=pd.read_csv(customA_url)
b=pd.read_csv(customB_url)
results=[]
for name in b['Name']:
     match=process.extractOne(name,a['Name'])
     results.append((name,match[0]))
df=pd.DataFrame(results,columns=['Name_B','Name_A_matched'])
print(df)
df.to_csv("TASK2Q2ans.csv",index=False)

