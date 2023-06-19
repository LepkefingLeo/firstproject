class Novenyek:
    def __init__(self, nev, resz, kezdes, befejezes):
        self.nev = nev
        self.resz = resz
        self.kezdes = kezdes
        self.befejezes = befejezes

    def __str__(self):
       return f"{self.nev}, {self.resz}, {self.kezdes}, {self.befejezes}"

gyogynovenyek = []

def beolvasas():
    f = open("gyogynovenyek.txt", encoding="UTF-8")
    for sor in f:
        reszek = sor.strip().split(';')
        obj = Novenyek(reszek[0], reszek[1], int(reszek[2]), int(reszek[3]))
        gyogynovenyek.append(obj)

def gyongyvirag():
    for x in gyogynovenyek:
        if x.nev == "Gyongyvirag":
            print(f"\t A gyöngyvirágnak a {x.resz} részét gyűjtik")

def level():
    leveles = 0
    for y in gyogynovenyek:
        if y.resz == "level":
            leveles += 1
    print(f"{leveles} db növényt gyűjtenek a leveléért")

def reszek():
    for z in gyogynovenyek:
        print(f"{z.nev} - {z.resz}")

def ossz():
    for i in gyogynovenyek:
        if i.kezdes == 9 or i.kezdes == 10 or i.kezdes == 11:
            print(f"{i.nev}")

def reszek_kapcsolattal():
    virag = 0
    for q in gyogynovenyek:
        if "virag" in q.resz:
            virag += 1
            print(f"{q.nev} db növényt gyűjtenek virággal kapocsolatos részéért")



def main():
    beolvasas()
    gyongyvirag()
    level()
    reszek()
    ossz()
    reszek_kapcsolattal()

main()