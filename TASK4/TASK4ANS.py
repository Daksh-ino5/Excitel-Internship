import pandas as pd
import re

file_path = r"C:\Users\Daksh\PycharmProjects\PythonProject\Backup\TASK4\Daksh.xlsx"
df = pd.read_excel(file_path)

def extract_mac_and_reason(message):
    mac = re.search(r'[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}', message).group()
    reason = re.search(r'auditd\[0\]: (.*?) PON', message).group(1)
    return pd.Series([mac, reason])

df[['MAC_Address', 'Shutdown_Reason']] = df['message'].apply(extract_mac_and_reason)

pivot_table = df.pivot_table(index='Shutdown_Reason', columns='MAC_Address', aggfunc='size', fill_value=0)
pivot_table.reset_index(inplace=True)

output_path = r"C:\Users\Daksh\PycharmProjects\PythonProject\Backup\TASK4\Reason_MAC_Report.xlsx"
pivot_table.to_excel(output_path, index=False)

