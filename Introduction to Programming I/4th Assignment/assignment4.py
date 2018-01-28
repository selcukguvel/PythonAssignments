import matplotlib.pyplot as plot
import numpy as np
import csv
from operator import itemgetter
from matplotlib.pyplot import cm
import sys
out=open("retrievedData.txt","w")
outt=open("myAnswer.txt","w")
list1=[]
votelist=[]
candlist=[]
dict={}
def retrieveData(filename,candidatename):
    with open(filename,"r") as csvfile:
        readcsv=csv.reader(csvfile,delimiter=",")
        for satx in readcsv:
            list1.append(satx)
        firstlist=list1[0]
        r=list1[1:]
        splt=candidatename.split(",")
        for cand in splt:
            a=firstlist.index(cand)
            candlist.append(cand)
            sum=0
            for value in r:
                voteindex=value[a]
                votelist.append(int(voteindex))
                sum=sum+int(voteindex)
                dict[cand]=sum
    return out.write(str(votelist))
retrieveData(sys.argv[1],sys.argv[2])
toptwocandidates=[]
listt=[]
vtes=[]
winners=[]
dict2={}
winner1ey=[]
winner2ey=[]
statename=[]
def DispBarPlot():
    for name,vote in dict.items():
        listt.append([name,vote])
    for dgr in listt:
        vtes.append(dgr[1])
        vtes.sort()
    for item in dict.keys():
        dict2[dict[item]]=item
    maxv=vtes[-1]
    maxv2=vtes[-2]
    winners.append(dict2[maxv])
    winners.append(dict2[maxv2])
    frst=list1[0]
    indx1=frst.index(winners[0])
    indx2=frst.index(winners[1])
    for elementt in list1[1:]:
        winner1ey.append(elementt[indx1])
    for elementt2 in list1[1:]:
        winner2ey.append(elementt2[indx2])
    for state in list1[1:]:
        statename.append(state[0])
    intwn1=[int(x) for x in winner1ey]
    intwn2=[int(x) for x in winner2ey]
    aa=np.arange(len(statename))
    width=0.23
    plot.bar(aa+width,intwn2,width,color="r",align='center',label=winners[1])
    plot.bar(aa,intwn1,width,color="b",align='center',label=winners[0])
    plot.xticks(aa+width,statename,rotation=90)
    plot.xlabel("States")
    plot.ylabel("Vote Count")
    plot.legend()
    plot.autoscale()
    plot.tight_layout()
    plot.savefig("ComparativeVotes.pdf")
    plot.close()
DispBarPlot()
chng=[]
byvote=[]
names=[]

def compareVoteonBar():
    total=0
    for elval1 in listt:
        total+=elval1[1]
    for elval in listt:
        c="%.3f"% ((elval[1]/total)*100)
        chng.append([elval[0],float(c)])
    perclist=sorted(chng,key=itemgetter(1))
    for element in perclist:
        names.append(element[0])
        byvote.append(element[1])
    byvote.reverse()
    names.reverse()
    length=len(names)
    aaa=np.arange(length)
    rex = list(map("{} %".format,byvote))
    k=0
    for con in names:
        plot.bar(k,byvote[k],align='center',color=cm.jet(1.*k/length),label=con)
        k+=1
        plot.xticks(aaa,rex)
    plot.xlabel("Nominees")
    plot.ylabel("Vote percentages")
    plot.legend()
    plot.autoscale()
    plot.tight_layout()
    plot.savefig("CompVotePercs.pdf")
    plot.close()
compareVoteonBar()
countt=[]
ocr=[]
freqlist=[]
def obtainHistogram(lst):
    del ocr[:]
    del countt[:]
    occr=0
    for rangx in range(0,10):
        count=0
        for elemntt in lst:
            v=str(elemntt)
            k=str(rangx)
            if len(v)>1 and k==v[-1]:
                count+=1
                occr+=1
            if len(v)>1 and k==v[-2]:
                count+=1
                occr+=1
            if len(v)<2 and v==k:
                count+=1
                occr+=1
            if len(v)<2 and rangx==0:
                count+=1
                occr+=1
        countt.append(count)
    ocr.append(occr)
    for elc in countt:
        freqlist.append(elc/ocr[0])
    return [elc/ocr[0] for elc in countt]

obtainHistogram(votelist)

meanv=[]
def plotHistogram(graph,i):
    del meanv[:]
    colorx=["b","r","c","m","y","orange"]
    mv=sum(graph)/len(graph)
    for tk in range(len(graph)):
        meanv.append(mv)
    av=np.arange(len(graph))
    plot.plot(av,meanv,"--",linewidth=2,color="g",label="Mean")
    plot.plot(av,graph,color=colorx[i],label="Digit Dist.")
    plot.xlabel("Digits")
    plot.ylabel("Distribution")
    if i==0:
        plot.legend(loc=2)
        plot.title("Histogram of least sign. digits - Sample:"+str(i+1))
        plot.savefig("HistogramofSample1.pdf")
        plot.close()
    elif i==1:
        plot.legend(loc=2)
        plot.title("Histogram of least sign. digits - Sample:"+str(i+1))
        plot.savefig("HistogramofSample2.pdf")
        plot.close()
    elif i==2:
        plot.legend(loc=2)
        plot.title("Histogram of least sign. digits - Sample:"+str(i+1))
        plot.savefig("HistogramofSample3.pdf")
        plot.close()
    elif i==3:
        plot.legend(loc=2)
        plot.title("Histogram of least sign. digits - Sample:"+str(i+1))
        plot.savefig("HistogramofSample4.pdf")
        plot.close()
    elif i==4:
        plot.legend(loc=2)
        plot.title("Histogram of least sign. digits - Sample:"+str(i+1))
        plot.savefig("HistogramofSample5.pdf")
        plot.close()
    else:
        plot.legend()
        plot.title("Histogram of least sign. digits")
        plot.savefig("Histogram.pdf")
        plot.close()
plotHistogram(freqlist,5)


k=[]
cc=[]
def plotHistogramWithSample():
    i=0
    for sizee in [10,50,100,1000,10000]:
        del k[:]
        del cc[:]
        k.append(np.random.randint(low=0,high=100,size=sizee))
        for element in k:
            for a in element:
                cc.append(a)
        u=obtainHistogram(cc)
        plotHistogram(u,i)
        i+=1
plotHistogramWithSample()

def calculateMSE(frst,scnd):
    totall=0
    for i in range(len(frst)):
        totall+=((frst[i]-scnd[i])**2)
    return totall

def takeshistogram(input):
    return calculateMSE(input,meanv)

ccx=takeshistogram(obtainHistogram(votelist))

gg=[]
maov=[]
rr=[]
totlfreq=[]
def compareMSEs(valuee):
    for el in range(10000):
        del gg[:]
        del maov[:]
        del rr[:]
        gg.append(np.random.randint(low=0,high=100,size=len(votelist)))
        for cbq in gg:
            for tq in cbq:
                rr.append(tq)
        ft=obtainHistogram(rr)
        mav=sum(ft)/len(ft)
        for t in range(len(ft)):
            maov.append(mav)
        c=calculateMSE(ft,maov)
        totlfreq.append(c)
    print("MSE value of 2012 USA election is",valuee)
    outt.write(str("MSE value of 2012 USA election is "+str(valuee))+"\n")
    largeqlrandom=0
    smalrandom=0
    for randommse in totlfreq:
        if randommse>=valuee:
            largeqlrandom+=1
        else:
            smalrandom+=1
    lentot=len(totlfreq)
    pvalue=smalrandom/lentot
    print("The number of MSE of random samples which are larger than or equal to USA election MSE is",largeqlrandom)
    outt.write(str("The number of MSE of random samples which are larger than or equal to USA election MSE is "+str(largeqlrandom))+"\n")
    print("The number of MSE of random samples which are smaller than USA election MSE is",smalrandom)
    outt.write(str("The number of MSE of random samples which are smaller than USA election MSE is "+str(smalrandom))+"\n")
    print("2012 USA election rejection level p is",pvalue)
    outt.write(str("2012 USA election rejection level p is "+str(pvalue))+"\n")
    newsmal=0
    for rndmse in totlfreq:
        if valuee<rndmse:
            newsmal+=1
    if newsmal>=((lentot*5)/100):
        print("Finding: There is no statistical evidence to reject null hypothesis")
        outt.write(str("Finding: There is no statistical evidence to reject null hypothesis"))
    else:
        print("Finding: We reject the null hypothesis at the p=",pvalue,"level")
        outt.write(str("Finding: We reject the null hypothesis at the p= "+str(pvalue)+" level"))

compareMSEs(ccx)
out.close()
outt.close()
