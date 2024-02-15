def bekeres():
    olimpikonok = []
    olimpikon = {}
    forras = open("helsinki_olimpia10D/helsinki.txt", "r")
    for sor in forras:
        sor = sor.strip().split()
        sor[0] = int(sor[0])
        sor[1] = int(sor[1])
        olimpikon = {
            "helyezes": sor[0],
            "sportolokszama": sor[1],
            "sportag": sor[2],
            "versenyszam": sor[3]
        }
        olimpikonok.append(olimpikon)
        olimpikon = {}
    return olimpikonok

def getPontSzerzo(tomb):
    pont = 0
    for i in range(len(tomb)):
        if tomb[i]["helyezes"] <= 6:
            pont+=1
    print(f"Pontszerző helyezések száma: {pont}")

def getErmek(tomb):
    arany = 0
    ezust = 0
    bronz = 0
    ossz = 0
    for i in range(len(tomb)):
        if tomb[i]["helyezes"] == 1:
            arany+=1
        if tomb[i]["helyezes"] == 2:
            ezust+=1
        if tomb[i]["helyezes"] == 3:
            bronz+=1
    ossz = arany + ezust + bronz
    print(f"Arany: {arany}")
    print(f"Ezüst: {ezust}")
    print(f"Bronz: {bronz}")
    print(f"Összesen: {ossz}")

def getPontok(tomb):
    pontok = 0
    for i in range(len(tomb)):
        if tomb[i]["helyezes"] == 1:
            pontok+=7
        if tomb[i]["helyezes"] == 2:
            pontok+=5
        if tomb[i]["helyezes"] == 3:
            pontok+=4
        if tomb[i]["helyezes"] == 4:
            pontok+=3
        if tomb[i]["helyezes"] == 5:
            pontok+=2
        if tomb[i]["helyezes"] == 6:
            pontok+=1
    print(f"Olimpiai pontok száma: {pontok}")

def getEredmeny(tomb):
    torna = 0
    uszas = 0
    for i in range(len(tomb)):
        if tomb[i]["helyezes"] == 1 and tomb[i]["sportag"] == "torna" or tomb[i]["helyezes"] == 2 and tomb[i]["sportag"] == "torna" or tomb[i]["helyezes"] == 3 and tomb[i]["sportag"] == "torna":
            torna+=1
        if tomb[i]["helyezes"] == 1 and tomb[i]["sportag"] == "uszas" or tomb[i]["helyezes"] == 2 and tomb[i]["sportag"] == "uszas" or tomb[i]["helyezes"] == 3 and tomb[i]["sportag"] == "uszas":
            uszas+=1
    if uszas > torna:
        print("Úszás sportágban szereztek több érmet")
    elif torna > uszas:
        print("Torna sportágban szereztek több érmet")
    else:
        print("Egyenlő volt az érmek száma")

def getMaxSportolo(tomb):
    maxsportolo = tomb[0]["sportolokszama"]
    for i in range(len(tomb)):
        if maxsportolo < tomb[i]["sportolokszama"]:
            maxsportolo = tomb[i]["sportolokszama"]
    return maxsportolo

def getMaxSportoloCsapat(tomb):
    for i in range(len(tomb)):
        helyezes = tomb[i]["helyezes"]
        sportag = tomb[i]["sportag"]
        versenyszam = tomb[i]["versenyszam"]
        sportolokszama = tomb[i]["sportolokszama"]
        if getMaxSportolo(olimpikonok) == tomb[i]["sportolokszama"]:
            print(f"Helyezés: {helyezes}")
            print(f"Sportág: {sportag}")
            print(f"Versenyszám: {versenyszam}")
            print(f"Sportolók száma: {sportolokszama}")

#main
olimpikonok = bekeres()

print("3. feladat")
getPontSzerzo(olimpikonok)

print("4. feladat")
getErmek(olimpikonok)

print("5. feladat")
getPontok(olimpikonok)

print("6. feladat")
getEredmeny(olimpikonok)

print("8. feladat")
getMaxSportoloCsapat(olimpikonok)