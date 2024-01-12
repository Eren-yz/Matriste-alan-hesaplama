import random

def matris_olustur():
    m1 = [[0 for a in range(3)] for b in range(3)]
    for x in range(3):
        for y in range(3):
            m1[x][y] = random.randint(0, 1)

    print(m1)
    return m1

def matris_alan(matris):
    alan = 0
    for satir in matris:
        for eleman in satir:
            if eleman == 1:
                alan += 1
    return alan


olusturulan_matris = matris_olustur()
print(matris_alan(olusturulan_matris))