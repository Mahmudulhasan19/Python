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

# BREAK
""" i = 1
while i <= 10:
    print(i)
    if (i == 4):
        break
    i += 1 """
#CONTINUE
i=1
while i<=10:
    if(i==5):
        i+=1
        continue
    print(i)
    i+=1