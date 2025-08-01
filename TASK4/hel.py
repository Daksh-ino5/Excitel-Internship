import json
import pandas as pd
import numpy as np
with open("student.json","r") as f:
    df=pd.DataFrame(json.load(f))
print(df)
