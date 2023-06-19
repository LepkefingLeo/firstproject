noveny = input("Kérem a gyógynövény nevét: ")
napi = int(input("Kérem a napi szükséges mennyiséget grammban: "))
hany_napra = str(round(100/napi))
print(f"A(z) {noveny} összesen {hany_napra} elegendő")
if hany_napra > "29":
    print("Elegendő 30 napra egy dobozzal")
else:
    print("Egy doboz sajnos nem elegendő a 30 napra!")