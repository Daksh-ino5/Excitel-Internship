import pandas as pd

employee_code_url='http://raw.githubusercontent.com/Daksh-ino5/Excitel-Internship/refs/heads/main/task%202/employee_codes.csv'
df=pd.read_csv(employee_code_url)
list_codes=['E101','E102','E103']#created a list as the filen was missing
matched=df[df['Code'].isin(list_codes)]
print("Doing the reverse lookup")
print(matched[['Code','Name']])