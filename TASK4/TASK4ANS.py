import re
import pandas as pd

file_path=r'C:\Users\Daksh\PycharmProjects\PythonProject\Backup\TASK4\Daksh.xlsx'
df=pd.read_excel(file_path)

def extractMACANDREASON(message):

 mac_match=re.search(r'[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}',message)
 mac=mac_match.group() if mac_match else None

 reason_match=re.search(r'auditd\[0\]: (.*?)PON',message)
 reason=reason_match.group(1) if reason_match else "Unkown"

 return pd.Series([reason,mac])

df[["Shutdown_reason","MAC_Address"]]=df["message"].apply(extractMACANDREASON)

pivot_table=df.pivot_table(index="MAC_Address",columns="Shutdown_reason",aggfunc='size',fill_value=None)
pivot_table.reset_index(inplace=True)

Output_path=r'C:\Users\Daksh\PycharmProjects\PythonProject\Backup\TASK4\correct.xlsx'
pivot_table.to_excel(Output_path,index=False)


