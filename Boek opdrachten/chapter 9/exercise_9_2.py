'''Opdracht 9.2 Door Daan Sijnja 20177747'''
import os.path       #nodig want anders doet hij de locatie apart
filename = 'text.txt'
foldername = 'Boek opdrachten/chapter 9' 
file = os.path.join(foldername,filename)

fin = open(file,'rt')
aantal_woorden = 0
aantal_zonder_e = 0
for line in fin:
    aantal_woorden += 1
    woord = line.strip()
    j = 0
    for i in range(len(woord)):
        if(woord[i] == 'e'):
            j = 1
            break

    if(j != 1):
        print(woord)
        aantal_zonder_e += 1

procent_e = (aantal_zonder_e/aantal_woorden)*100

print('Procent onder E', procent_e,'%')
    
    
