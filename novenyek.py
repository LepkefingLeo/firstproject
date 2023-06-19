f = open("novenyek.txt", "r", encoding="utf-8")
novenyek = []

for sor in f:
    novenyek.append(sor.strip())
f.close()

    
def osszes_noveny():
    for noveny in novenyek:
        noveny = noveny.lower()
        print(noveny)

def novenyek_szama():
    print(f"A gyógynövények száma: {len(novenyek)}")


def kereses():
    noveny = input("Kérem adjon meg egy nevet:")
    if noveny not in novenyek:
        print("Nem szerepel a listában")
    else:
        print("Szerepel a listában")

def mgh():
    print("A magánhangzóval kezdődő növények:")
    for noveny in novenyek:
        if noveny[0] in "AÁEÉIÍOÓÖŐUÚÜŰ":
            print(f"\t{noveny}")

def abc_szerint():
    print("A rendezett lista:")
    abc_szerint = sorted(novenyek)
    print(f"\t{abc_szerint}")


def main():
    osszes_noveny()
    novenyek_szama()
    kereses()
    mgh()
    abc_szerint()

main()

