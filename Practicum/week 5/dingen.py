def bereken_cijfer(goede_aantal,totaal_vragen = 45):
    return (goede_aantal/totaal_vragen) * 9 + 1

totaal = 45
for i in range(totaal):
    print(i, bereken_cijfer(i,totaal) )
