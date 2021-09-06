'''API van de KNMI'''
import requests


def jaar():
    '''Vraag om het jaartal'''
    var = int(input('Voer het jaar in YYYY:'))
    if(var < 1998 or var > 2021):
        #Er mag een jaartal tussen 1998 en 2021 ingevoerd worden
        print('Ongeldig jaar. Voer een getal tussen 1998 en 2021 in')
        #stel de vraag nog een keer
        return jaar()
    else:
        return var

def maand():
    '''Vraag om de maand'''
    var = int(input('Voer het maand in MM:'))
    if(var < 1 or var > 12):
        #Er mag een getal tussen 1 en 12 ingevoerd worden
        print('Ongeldige maand. Voer een getal tussen 1 en 12 in')
        #stel de vraag nog een keer
        return maand()
    else:
        return var

def dag(maand):
    '''Vraag om de dag'''
    var = int(input('Voer het dag in DD:'))
    if((maand == 2) and (var < 1 or var > 28)):
        #als de maand februari is mag de dag niet hoger zijn dan 28
        print('Ongeldige dag. Voer een dag tussen 1 en 28 in')
        #stel de vraag nog een keer
        return dag(maand)
    elif(((maand == 4) or (maand == 6) or (maand == 9) or (maand == 11)) and (var < 1 or var > 30)):
        #als de maand april, juni, september of november is mag de dag niet hoger zijn dan 30
        print('Ongeldige dag. Voer een dag tussen 1 en 30 in')
        #stel de vraag nog een keer
        return dag(maand)  
    elif(var < 1 or var > 31):
        #in de rest van de maanden mag de dag niet hoger zijn dan 30
        print('Ongeldige dag. Voer een dag tussen 1 en 31 in')
        #stel de vraag nog een keer
        return dag(maand)    
    else:
        return var

#startdatum array: Jaar : Maand : Dag
start_datum = [0,0,0]
#startdatum array: Jaar : Maand : Dag
end_datum = [0,0,0]


print('Voer de start datum in:')
#input start datum
start_datum[0] = jaar()
start_datum[1] = maand()
start_datum[2] = dag(start_datum[1])

#input eind datum

print('Voer de eind datum in:')
#input start datum
end_datum[0] = jaar()

while(end_datum[0] < start_datum[0]):
    #eind jaar mag niet kleiner zijn dan de start jaar
    print('eind jaar mag niet kleiner zijn dan het start jaar')
    end_datum[0] = jaar()

end_datum[1] = maand()

if(end_datum[0] == start_datum[0]):
    #check of het eind jaar het zelfde is al het start jaar
    while(end_datum[1] < start_datum[1]):
        #eind maand mag niet kleiner zijn dan de start maand
        print('eind maand mag niet kleiner zijn dan de start maand')
        end_datum[1] = maand()

end_datum[2] = dag(start_datum[1])

if(end_datum[0] == start_datum[0] and end_datum[1] == end_datum[1]):
    #check of het eind jaar het zelfde is al het start jaar en of de eind maand het zelfde is als de start maand
    while(end_datum[2] < start_datum[2]):
        #eind dag mag niet kleiner zijn als de start dag
        print('eind dag mag niet kleiner zijn dan de start dag')
        end_datum[2] = dag(start_datum[1])


print(start_datum,end_datum)


'''
res = requests.get('https://www.daggegevens.knmi.nl/klimatologie/uurgegevens',params={"start":start_datum,"end":end_datum,"stns":"344","vars":"T","fmt":"json"})
data = res.json()

i = 0
sum_temp = 0
gem_temp = 0

for i in range(len(data)):
    sum_temp += data[i]["T"]
gem_temp = sum_temp/i


print(gem_temp/10)
'''