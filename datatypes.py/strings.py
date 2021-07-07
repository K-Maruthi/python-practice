str = "Maruthi learing python"
#indexing in strings
print(str[1])
#looping through stings
for x in "banana":
    print(x)
#string length
print(len(str))
# check sting (in,not in)
print("death" in str)
print("python" not in str)
if "death" in str :
    print("present")
else:
    print("absent")
#slicing in strings (spaces also takes index)
print(str[:3])
print(str[3:]) 
print(str[1:3])
print(str[3:14])
print(str[:-1])
# modify strings
print(str.upper()) # upper case 
print(str.lower()) #lower case
print(str.strip()) #removes white spaces
print(str.replace("m","M")) # replaces a sting item
print(str.split(":")) # splits the string into sub strings 
# sting concatanation
a = " naruto"
b = " hinata"
print(a+" loves "+b)
