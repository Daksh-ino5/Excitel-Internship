import re
string1 = '''Hello my phone number is dakshnaithani2004@gmail.com'''
patt = re.compile(r'[a-zA-Z.+-_]+@[a-zA-Z]+\.[A-Za-z]{2,}')
matches = patt.findall(string1)
print(matches)
