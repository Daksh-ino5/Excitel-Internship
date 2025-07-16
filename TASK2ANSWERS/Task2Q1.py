import pandas as pd
details_url='http://raw.githubusercontent.com/Daksh-ino5/Excitel-Internship/refs/heads/main/task%202/employee_details.csv'
salary_url='https://raw.githubusercontent.com/Daksh-ino5/Excitel-Internship/refs/heads/main/task%202/employee_salary.csv'
details=pd.read_csv(details_url)
salary=pd.read_csv(salary_url)
merged = pd.merge(
    details,
    salary[['Name', 'DOB', 'Salary']],
    on=['Name', 'DOB'],
    how='left'
)

merged.to_csv("Task2Q1ans.csv",index=False)