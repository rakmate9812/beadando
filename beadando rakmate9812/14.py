import sys

for arg in sys.argv:
  print("argumentum: ",arg)
haromszog_szamok=0
n=int(arg)
ls=[]
for i in range(1,n+1):
  haromszog_szamok=haromszog_szamok+i
  ls.append(haromszog_szamok)
out=[]
for j in ls:
  if j%2!=0 and j<n:
    out.append(j)
print(out)
fajl_txt=open("paratlan_haromszog_szamok.txt", "w")
for k in out:
  print(k,file=fajl_txt)
fajl_txt.close()




