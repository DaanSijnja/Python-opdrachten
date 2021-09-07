'''Opdracht 9.1 Door Daan Sijnja 20177747'''
import os.path       #nodig want anders doet hij de locatie apart
filename = 'text.txt'
foldername = 'Boek opdrachten/chapter 9' 
file = os.path.join(foldername,filename)

fin = open(file,'rt')
i = 0
for line in fin:
    woord = line.strip()
    '''check voor woorden langer dan 20 tekents'''
    if(len(woord) > 20):
        i += 1
        print(woord)

print('Totaal woorden',i)