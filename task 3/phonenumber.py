import re
string = '''
+91 9876543210 -- junk@#$%data1@@@some_text_here
HelloWorld +91-9123456789 :: random_text_123 ### ????
Info: +91 9988776655 &*()_++}{>>“”abc_data_xyz
Customer: +91 9090909090 | garbage--text!!!--junk-data
user001: +91 7788990011 lorem$$$ipsum###donotuse
+91 8888888888 <<-->> text_before && after ~!@#
Name: Rohan, Contact: +91 9812345678 ::!!!--misc-data--!!
Note: +91 7000070000 / test_case__begin__ @#$_end
Data+++: +91 9345678901 $$$random###string$$$data
+91 8008008008 -->*<&% messy_random__##text!!inserted
'''
patt=re.compile(r'\+91\s+\d[0-9]{0,10}')
matches=patt.finditer(string)
for match in matches:
    print(match)
