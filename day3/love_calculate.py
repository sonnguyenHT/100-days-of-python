print("Welcome to Love Calculator")

name1= input("What is your name?\n")
name2= input("What is their name?\n")

combine = name1 + name2

t = combine.lower().count("t")
r = combine.lower().count("r")
u = combine.lower().count("u")
e = combine.lower().count("e")
print("Apperance of T is"+str(t))
print("Apperance of R is"+str(r))
print("Apperance of U is"+str(u))
print("Apperance of E is"+str(e))
l = combine.lower().count("l")
o = combine.lower().count("o")
v = combine.lower().count("v")

print("Apperance of L is"+str(l))
print("Apperance of O is"+str(o))
print("Apperance of V is"+str(v))
print("Apperance of E is"+str(e))

var1 = t + r + u + e 
var2 = l + o + v + e

percen = int(str(var1)+ str(var2))
print(percen)

if percen < 10 or percen > 90:
    print("Your love is like coke and mentos")
elif percen >=40 and percen <=50:
    print("You are together")
else:
    print("Your point is "+str(percen))