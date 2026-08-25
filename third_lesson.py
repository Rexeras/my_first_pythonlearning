# for i in range(8):
#     print(i)
#     print("one")

# number = int(input("enter a number: "))
# for i in range(1, 11):
#     answer = number * i
#     print(number, "x", i, "=", answer)

mylist = ["one", "two", "three"]
# print(mylist)
# myintlist = [1, 2, 3]
# print(myintlist)
# myblist = [True, False, True]
# print(myblist)
# mixlist = ["one", 2, True, "two", 1, False]
# print(mixlist)

total = 0
for results in mylist:
    marks = int(input("Enter your marks:"))
    total = total + marks

print(total)
print(len(mylist))

myAverage = total/len(mylist)
print(myAverage)