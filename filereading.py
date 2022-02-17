f = open("sampledata.txt","r")


aList = []
bList = []
for line in f:
    line = line.strip() # removes whitespace and newline characters at the beginning/end of the line
    letter, number = line.split(",")
    number = int(number)
    if letter == "a":
        aList.append(number)
    elif letter == "b":
        bList.append(number)

print(aList)
print(bList)
