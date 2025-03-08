
# DiCTIONARY
""" matin = {
    "name": "mahmudul",
    "ID": "IT-2101919",
    "subject": ["Python", "Java", "C++"],  # list , also we can write tuple

}
# Print dictionary and type
print(type(matin))

# Access in key of dictionary
# print(matin["name"])

# Change the key value(Mutable)
matin["name"] = "Hasan"
matin["ID"] = "IT-21020"
print(matin) """


""" # Create null dictionary
null_dict = {}
print(null_dict)
 """

# Nested Dictionary
""" info = {
    "name" : "matin",
    "subject": {
        "Chem" : 97,
        "math" : 100,
        "Phy"  : 67,
        "Eng"  : 89,
    },                #Careful here, here also has a comma
    "ID" : "IT-21019"
} """

""" print(info)
#Access specific key
print(info["subject"] ["Chem"])
 """
# Dictionary Method
""" print(info.keys())
print(info.values())
print(info["name"])       # If error, then next line could not be execute
print(info.get("name"))  #Method is preferable for error handling, Return none
new_dict  ={
    "city":"Dhaka",
}
info.update(new_dict)   
print(info)
 """

#SET And its Methods
afm = {1,2,4,(1,3,4),"matin",}
collection = set()                                        # Empty set syntex 
collection.add(0)
collection.add(1)
collection.add(2)
collection.add(2)                                         # Ignore this element because of duplicate
collection.add("Hey there, This is Mahmudul Hasan Matin") #String because of immutability
collection.add((1,2,3))                                   #Tuple because of immutability
#collection.add([1,2,34])                                  #Error because of List(Unhashable)
collection.remove(0)
#collection.clear()
collection.pop()


print("Set 1:",afm)
print("Set 2:",collection)
#print(type(collection))
#print(collection.pop())
print(afm.union(collection))
print(afm.intersection(collection))