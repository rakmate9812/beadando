def tizesse(sz,szr):
    hossz=len(str(sz))
    tsz=0
    for i in range(hossz):
        sz=str(sz)
        tsz+=int(sz[i])*szr**(hossz-1)
        hossz-=1
    return tsz
def vissza(sz,szr):
    findex=sz**0
    hatvanyertek=0
    while sz>=findex:
        findex*=szr
        hatvanyertek+=1
    findex/=szr
    megoldas=""
    for i in range(hatvanyertek):
        helyiertek=0
        while findex<=sz:
            sz-=findex
            helyiertek+=1
        megoldas+=str(helyiertek)
        findex/=szr
    return megoldas
def huszonnegy(sz1,sz2,szr):
    tsz1=tizesse(sz1,szr)
    tsz2=tizesse(sz2,szr)
    re=tsz1+tsz2
    eredmeny=vissza(re,szr)
    return eredmeny
print("eredmeny:",huszonnegy(125,149,2))
