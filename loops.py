# WHILE LOOP #WHILE LOOP #WHILE LOOP #WHILE LOOP #WHILE LOOP #WHILE LOOP #WHILE LOOP #WHILE LOOP

""" i = 0
while i < 5:
    print('Matin')
    i += 1
print(i) """

# Print Number from 1 to 100 and vice versa
""" i = 1
while i <= 100:
    print(i)
    i += 1 """

# Print the multiplication table of a number n
""" n = int(input("Enter a number :"))
i = 1
while i <= 10:
    print(n*i)
    i += 1
 """

# Using user input by f string
""" n = int(input("Enter a Number: "))
i = 1
while i <= 10:
    #f string which is directly embed variables and expression inside a string.
    print(f"{n}*{i}={n*i}")
    i += 1 """

# Print the elements of a list
""" list=[1,4,34,35,34]
i=0
while i< len(list):  #traverse
    print(list[i])
    i+=1 """

# Search a number in tuple using loop
""" tuple = (1, 3, 4, 5, 6, 7, 7, 77, 78, 77, 77, 89)
n = int(input("Enter number what you want to search: "))
i = 0
while i < len(tuple):
    if (tuple[i] == n):
        print("Found at:", i)

    else:
        print("Finding.....")

    i += 1
 """

# BREAK # BREAK
""" i = 1
while i <= 10:
    print(i)
    if (i == 4):
        break
    i += 1 """
# CONTINUE #CONTINUE
""" i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue #Skip
    print(i)
    i+=1 """


# FOR LOOP #FOR LOOP #FOR LOOP #FOR LOOP #FOR LOOP #FOR LOOP #FOR LOOP #FOR LOOP #FOR LOOP

""" list =[1,3,44,56,43,55,77]    #Also in tuples and string
for val in list:
    print(val) """

""" str = "Mahmudul"
for char in str:
    if(char=='u'):
        print("u found")
        break
    print(char)

else:                #Break statement a else kaj korbe na...
    print("End")
 """
# Searh a number in a tuple using loop   #Linear search
""" tup=[1,3,44,55,66,4,3,33,44]
i=0
n=int(input("Enter the num which you want to search:"))
for el in tup:
    if(n==el):
        print("Found at index:",i)
        break              #If we want to stop when appeared first
    i+=1 """

# range() Function #range() Function
""" for el in range(3, 10, 3):  # range(start,stop,step)
    print(el)
 """
""" #Print odd or even using range() function
for el in range(1,100,2):
    print(el) """
# Print a multiplication table of a number
""" n=int(input("Enter a Number:"))
for i in range(1,11):
    print(n*i)
 """
# pass Statement #pass Statement
""" for el in range(10):
    #dfbjddf

print("Matin")   #IndentationError """

""" for el in range(10):
    pass
if el < 5:
    pass
# No error because of pass statement. We can use that loop block whenever need.
print("Matin") """

# Find sum of first n numbers using while loop
""" n=3
sum=0
i=0
while i<=n:
    sum+=i
    i+=1
print(sum) """
# Using for loop
""" n = int(input("Enter the Number:"))
sum = 0
for i in range(1, n+1):
    sum += i
print("Total sum of the numbers:", sum) """

# Find factorial of a number
n = 4
fact = 1
for i in range(1, n+1):
    fact *= i            # 5!= 1*2*3*4*5
print(fact)

