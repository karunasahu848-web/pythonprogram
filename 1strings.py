""" a = "h" 
print(ord(a)) # unicode(unique cide/value) inside a 
a = 'COLLEGE'
indexing - num given to particular place +veindexing( index6= E always start from 0) -ve indexing(starts from last word -1 index-1 = E)
print(a[4],a[-3])
String Slicinng - portion of any stirng a[start: stop: step]  stop -> where u want to stop in index add 1
print(a[1:5:1])#index4 pe stop hona tha to index 4+1 = 5
print(a[0:7:2])#CLEE or print(a[::2]) default values  and a[:::] -> COLLEGE
"""
"""
b = "Hello How are you"
print(b[6:9:])#print how
print(b[14:17:])#print you
print(b[0:5:])#print hello"""


#TYPE CONVERSION 
a = "23"
b = int(a)
c = float(a)
d = bool(a)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#7 value bool - false,0,0.00,empty string"",{},[],()