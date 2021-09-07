'''Opdracht 9.3 Door Daan Sijnja 20177747'''
import os.path       #nodig want anders doet hij de locatie apart
filename = 'text.txt'
foldername = 'Boek opdrachten/chapter 9' 
file = os.path.join(foldername,filename)

fin = open(file,'rt')
#niet de goede naamgeving maar kon niks anders bedenken
def avoid(woord,string):
    j = True
    for i in range(len(string)):
        if(string[i] in woord):
            j = False
    return j
        
            

for_string = input('geef de verboden letters op: ')

for line in fin:
    woord = line.strip()
    if(avoid(woord,for_string)):
        print(woord)

    
