import json
# 1. Read and parse nested JSON
# - Load 'student.json' which contains nested JSON
# - Print only the math grade
# - Print each skill in the 'skills' list on a new line
# nested_str={
#     "Name":"Daksh",
#     "Grade":{
#         "math":89,
#         "eng":99
#     },
#     "skills":["IOT","CCNA","SDWAN"]
# }
# with open("student.json", "w") as f:
#     json.dump(nested_str,f)
# with open("student.json", "r") as f:
#     data=json.load(f)
# print(data)
# print("Math grade=",nested_str["Grade"]["math"])
# print("Skills=")
# for skill in nested_str["skills"]:
#     print("->",skill)


# 2. Write a Python dictionary to a JSON file, then read it back
# - Create a dictionary with keys: username, email, verified, followers
# - Save it to 'profile.json'
# - Load it again and print only the username

# data={
#   "username": "daksh_007",
#   "email": "daksh@example.com",
#   "verified": True,
#   "followers": 1570
# }
# with open("profile.json", "w") as f:
#     json.dump(data,f)
# with open("profile.json", "r") as f:
#     data=json.load(f)
# print(data["username"])



# 3. Convert a list of dictionaries to JSON
# - Create a list of student dictionaries with name and marks
# - Write the list to 'students.json' using json.dump with indentation

# student=[
#     {"Name":"Daksh1","Age":26,"Height":9.7},
#     {"Name1":"Daksh2","Age":23,"Height":8.7},
#     {"Name2":"Daksh3","Age":28,"Height":5.9}
#
# ]
# with open("student.json",'w') as f:
#     json.dump(student,f,indent=4)


# 4. Update a key-value pair inside a JSON file
# - Read a JSON file that has 'device' and 'status'
# - Update status from 'inactive' to 'active'
# - Save the updated JSON back to the same file
# device_list={"device":"sensor","status":"inactive"}
# with open("status.json",'w') as f:
#     json.dump(device_list,f,indent=4)
# with open("status.json",'r') as f:
#     data=json.load(f)
# data["status"]="active"
# with open("status.json","w") as d:
#     json.dump(data,d,indent=4)





# 5. Flatten a deeply nested JSON
# - Given a nested dictionary, flatten it into a single dictionary
# - The keys should represent the full path like: person_location_city



# 6. Extract all values of a specific key from a list of JSON objects
# - Given a list of records, extract all 'status' values into a new list
people = [
    {"name": "Daksh", "age": 21},
    {"name": "Shruti", "age": 20}
]
hello=[record["age"] for record in people]
print(hello)


# 7. Parse JSON from an API (Bonus if internet access is available)
# - Use requests.get() to fetch data from GitHub's user API
# - Extract and print the 'login', 'public_repos', and 'bio' fields

# 8. Check if a key exists in a nested JSON
# - Given a deeply nested dictionary, write a function to search for a key like 'c' at any level

# 9. Sort a list of JSON objects by a key
# - Given a list of student dictionaries, sort them by 'marks' in descending order

# 10. Convert JSON to CSV
# - Given a list of dictionaries (name and age), write them to 'people.csv' using the csv module














import pandas as pd

# Original messy DataFrame
data = {
    'Name': ['Daksh1', None, None],
    'Age': [26, 23, 28],
    'Height': [9.7, 8.7, 5.9],
    'Name1': [None, 'Daksh2', None],
    'Name2': [None, None, 'Daksh3']
}

df = pd.DataFrame(data)

# Combine 'Name', 'Name1', 'Name2' into a single 'Name' column
df['Name'] = df['Name'].fillna(df['Name1']).fillna(df['Name2'])

# Drop extra name columns
df = df.drop(['Name1', 'Name2'], axis=1)

# Optional: reset index if needed
df = df.reset_index(drop=True)

print(df)

