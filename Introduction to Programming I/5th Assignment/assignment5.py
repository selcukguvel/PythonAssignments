import glob, os
from operator import itemgetter
filee=open("review.txt","w")
fil=open("u.item","r",encoding="ISO-8859-15")
genr=open("u.genre","r")
dat=open("u.data","r")
occp=open("u.occupation","r")
usr=open("u.user","r")
stp=open("stopwords.txt",encoding="utf-8")
flmgenr=open("filmGenre.txt","w")
textt = fil.readlines()
itemnamelisat=[element.strip("\n").split("(") for element in textt]
filmnamelist=[ell[0].rstrip().split("|")[1] for ell in itemnamelisat]
idlist=[ell[0].rstrip().split("|")[0] for ell in itemnamelisat]
newfilm=[mm.upper() for mm in filmnamelist]
itemnamelist=[elementtt.strip("\n").split("|") for elementtt in textt]
urll=[elpp[3] for elpp in itemnamelist]
genrelist=[elpp[4:] for elpp in itemnamelist]
list3=[]
filetxtdict={}
frstlc=os.getcwd()
def fileloop():
    os.chdir("film")
    for file in glob.glob("*.txt"):
        with open(file) as f:
            text = f.read()
            string=""
            a=text.split("(")
            string=string+a[0]
            k=string.rstrip()
            list3.append(k)
            filetxtdict[list3[-1]]=file
    os.chdir(frstlc)
fileloop()
same=[]
def searching(fli,sli):
    for indeg,elment in enumerate(fli):
        try:
            if elment.upper() in sli:
                filee.write(str(idlist[indeg])+" "+str(elment)+" is found in folder."+"\n")
                same.append(elment)
            raise Exception
        except Exception:
            if elment.upper() not in sli:
                filee.write(str(idlist[indeg])+" "+str(elment)+" is not found in folder."+" Look at "+str(urll[indeg])+"\n")
    filee.close()
searching(filmnamelist,list3)
readdict={}
def readtxt():
    os.chdir("film")
    for eq in same:
        r=eq.upper()
        txtname=filetxtdict[r]
        file=open(txtname)
        a=file.read()
        kk=0
        for i in a:
            if i=="\n":
                readdict[r]=a[kk+1:]
                break
            kk+=1
    os.chdir(frstlc)
readtxt()
genrdict={(el.rstrip().split("|"))[1]:(el.rstrip().split("|"))[0] for el in genr}
occpdict={(elo.rstrip().split("|"))[0]:(elo.rstrip().split("|"))[1] for elo in occp}
usrlist=[ela.rstrip().split("|") for ela in usr]
datlist=[elr.rstrip().split() for elr in dat]
stplist=[elbq.strip() for elbq in stp]
oleystrng=[]
def html():
    if not os.path.exists("filmList"):
        os.makedirs("filmList")
    os.chdir("filmList")
    for elv in same:
        nasa=filmnamelist.index(elv)
        id=idlist[nasa]
        up=elv.upper()
        idd=id
        r=idd+".html"
        f=open(r,"w")
        indsk=filmnamelist.index(elv)
        a=genrelist[indsk]
        string=""
        i=0
        for number in a:
            if number=="1":
                string=string+genrdict[str(i)]+" "
            i+=1
        userid=[takao[0] for takao in datlist if takao[1]==idd]
        userrate=[int(takao[2]) for takao in datlist if takao[1]==idd]
        message="""<html>
        <head><title>{}</title></head>
        <body>"""
        message3="""<h1 style="color:red" size="6" font-family:"Times New Roman">{}</h1>"""
        message5="""<p><b>Genre: {}<b/><br> """
        message6="""<b>IMDB Link:<a href={}> {}</a></b><br>"""
        message4="""Review:<br>
        {}</p>
        """
        totaluserrate="""<p><b>Total User:{}/Total Rate:{}</b></p>"""
        head="""<p><b>User who rate the film:</b><br>"""
        k0=message.format(elv)
        m3=message3.format(elv)
        lu5=message5.format(string)
        lu6=message6.format(urll[indsk],elv)
        l4=message4.format(readdict[up])
        trate=totaluserrate.format(len(userid),sum(userrate)/len(userrate))
        f.write(k0)
        f.write(m3)
        f.write(lu5)
        f.write(lu6)
        f.write(l4)
        f.write(trate)
        f.write(head)
        for i in range(len(userid)):
            go="""<b>User:{} Rate:{}</b><br>"""
            go2="""<b>User Detail: Age:{} Gender: {} Occupation: {} Zip Code: {}</b><br>"""
            g1=go.format(userid[i],userrate[i])
            for fsa in usrlist:
                if fsa[0]==userid[i]:
                    g2=go2.format(fsa[1],fsa[2],occpdict[fsa[3]],fsa[4])
            f.write(g1)
            f.write(g2)
        last="""</p></body></html>"""
        f.write(last)
        f.close()
    os.chdir(frstlc)
    os.chdir("film")
    for bb in list3:
        indsk=newfilm.index(bb)
        a=genrelist[indsk]
        string=""
        i=0
        for number in a:
            if number=="1":
                string=string+genrdict[str(i)]+" "
            i+=1
        oleystrng.append(string)
    os.chdir(frstlc)
html()
ttal=[]
def findreview():
    os.chdir("film")
    k=0
    for file in glob.glob("*.txt"):
            backs=[]
            with open(file) as f:
                text = f.read()
                kk=0
                for i in text:
                    if i=="\n":
                        backs.append(int(kk))
                    kk+=1
                spll=text[backs[0]+1:].split(' ')
                ttal.append([oleystrng[k],spll])
                k+=1
    os.chdir(frstlc)
findreview()
ttalgenr=[[el,takao[1]] for takao in ttal for el in takao[0].split()]
new=[]
for rei in ttalgenr:
    totel=[]
    for al in rei[1]:
        if al.lower() not in stplist:
            totel.append(al.lower())
    new.append([rei[0],totel])
newlist=sorted(new,key=itemgetter(0))
sumlist=[el[0] for el in newlist]
lst=[]
dnmq=[]
ff=0
for elmai in newlist:
    rr=elmai[0]
    if rr not in dnmq:
        dnmq.append(rr)
        cnn=sumlist.count(rr)
        listb=[]
        for i in newlist[ff:cnn+ff]:
            listb.append(i[1])
        lst.append([rr,listb])
        ff=cnn+ff
nevo=[]
for a in lst:
    sl=[]
    c=a[0]
    k=a[1]
    for a in k:
        for b in a:
            sl.append(b)
    nevo.append([c,sl])
final=[[a[0],list(set(a[1]))] for a in nevo]
donk=[]
list6=[]
def stage2():
    os.chdir("filmGuess")
    k=0
    for file in glob.glob("*.txt"):
        backs=[]
        with open(file,encoding="ISO-8859-15") as f:
            text = f.read()
            string=""
            a=text.split("(")
            string=string+a[0]
            qe=string.rstrip()
            list6.append(qe)
            kk=0
            for i in text:
                if i=="\n":
                    backs.append(int(kk))
                kk+=1
            spll=text[backs[0]+1:].split(' ')
            donk.append([list6[-1],spll])
            k+=1
    os.chdir(frstlc)
stage2()
quo=[]
for rei in donk:
    totel=[]
    for al in rei[1]:
        if al.lower() not in stplist:
            totel.append(al.lower())
    quo.append([rei[0],totel])
donaee=[[a[0],list(set(a[1]))] for a in quo]
newfinal=[]
for mmq in final:
    br=mmq[0]
    brr=mmq[1]
    au=[]
    for t in brr:
        au.append(t.split("\n"))
    newfinal.append([br,au])
dnq=[]
for xa in newfinal:
    m=xa[0]
    m1=xa[1]
    rrs=[]
    for rb in m1:
        for t in rb:
            if t.lower() not in stplist and len(t)>0:
                rrs.append(t)
    abk=list(set(rrs))
    dnq.append([m,abk])
btr=[]
for el in donaee:
    br=el[1]
    dh=[]
    for vv in br:
        dh.append(vv.split("\n"))
    btr.append([el[0],dh])
all=[]
for cc in btr:
    m=cc[0]
    m1=cc[1]
    rr=[]
    for r in m1:
        for t in r:
            if t.lower() not in stplist and len(t)>0:
                rr.append(t)
    kk=list(set(rr))
    all.append([m,kk])
flmgenr.write("Guess Genres of Movie based on Movies"+str("\n"))
for item in all:
    fr=item[0]
    rr=set(item[1])
    flmgenr.write(str(fr))
    flmgenr.write(str(" : "))
    for itemm in dnq:
        k=itemm[0]
        b=set(itemm[1])
        d=list(b&rr)
        if len(d)>=20:
            flmgenr.write(str(k))
            flmgenr.write(" ")
    flmgenr.write("\n")
flmgenr.close()
fil.close()
genr.close()
dat.close()
occp.close()
usr.close()
stp.close()
