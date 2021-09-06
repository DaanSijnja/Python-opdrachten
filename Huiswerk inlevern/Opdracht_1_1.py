'''Tijdconversie Opdracht 1 A en B'''

def convert_time(u,m,s):
    '''u is in uren. m is in minuten en s is in seconden'''
    totaal_seconden = 0
    totaal_seconden += u*3600
    totaal_seconden += m*60
    totaal_seconden += s
    return totaal_seconden

def invers_convert_time(s):
    '''time is een array met u m en s als elementen'''
    time = [0,0,0] 
    time[0] = int(s/3600)
    time[1] = int((s%3600)/60)
    time[2] = s%60

    return time


'''input is het zelfde als de output'''

print(invers_convert_time(convert_time(6,20,45)))