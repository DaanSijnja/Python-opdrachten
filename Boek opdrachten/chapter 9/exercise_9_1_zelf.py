'''Door Daan Sijnja 20177747'''
import os.path       #nodig want anders doet hij de locatie apart


filename = 'text.txt'
foldername = 'Boek opdrachten/chapter 9' 
file = os.path.join(foldername,filename)

def geef_lengte_woorden(filelocatie):
    result_array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fin = open(filelocatie,'rt')
    for line in fin:
        woord = line.strip()
        result_array[len(woord)-2] += 1

    return result_array

def print_array(array):
    for i in range(len(array)):
        print('Aantal letters:', i + 2, 'Aantal woorden: ', array[i])



print_array(geef_lengte_woorden(file))









