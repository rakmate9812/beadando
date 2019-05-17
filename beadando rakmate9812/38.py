mozi=[["X" for j in range(40)] for i in range(100)]
def foglalas():
    nev=input("Adja meg a foglaló monogrammját: ")
    hely=input("Adja meg a foglalni kívánt helyet (sor szék): ").split()
    while mozi[int(hely[0])-1][(int(hely[1])-1)*2]!="X":
        hely=input("Ez a szék már le van foglalva! Válasszon másik széket: ").split()
    print("A szék sikeresen lefoglalva a {0}.sor {1}.székére {2} névre.".format(int(hely[0]),int(hely[1]),nev))
    mozi[int(hely[0])-1][(int(hely[1])-1)*2]=nev[0]
    mozi[int(hely[0])-1][(int(hely[1])-1)*2+1]=nev[1]
def kereses():
    nev=input("Adja meg a keresendő monogrammját: ")
    i=0
    while i<100:
        j=0
        while j<40:
            if mozi[i][j]==nev[0] and mozi[i][j+1]==nev[1]:
                print("{0} a(z) {1}.sor {2}.székén foglalt helyet.".format(nev,i+1,j//2+1))
                return 0
            j+=2
        i+=1
    print("Nincs ilyen monogrammú foglalás!")
    return 0
def modositas():
    nev=input("Adja meg a módosítandó foglalás monogrammját: ")
    siker=0
    i=0
    while i<100:
        j=0
        while j<40:
            if mozi[i][j]==nev[0] and mozi[i][j+1]==nev[1]:
                mozi[i][j]= mozi[i][j+1]="X"
                x=i
                y=j
                siker=1
            j+=2
        i+=1

    if siker==1:
        hely=input("Adja meg a foglalni kívánt helyet (sor szék): ").split()
        while mozi[int(hely[0])-1][(int(hely[1])-1)*2]!="X":
            hely=input("Ez a szék már le van foglalva! Kérem válasszon másik széket: ").split()
        mozi[int(hely[0])-1][(int(hely[1])-1)*2]=nev[0]
        mozi[int(hely[0])-1][(int(hely[1])-1)*2+1]=nev[1]
        print("A {0} nevű foglalás áthelyezve a {1}. sor {2}. székéről a {3}. sor {4}.székére"
              .format(nev,x+1,y//2+1,int(hely[0]),int(hely[1])))
        return 0
    else:
        print("Nincs ilyen nevű foglalás!")
        return 0
def torles():
    nev=input("Adja meg a foglaló monogrammját: ")
    i=0
    while i<100:
        j=0
        while j<40:
            if mozi[i][j]==nev[0] and mozi[i][j+1]==nev[1]:
                mozi[i][j]=mozi[i][j+1]="X"
                print("A foglalás sikeresen törölve {0} névről a(z) {1}.sor {2}.székéről!".format(nev,i+1,j//2+1))
                return 0
            j+=2
        i+=1
    print("Nincs ilyen monogrammú foglalás!")
def main():
    utasitas=input("Adjon meg egy utasítást (foglalas/kereses/modositas/torles/helyek): ")
    while utasitas!="END":
        if utasitas=="foglalas":
            foglalas()
        elif utasitas=="kereses":
            kereses()
        elif utasitas=="modositas":
            modositas()
        elif utasitas=="torles":
            torles()
        elif utasitas=="helyek":
            for j in mozi:
                print(j)
        else:
            print("Nincs ilyen utasítás!")
        utasitas=input("Adjon meg egy utasítást: (foglalas/kereses/modositas/torles): ")
if __name__ == "__main__":
    main()