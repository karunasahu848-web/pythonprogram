# for - use when range is given
# while - works when condition
#FOR LOOP for nums
'''range(10,101,1)
range(23,57,3)
range(0,46,1)
n = int(input("Enter any num :"))
for i in range(n,(n*10) + 1,n) :
    print(i)
#for loop for string
a = "Karuna"
for i in a:
    print(i)
for i in range(len(a)):
    print(a[i])
b = input("Enter your name :")
for i in range(len(b)) :
    print(f"{i} : {b[i]}")

#break , conntinue and else(jb loop me break nhi chalega tb else chalega )
for i in range (11):
    if i == 4:
        continue
    if i == 92:
        break
    print(i)
else :
    print("No break was encountered.")

#print hello world n times
n = int(input("Enter the num the times u want to print hello world :"))
for i in range(n):
    print("hello world")

# print natural num from 1 to n  and reverse n to 1
n = int(input("Enter your num:"))
for i in range(1,n+1):
    print(i)
print("above num in reverse:- ")
for i in range(n,0,-1):
    print(i)

# print the multipllication table of a num
n = int(input("Which table you want :"))
for i in range (1,11):
    print(f"{n} * {i} = {n*i}")

#Sum of firsy n natural num
a = 0
n = int(input("Enter number :"))
for i in range(1, n+1):
     a = a + i
print(a)
#factorial of a num
a = 1
n = int(input("Enter num whose factorial u want:"))
for i in range(1,n+1):
        a = a * i
print(a)

# Print sum of all even and odd nnums between 1 - 10 separately
a = 0
b = 0
for i in range(1,11,2):
    a = a + i 
print(f"Sum of all odd numbers between 1 - 10 is {a} ")
for i in range(2,11,2):
    b = b + i
print(f"Sum of all even numbers between 1 - 10 is {b}")

# Print sum of all even and odd nnums in a range separately
n = int(input("enter your number : "))
a = 0
b = 0 
for i in range(1,n+1,2):
    a = a + i
print(f"Sum of all odd numbers between 1_n is {a} ")
for i in range(2,n+1,2):
    b = b + i
print(f"Sum of all even numbers between 1 - 10 is {b}")
#or
n = int(input("enter your number : "))
a = 0
b = 0
for i in range(1,n+1):
    if i % 2 == 0 :
        a = a + i
    else:
        b = b + i
print(f"Sum of all odd numbers between 1-n is {b} ")
print(f"Sum of all even numbers between 1-n is {a}")

# Print all the factors of a num
n = int(input("Enter the num whose factor u want:"))
for i in range(1,n+1):
    if n % i == 0:
        print(i)

# Check if a num is perfect (sum pf factors = the num itself)
n = int(input("Enter any num :"))
a = 0
for i in range(1,n+1):
    if n % i == 0 and n != i :
        a = a + i
if a == n :
   print(f"Given number {n} is Perfect number")
else:
    print(f"Given number {n} is not a Perfect Number")

# Check if a number is prime
n = int(input("Enter any num :"))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("It is Prime number.")
else:
    print("Not a prime number")'

# reverse a string without using function
a = "I am Karuna sahu"
rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + n[i]
print(rev)  

# check if string is pallandrome or not 
n = input("Enter your string:")
rev = ""
for i in range(len(n)-1,-1,-1):
    rev = rev + n[i]
if rev == n:
    print("Given string is pallindrome.")
else:
    print("Not a pallindrome.") 
#count letters, digits, and special symbols in a string
a = input("Enter any string :-")
char = 0
schar = 0 
dig = 0 
for i in a:
    if i.isdigit():
        dig = dig + 1
    elif i.isalpha():
        char = char + 1
    else:
        schar = schar + 1
print(f"No of charcters in given string is {char}")
print(f"No of digis in given string is {dig}")
print(f"No of special charcters in given string is {schar}")
#or
a = input("Enter any string :-")
char = 0
schar = 0 
dig = 0 
for i in a:
    if 48 <= ord(i) and ord(i)<=57:
        dig = dig + 1
    elif ord(i)>=97 and ord(i)<=122:
        char = char + 1
    elif ord(i)>=65 and ord(i)<=90:
        char = char + 1
    else:
        schar = schar + 1
print(f"No of charcters in given string is {char}")
print(f"No of digis in given string is {dig}")
print(f"No of special charcters in given string is {schar}")

# WHILE LOOP
a = 1
while a != 20:
    print(a)
    a = a + 1

# Separate each digit of a number and print on a new line{reverse num }
a = int(input("Enter any num: "))
while a > 0:
    print(a%10)
    a = a // 10

# Accept a num and print its reverse
a = int(input("Enter a num whose rev u want : "))
rev = 0
while a > 0 :
    rev = rev * 10 + a % 10
    a = a // 10   
print(rev)
    
#Check if a num is pallindrome (equal to its reverse)
n = int(input("Enter your number : "))
copy = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
if rev == copy:
    print("Given number is pallindrome")
else:
    print("not a palindrome")'''

#