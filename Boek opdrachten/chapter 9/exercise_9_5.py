'''Opdracht 9.5 Door Daan Sijnja 20177747'''
import os.path       #nodig want anders doet hij de locatie apart
filename = 'text.txt'
foldername = 'Boek opdrachten/chapter 9' 
file = os.path.join(foldername,filename)

fin = open(file,'rt')
#niet de goede naamgeving maar kon niks anders bedenken
def uses_all(woord,string):
    if(string in woord):
        return True
    else:
        return False   
    
    
for_string = input('geef de letters op: ')

for line in fin:
    woord = line.strip()
    if(uses_all(woord,for_string)):
        print(woord)