
getal = input("Voer een getal of een romijns getal in: ")
output = ""

rletters = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

print(len(getal))

for item, index in enumerate(getal,1):
    print(item, index)
    