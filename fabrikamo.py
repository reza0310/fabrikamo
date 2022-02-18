import random as r
nbre_lettre = r.randint(2, 10)  # Nombre de lettres
res = ""
voyelles = 0
cons = 0
while voyelles <= (nbre_lettre//2):  # Condition pour faire un mot lisible: une lettre sur deux doit être voyelle.
    liste = []
    voyelles = 0
    for i in range(0, nbre_lettre):
        if cons == 3:
            i = 0
            liste = []
            voyelles = 0
            cons = 0
        a = r.randint(1, 26)
        if a == 1:
            liste.append("a")
            voyelles += 1
            cons = 0
        elif a == 2:
            liste.append("b")
            cons += 1
        elif a == 3:
            liste.append("c")
            cons += 1
        elif a == 4:
            liste.append("d")
            cons += 1
        elif a == 5:
            liste.append("e")
            voyelles += 1
            cons = 0
        elif a == 6:
            liste.append("f")
            cons += 1
        elif a == 7:
            liste.append("g")
            cons += 1
        elif a == 8:
            liste.append("h")
            cons += 1
        elif a == 9:
            liste.append("i")
            voyelles += 1
            cons = 0
        elif a == 10:
            liste.append("j")
            cons += 1
        elif a == 11:
            liste.append("k")
            cons += 1
        elif a == 12:
            liste.append("l")
            cons += 1
        elif a == 13:
            liste.append("m")
            cons += 1
        elif a == 14:
            liste.append("n")
            cons += 1
        elif a == 15:
            liste.append("o")
            voyelles += 1
            cons = 0
        elif a == 16:
            liste.append("p")
            cons += 1
        elif a == 17:
            liste.append("q")
            cons += 1
        elif a == 18:
            liste.append("r")
            cons += 1
        elif a == 19:
            liste.append("s")
            cons += 1
        elif a == 20:
            liste.append("t")
            cons += 1
        elif a == 21:
            liste.append("u")
            voyelles += 1
            cons = 0
        elif a == 22:
            liste.append("v")
            cons += 1
        elif a == 23:
            liste.append("w")
            cons += 1
        elif a == 24:
            liste.append("x")
            cons += 1
        elif a == 25:
            liste.append("y")
            voyelles += 1
            cons = 0
        elif a == 26:
            liste.append("z")
            cons += 1
        for y in range (0, len(liste)-1):
            if liste[y] == liste[y+1]:
                i = 0
                liste = []
                voyelles = 0
                cons = 0
for i in range(0, len(liste)):
    res = str(res) + str(liste[i])
print(res)
