import ciklusok

print("Teszteset 1: Páros szám, amelyik 3-al nem osztható. 4")
print("Várt eredmény: 1, BAM, BUMM, BAM")
ciklusok.feladat4(4)
print()
print("Teszteset 1: 6-tal osztható - 2-vel és 3-al is. 6")
print("Várt eredmény: 1, BAM, BUMM, BAM, 5 BUMMBAM")
ciklusok.feladat4(6)
print()
print("Teszteset 1: 3-mal osztható, de 2-vel nem. 9")
print("Várt eredmény: 1, BAM, BUMM, BAM, 5 BUMMBAM, 7 BAM, BUMM")
ciklusok.feladat4(9)
print()
print("Teszteset 1 - se 3-mal, se 2-vel nem osztható. 11")
print("Várt eredmény: 1, BAM, BUMM, BAM, 5 BUMMBAM, 7 BAM, BUMM, BAM 11")
ciklusok.feladat4(11)
print()

print("Teszteset 1 - negatív szám esetén:")
print("Várt eredmény: Hiba!")
ciklusok.feladat4(-7)

print("Teszteset 2: - nulla")
print("Várt eredmény: Hiba!")
ciklusok.feladat4(0)

print("Teszteset 3: tört szám")
print("Várt eredmény: Hiba!")
ciklusok.feladat4(6.4)


