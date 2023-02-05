row1 = ["👘 ","👘 ","👘 "]
row2 = ["👘 ","👘 ","👘 "]
row3 = ["👘 ","👘 ","👘 "]
map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}\n")

choose = input("choose your destination to put a 'X': ")

print(int(choose[0]))
print(int(choose[1]))
map[int(choose[0])-1][int(choose[1])-1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")