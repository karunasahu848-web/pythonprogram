'''d = {"key":"value",1:10,"hello":"world","age":18}
#dont use same key to store different value 
print(d["key"]) #read -  key act as index in dictionary 


#Vanilla python
#C_R_U_D ->>  Create  Reading
d["name"] =  "Karuna" #add new key and value
print(d["hello"])     # ReAding a value
d["age"] = 19       # Update value of already existing
del d[1] #delete key and its value

# Method of approach
a = {10:100,20:200,30:300,40:400,50:500}
a.clear() #Empty dict ->> delete each and every key and its value
print(a.get(30)) #as read to a value 
print(a.items()) #create different tuple of pair of different keys and values 
print(a.keys()) # Return all the keys in form of List 
print(a.values()) # Return all the values in form of List
print(a.pop(40)) # Delete the key and value 
a.popitem()  # Delete last 




key and its value
print(a.setdefault(60,600)) #add ney key to the dict 
a.update({70:700})   #Can add new key&val and also change existing key&val
print(a)

#traversing in dict
for i in a:
    print(f"Key {i} : value {a[i]}")

#Merge twodicctionary into one
d1 = {"a":10,"b":20}
d2 = {"c":50,"d":80}
d1.update(d2)
print(d1)
for i in d2:
    d1[i] = d2[i]
print(d1)


#SUM all values in a dictionary 
s = {"a":10,"b":20,"c":30,"d":40}
sum = 0
for i in s:
    sum = sum + s[i]
print(sum)

#Count the frequency of each element in a list using a dictionary 
l = ["a","s","g","a","b","s","a","g"]
d = {}
for i in l:
    if i in d.keys():
        d[i] += 1
    else :
        d[i] = 1
print(d)

#Combine two dict adding values for common keys
d1 = {"a":10,"b":20,"c":40}
d2 = {"c":50,"d":80,"e":20}
for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]
print(d1)
'''




#EXEPTION HANDLING
''' #Errors(unfixable) ->> 1 Taberror
print("HEllo"    ->>  2 Syntax Error
for i in range(0,11):
print(i)   ->> 3 indentation error

#Exception (Handleable)
#Zero divide error
a = 50
b = int(input("Enter your num->> ")) #enter -> 0
print(a/b) #zeroerror
#Type error 
a = "10"
b = 5
print(a + b) # adding string with a int 
#Value error
c = int("helo") #to convert in int there should be a num

a = int(input("Enter 1st num->> "))
b = int(input("Enter 2nd num->> "))
try : #catch all the errors 
    print(a/b)
except Exception as err: # konsa error btaega 
    print(f"SOrry an error occured as {err}")
else: 
    print("No error occured") 
finally:
    print("Always runs no matter what....")
name = input("Enter your name->> ")
print(f"Hello your name is{name}")

#Raise ->> Manually error or exception throw like age<18 error -> 
age = int(input("Enter your age->> "))
if age<18 :
    raise ValueError("You are not eligible...")
print("congratulation! Your are eligible.")'''



