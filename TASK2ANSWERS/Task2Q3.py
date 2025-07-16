import pandas as pd
#test
product_url = 'https://raw.githubusercontent.com/Daksh-ino5/Excitel-Internship/main/task%202/products.csv'
price_url = 'https://raw.githubusercontent.com/Daksh-ino5/Excitel-Internship/main/task%202/price_list.csv'

product = pd.read_csv(product_url)
price = pd.read_csv(price_url)

merged = pd.merge(
    product,
    price[['ProductName', 'Price']],
    on='ProductName',
    how='left'
)

merged['Price'] = merged['Price'].fillna("NOT AVAILABLE")

merged.to_csv("TASK2Q3ANS.csv", index=False)
