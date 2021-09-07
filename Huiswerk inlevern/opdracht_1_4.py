'''API van de KNMI Door Daan Sijnja 20177747'''
import requests
from requests.models import REDIRECT_STATI, Response


'''Dit had ook makkelijker gekunt met de datatime libary'''
def jaar():
    '''Vraag om het jaartal'''
    var = int(input('Voer het jaar in YYYY:'))
    if(var < 1970 or var > 2021):
        #Er mag een jaartal tussen 1970 en 2021 ingevoerd worden
        print('Ongeldig jaar. Voer een getal tussen 1970 en 2021 in')
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

def datum_to_sting(datum):
    '''convert de datum array naar een string'''
    #jaartal naar string
    datum_string = str(datum[0])

    if(datum[1] < 10):
        #check of het getal kleiner is dan tien want dan moet er een nul voor
        datum_string += '0' + str(datum[1])
    else:
        datum_string += str(datum[1])

    if(datum[2] < 10):
        #check of het getal kleiner is dan tien want dan moet er een nul voor
        datum_string += '0' + str(datum[2])
    else:
        datum_string += str(datum[2])

    return datum_string

#start datum array: Jaar : Maand : Dag
start_datum = [0,0,0]

#eind datum array: Jaar : Maand : Dag
end_datum = [0,0,0]

print('Voer de start datum in:')
#input start datum
start_datum[0] = jaar()
start_datum[1] = maand()
start_datum[2] = dag(start_datum[1])

print('Voer de eind datum in:')
#input eind datum
end_datum[0] = jaar()

while(end_datum[0] < start_datum[0]):
    #eind jaar mag niet kleiner zijn dan de start jaar
    print('Eind jaar mag niet kleiner zijn dan het start jaar')
    end_datum[0] = jaar()

end_datum[1] = maand()

if(end_datum[0] == start_datum[0]):
    #check of het eind jaar het zelfde is al het start jaar
    while(end_datum[1] < start_datum[1]):
        #eind maand mag niet kleiner zijn dan de start maand
        print('eind maand mag niet kleiner zijn dan de start maand')
        end_datum[1] = maand()

end_datum[2] = dag(end_datum[1])

if(end_datum[0] == start_datum[0] and end_datum[1] == end_datum[1]):
    #check of het eind jaar het zelfde is al het start jaar en of de eind maand het zelfde is als de start maand
    while(end_datum[2] < start_datum[2]):
        #eind dag mag niet kleiner zijn als de start dag
        print('eind dag mag niet kleiner zijn dan de start dag')
        end_datum[2] = dag(end_datum[1])

#print de datum nogmaals
print('Start datum:',start_datum[0], start_datum[1], start_datum[2])
print('Eind datum:',end_datum[0], end_datum[1], end_datum[2])

#convert de datums naar strings
start_string = datum_to_sting(start_datum)
end_string = datum_to_sting(end_datum)

#bool om te bewaren of er iets mis is gegaan
hasFailed = False

#try om er voor te zorgen dat er het programma niet vastloopt op een fout
try:
    #request naar de API om de Tempratuur te sturen van de gegeven data
    res = requests.get('https://www.daggegevens.knmi.nl/klimatologie/uurgegevens',params={"start":start_string,"end":end_string,"stns":"344","vars":"T","fmt":"json"},timeout=0.0001)
except requests.Timeout:
    #Timeout error
    print('Kon niet verbinden met de KMNI server, Probeer het later nog een keer. ERROR: TIMEOUT')
    hasFailed = True

except requests.ConnectionError:
    #Connection Error
    print('Kon niet verbinden met de KMNI server, Probeer het later nog een keer. ERROR: CONNECTION')
    hasFailed = True
except requests.HTTPError:
    #HTTPError
    print('Kon niet verbinden met de KMNI server, Probeer het later nog een keer. ERROR: HTTP')
    hasFailed = True

except requests.TooManyRedirects:
    #TMR error
    print('Kon niet verbinden met de KMNI server, Probeer het later nog een keer. ERROR: TOOMANYREDIRECTS')
    hasFailed = True

#check of er niks gevaalt is
if(hasFailed == False):
    if(res.ok):
        print('Request Status: OK')
    else:
        print('Request Status: Failed')


    data = res.json()

    i = 0
    #sum_temp is alle tempraturen bij elkaar opgetelt
    sum_temp = 0
    gem_temp = 0

    #bereken de som
    for i in range(len(data)):
        sum_temp += data[i]["T"]

    #failsave
    if(i == 0):
        sum_temp += data[0]["T"]

    #bereken het gemiddelde
    gem_temp = sum_temp/(i+1)
    #len(data) moet gedeelt worden door 24 want er wordt elk uur van een dag gestuurt
    print('totaal dagen', len(data)/24)
    #nog delen door tien omdat je een heel getal krijgt
    print('Gemiddelde temperatuur:',round(gem_temp/10,1), 'graden')