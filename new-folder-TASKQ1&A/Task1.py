import pandas as pd


input_file = r'/daksh/pandas/testingdata.xlsx'
sheet1 = pd.read_excel(input_file, sheet_name='Sheet1')
sheet2 = pd.read_excel(input_file, sheet_name='Sheet2')

swe_map = sheet2.set_index('Serial')['S/W Rev'].to_dict()

sheet1['S/W Rev'] = sheet1['ONU Device Serial Number'].map(swe_map)

sheet1.to_excel('sheet1_with_swe_column.xlsx', index=False)
