# Strings (str)

str # <-- this is purple which means it is a key word

'''
What is an str?
    An str is a "string" of characters

What do we use them for?
    Anything that can be represented by characters on the keyboard
      examples:
        -names
        -sentences
        -jibberish
'''

# Stuff we can do with strings:

# we can get its how many characters a string: using len
# Remember: spaces count as a character

len

##s = "jibjab"
##print(len(s)) # what does this print?
##print(len("Hi guys")) # what does this print?

'''
Addition:
    what does it mean to add strings?

    s1 = "I love"
    s1 = "cats"
    s1 + s2 returns I lovecats
'''

##print("me" + "et")
##print("Hi" + " " + "guys")


'''
Indexing: we can get one character from a string

s =  "Hi guys"
      0123456

s[0] returns "H"
s[4] returns "u"

IMPORTANT to note:
    - count from 0
    - spaces count
'''

##s = "cuckooo"
##
##print(s[0]) 
##print(s[3])

'''
Slicing: we can get a slice(part) of a string

s =  "Hi guys"
      0123456

s[0:2] returns "Hi"
s[2:7] returns " guys"
s[:4]  returns "Hi g"
s[3:]  returns "guys"
s[1:3] returns ??

'''

s = "minecraft"

##print(s[:4])
##print(s[4:])

# Put it all together:

##s = "anteaters"
##    #012345678
##
##print(s, s[3:6], s[0:2] + s[8])







