import requests
import pandas as pd

url = "http://10.10.11.118:5000/get-services"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("JSON Received:", data)
    df = pd.DataFrame(data["services"])
    print("\n  Table:\n", df)
else:
    print(" Failed with status code:", response.status_code)
print("\nData fetching is successfull")