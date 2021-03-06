# 193. How to Slice Lists & Tuples in Python

piano_keys = ["a", "b", "c", "d", "e", "f", "g", "h"]
# piano_keys = ("a", "b", "c", "d", "e", "f", "g", "h")

# slice all the way down to last one
print(piano_keys[3:]) 
#['d', 'e', 'f', 'g', 'h']

# get rid of the last one
print(piano_keys[3:-1])
# ['d', 'e', 'f', 'g']

# this will REVERSE the list
print(piano_keys[::-1])
# ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

# print(piano_keys[2:5:2])
# ['c', 'e']

# print(piano_keys[::2])
# ['a', 'c', 'e', 'g']

