# matin = [10, 1, 4, 4.5]
""" #matin[0]="Fatin"
 print(matin[1: len(matin)])
print(matin[-3: -1])    """  # Negative indexing is allowed in only in time of Slicing

# Methods which not return any value
""" #matin.sort()
#matin.sort(reverse=True)
#print(matin.sort(reverse=True))  # None return
#print(matin) """

# Method which is return value
""" matin1=sorted(matin)
print(matin)
print(sorted(matin))
print(matin1) """

# Tuple
# comma na dile string hishebe count corbe but comma dile tuple hobe
""" tup = ("matin", 1, 4, 6, 3, 3, 1, 1,)
print(type(tup))
print(tup)
print("Index:", tup.index(3))
print(tup.count(1)) """

# practice 1

# movies = []
"""mov=input("Enter First Movie:" )
movies.append(mov)
mov=input("Enter Second Movie:")
movies.append(mov)
mov=input("Enter 3rd Movie:")
movies.append(mov) """

""" movies.append(input("Enter first movie:"))
movies.append(input("Enter second movie:"))
movies.append(input("Enter 3rd movie:"))

print(movies)
 """

# Practice 2
tup = ["matin", 1, 4, 5, 7, 4]
""" tup1 = tup.copy()
print(tup1)
tup1.reverse()
print(tup1) """

print(list(reversed(tup)))   # Build in funtion that returns iterator
#print(tup1)