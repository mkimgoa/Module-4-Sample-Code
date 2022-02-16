f = open("sampledata.txt","r")


aList = []
bList = []
for line in f:
    line = line.strip()
    letter, number = line.split(",")
    number = int(number)
    if letter == "a":
        aList.append(number)
    elif letter == "b":
        bList.append(number)

print(aList)
print(bList)
