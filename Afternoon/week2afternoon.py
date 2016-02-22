#for loops
"""
for an_item in whatever_list_you_have:
    do something
"""


for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)

#lists
numbers = [0,1,2,3,4,5,6,7,8,9,10,11]
listOfChar = "ListOfChar"
['L','i','s','t','O','f','C','h','a','r']
["Hello", "There"]
[True, False, True, False, True]

print(numbers[3])
print(listOfChar[-2])

numbers.append(12)
print(numbers)

numbers.extend([13,14,15,16])
print(numbers)

numbers.append("string")
print(numbers)

numbers.remove("string")
print(numbers)

random = [5,4,3,6,10,9,1,2,7,8]
random.sort()
print(random)

randomStrings = ["python", "dogs", "cats", "snake"]
randomStrings.sort()
print(randomStrings)
print(randomStrings.count("python"))
print(len("python"))
print(len(randomStrings))

"""
print out every item in randomStrings using a for loop
print out the even numbers in numbers using a for loop, if statement, comparators, and modulo
print out the maximum and minimum of random without using sort()
"""
4%2==0
5%2==1
for i in randomStrings:
    print(i)

for i in numbers:
    if i%2==0:
        print(i)

