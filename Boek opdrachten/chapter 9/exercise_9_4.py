'''Opdracht 9.4 Door Daan Sijnja 20177747'''
import os.path       #nodig want anders doet hij de locatie apart
filename = 'text.txt'
foldername = 'Boek opdrachten/chapter 9' 
file = os.path.join(foldername,filename)

fin = open(file,'rt')
#niet de goede naamgeving maar kon niks anders bedenken
def uses_only(woord,string):
    for i in range(len(woord)):
        if(woord[i] not in string):
            return False
        else:
            return True   
    
    
for_string = input('geef de letters op: ')

for line in fin:
    woord = line.strip()
    if(uses_only(woord,for_string)):
        print(woord)