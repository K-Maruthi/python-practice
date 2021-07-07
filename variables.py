# variables are used to assign  values , variables are containers for storing values
x = 7
y = "Hello World"
print(x)
print(y)
#multiple values to multiple variables (no.of variables should be = no.of values)
a,b,c = "orange",22,34.9
print(a)
print(b)
print(c)
# mutliple variables same value
p=q=r=2
print(p)
print(q)
print(r)
#unpack a collection
colours = ["blue","Red","white","black"]
x,y,z,memine= colours
print(x)
print(y)
print(z)
print(memine)
#global variables created outside of a function and can be used globally
x = "awesome"
def myfunc():
    x = "fantastic"
    print("python is " +x)

myfunc()
print("python is " +x)

