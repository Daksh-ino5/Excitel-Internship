import pandas as pd

file_path = r'C:\Users\Daksh\PycharmProjects\PythonProject\daksh\pandas\TASK1Q&A\testingdata.xlsx'
sheet1 = pd.read_excel(file_path, sheet_name='Sheet1')
sheet2 = pd.read_excel(file_path, sheet_name='Sheet2')


for col1 in sheet1.columns:
    for col2 in sheet2.columns:
        if not sheet1[col1].isna().all() and not sheet2[col2].isna().all():
            if set(sheet1[col1].dropna().astype(str)) & set(sheet2[col2].dropna().astype(str)):
                print(f"Common values in= Sheet1 = {col1} and Sheet2 = {col2}")
