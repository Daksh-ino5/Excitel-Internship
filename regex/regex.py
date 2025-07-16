import re
string1='''essay paragraph is a distinct unit of writing, typically composed
           of multiple sentences, that focuses on a single idea or topic. 
           It serves as a building block for longer pieces of writing like 
           essays, helping to organize and structure information for better readability des'''
patt= re.compile(r'es$')
matches=patt.finditer(string1)
for match in matches:
    print(match)


