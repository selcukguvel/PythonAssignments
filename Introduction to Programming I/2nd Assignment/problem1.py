import sys
filename=open(sys.argv[1],"r")
ListIntegers=[]
for number in filename.readlines():
    new=number.split(";")
    for number2 in new:
        ListIntegers.append(int(number2))
c=[]
b=[]
def avgFirstThreeDigit(x):
    for a in x:
        new = str(a)
        total=0
        for m in range(0,3):
            total+=int(new[m])
        ave=(total/3)
        c.append(ave)
    count=0
    for i in range(0,len(c)):
        b.append(c[len(c)-1-count])
        count += 1
    return b

output=avgFirstThreeDigit(ListIntegers)
print(output)

filename.close()

