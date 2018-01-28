#------------------------------------------------------------#
# Student Name:Muhammet Selçuk Güvel
# Student ID:21527079
# BBM103 Introduction to Programming Laboratory I, Fall 2016 
# Assignment 3: Mission: Save the Earth
#------------------------------------------------------------#
import sys

filename=open(sys.argv[1],"r")
filename1=open(sys.argv[2],"r")
filename2=open("binarian_message.txt","w")
filename3=open("message.txt","w")
filename4=open(sys.argv[3],"r")
filename5=open("computations.txt","w")

dict={}
def read_dictionary():
    for a in filename.readlines():
        c=a.strip()
        b=c.split(" ")
        key=b[0]
        value=b[1]
        dict[key]=value

listt=[]
def binarian_to_english():
    for a in list3:
        bb=0
        for b in a:
            bb=bb+1
            if b in dict.keys() and bb<len(a):
                print(dict[b], end=" ")
                filename2.write(dict[b])
                filename2.write(" ")
            else:
                if bb<len(a):
                    print(b, end=" ")
                    filename2.write(b)
                    filename2.write(" ")
        if b in dict.keys():
            print((dict[b]).rstrip())
            filename2.write(str(dict[b]).rstrip())
        else:
            print(b.rstrip())
            filename2.write(str(b).rstrip())
        filename2.write("\n")

def english_to_binarian():
    for a1 in list0:
        rr=0
        for b1 in a1:
            rr=rr+1
            a=''.join([c for c in b1 if c not in ('!', '?',".",",","'",":",";")])
            kv1=a.lower()
            if kv1 in dict2.keys():
                if rr<len(a1):
                    print(dict2[kv1], end=" ")
                    filename3.write(str(dict2[kv1]))
                    filename3.write(" ")
            elif kv1.isdigit() and rr<len(a1):
                print(str(decimal_to_binary(int(kv1))), end=" ")
                filename3.write(str(decimal_to_binary(int(kv1))))
                filename3.write(" ")
            elif rr<len(a1):
                print(a, end=" ")
                filename3.write(str(a))
                filename3.write(" ")
        if kv1 in dict2.keys():
            print((dict2[kv1]).rstrip())
            filename3.write(str(dict2[kv1]).rstrip())
        elif kv1.isdigit():
            print(str(decimal_to_binary(int(kv1))))
            filename3.write(str(decimal_to_binary(int(kv1))))
        else:
            print(a.rstrip())
            filename3.write(str(a).rstrip())
        filename3.write("\n")

def binary_to_decimal(x):
    m=0
    for a in range(len(x)):
        m+=float(x[-a-1])*(2**float(a))
    return m



def ly_to_km(distance):
    lightyear=9.4607e+12
    b=lightyear*distance
    return "%e"%b


def decimal_to_binary(number):
    return "{0:b}".format(number)

qq=filename1.readlines()
list1=[]
for strings in qq:
    a=strings.strip()
    element=a.split(" ")
    for i in range(len(element)):
        element[i]=str(element[i])
    list1.append(element)

calculations=[]
list3=[]
for listelement in list1:
        k=listelement[0]
        l=k[0]
        if l[0]=="#" or l[0]=="+":
            calculations.append(listelement)
        else:
            list3.append(listelement)

qq1=filename4.readlines()
list9=[]
for strings1 in qq1:
    a1=strings1.strip()
    element1=a1.split(" ")
    for ii in range(len(element1)):
        element1[ii]=str(element1[ii])
    list9.append(element1)

list0=[]
for tt in list9:
    list0.append(tt)

read_dictionary()
dict2={}
for ky in dict.keys():
    a=dict[ky]
    dict2[a]=ky

tempp=dict2["temperature"]
orb=dict2["orbital-speed"]
dist=dict2["distance"]

for aa in calculations:
    for i in range(len(aa)):
        if aa[0]=="+" and aa[i]==dist:
                v=int(aa[i+1])
                m=str(v)
                if m.isdigit():
                    kilo=ly_to_km(binary_to_decimal(m))
        elif aa[0]=="+" and aa[i]==tempp:
                v1=int(aa[i+1])
                m1=str(v1)
                if m1.isdigit():
                    temp=binary_to_decimal(m1)
        elif aa[0]=="+" and aa[i]==orb:
                v2=int(aa[i+1])
                m2=str(v2)
                if m2.isdigit():
                    orbital=binary_to_decimal(m2)


binarian_to_english()


print("Data about Binarian planet:")
out1="Distance from the Earth: {} km"
print(out1.format(kilo))
print(out1.format(kilo),file=filename5)
out1="Planet temperature: {} degrees Celsius"
print(out1.format(temp))
print(out1.format(temp),file=filename5)
out1="Orbital speed: {} km/s"
print(out1.format(orbital))
print(out1.format(orbital),file=filename5)



english_to_binarian()

filename.close()
filename1.close()
filename2.close()
filename3.close()
filename4.close()
filename5.close()
