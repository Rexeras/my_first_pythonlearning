mylist = ["apple", 2, True, "banana", "kiwi", 3, False]
print(mylist)

print(len(mylist))
print(type(mylist))



thislist = list(("apple", False, 3))
print(thislist)

print(thislist[1])
print(thislist[-1])

print(mylist[1:3])
print(mylist[:3])
print(mylist[-4:-1])

if "apple" in thislist:
    print("Yes, apple is in the list")



thislist[1] = "cherry"
print(thislist)

thislist[1:3] = ["cherry", "watermelon"]
print(thislist)

mylist[1:3] = ["watermelon"]
print(mylist)