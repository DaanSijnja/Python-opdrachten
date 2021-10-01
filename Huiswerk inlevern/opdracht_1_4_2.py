import requests

dagen_in_maand = [-1,31,28,31,30,31,30,31,31,30,31,30,31]

def get_datum():
    datum = input('Geef datum op JJJJMMDD:')

    if(len(datum) != 8):
        print('geen geldige datum')
        return get_datum()

    if(int(datum[0:4]) < 1970 or int(datum[0:4]) > 2021):
        print('verkeerd jaar opgegeven')
        return get_datum()

    if(int(datum[4:6]) < 1 or int(datum[4:6]) > 12):
        print('verkeerde maand opgegeven')
        return get_datum()

    if(int(datum[6:8]) < 1 or int(datum[6:8]) > dagen_in_maand[int(datum[4:6])]):
        print('verkeerde maand opgegeven')
        return get_datum()

    return datum

print('Startdatum:')
start_datum = get_datum()

print('Einddatum:')
eind_datum = get_datum()

while(int(start_datum) > int(eind_datum)):
    print('eind datum mag niet kleiner zijn dan de start datum:')
    eind_datum = get_datum()


hasfailed = False

try:
    req = requests.get('https://www.daggegevens.knmi.nl/klimatologie/uurgegevens',params={"start": start_datum ,"end": eind_datum,"stns":"344","vars":"T","fmt":"json"},timeout=20)
except:
    hasfailed = True
    print('kon geen connectie maken')
    
if(hasfailed == False):
    data = req.json()

    som_tempratuur = 0

    for i in range(len(data)):
        som_tempratuur += data[i]['T']

    gem_tempratuur = som_tempratuur/len(data)
    print('gemiddelde tempratuur', round(gem_tempratuur/10,2))




