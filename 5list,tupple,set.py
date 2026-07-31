'''a = [12,32,45,64,87]
print(a[0])  #ordered nature you can access any element at any point of time

# mutable = you can change any value any time
a[2] = 67
print(a[3])
print(a)

#duplicates
t = [1,1,1,2,2,2,4,4,4,4,6,6,6,6,6]

#transversing on list 
l = [10,20,30,40,50]
#transversing on values
for i in l:
    print(i)  # only print values
#transversing on index
for i in  range(0,len(l)):
    print(f"{i} : {l[i]}") #both value and index


# base methods crud- create read update delete
l = [10,20,30,40]
l.append(50)      #append -> add any elment in last or at the end of the list (hetrogenuous)
l.insert(2,55)         #insert-> add value in the middle 
l.insert(4,55)
print(l)
l.pop(3)         #remove element through index of that element
print(l)
l.remove(55) 
print(l)    
#remove elment using that element only and remove only first occurance of list [12,2,2] remove 2 of index1 only it'll not remove index2
l.clear()  #remove all element in list 
m = [23,32,12,98,53,75,56]
m.sort() #arrange according to accending order
print(m)
m.sort(reverse=True)  #decending order
print(m)

#print all positive and negative elements separatelly
p = [2, -5, 3,-1, -8, 7]
print("Given List = ", p)
pos = []
neg =[]
for i in p:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
print("Positive elements = ",pos)
print("Negative elements = ",neg)

#find mean or average of all list elements
a = [12,32,45,64,87]
sum = 0 
for i in a:
    sum = sum + i
avg = sum / len(a)
print(f"Average of elements in given list = {avg}")

#find the greates element and print its index 
a = [12,32,95,88,60,45,64,87]
largest = a[0]
index = 0
for i in range(len(a)):
    if a[i] > largest :
        largest = a[i] 
        index = i 
print(f"Largest element in given list is {largest} , it's index is {index}")

#find the second greatest element and print its index 
a = [12,32,95,88,60,45,64,89]
sec_largest = a[0]
largest = a[0]
for i in a :
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest :
        sec_largest = i

print("Second largest element is ",sec_largest)

#Chech if the list is already sorted
a = [10,20,30,40]
for i in range(len(a)-1) :
    if  a[i] >= a[i+1]:
        print("List is not sorted")
        break
else:
    print("Your list is sorted")

#TUPLE - immutable list - cannot change the elements & use - constant data 
#access element = index      0,      1,       2,   3
a =                    ["monday", "tuesday", 13, 13, 25, 13, 13,13,13,]
tup = tuple(a)       # list -> tupple convert 
print(type(tup))
print(tup[0])  #accessiing element through index same as list
#methods
print(tup.index("tuesday")) #retrun index of that element
print(tup.count(13)) #return how many times that element is in the tuple 

#Use of tuple
def students():
    return "karuna",18,"karunasahu@gmail.com"
info = students()
print(info) #tuple create
name, age, gmail = info #unpack tuple
print(name) 
print(gmail)
'''

#SET = unique values only , unorderd nature
s = {12,13,13,14,14,15,16,16 }
print(s)
