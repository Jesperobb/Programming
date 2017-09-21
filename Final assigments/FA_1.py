def standaardprijs(afstandKM):
    if afstandKM >= 50:
        return afstandKM * 0.60 + 15
    elif afstandKM <= 0:
        return 0
    else:
        return afstandKM * 0.80

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == 'ja':
        weekendrit = True
    else:
        weekendrit = False
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == True:
            prijs = standaardprijs(afstandKM) * 0.65
        else:
            prijs = standaardprijs(afstandKM) * 0.7
    else:
        if weekendrit == True:
            prijs = standaardprijs(afstandKM) * 0.6
        else:
            prijs = standaardprijs(afstandKM)
    return prijs

test = eval(input('Welke leeftijd wilt u checken? u kunt kiezen uit de leeftijden 11, 12 ,64 en 65: '))
if test == 11:
    print('€' + str(ritprijs(leeftijd=11, weekendrit='ja', afstandKM=10)))
    print(ritprijs(leeftijd=11, weekendrit='ja', afstandKM=60))
    print(ritprijs(leeftijd=11, weekendrit='nee', afstandKM=10))
    print(ritprijs(leeftijd=11, weekendrit='nee', afstandKM=60))
elif test == 12:
    print(ritprijs(leeftijd=12, weekendrit='ja', afstandKM=10))
    print(ritprijs(leeftijd=12, weekendrit='ja', afstandKM=60))
    print(ritprijs(leeftijd=12, weekendrit='nee', afstandKM=10))
    print(ritprijs(leeftijd=12, weekendrit='nee', afstandKM=60))

elif test == 64:
    print(ritprijs(leeftijd=64, weekendrit='ja', afstandKM=10))
    print(ritprijs(leeftijd=64, weekendrit='ja', afstandKM=60))
    print(ritprijs(leeftijd=64, weekendrit='nee', afstandKM=10))
    print(ritprijs(leeftijd=64, weekendrit='nee', afstandKM=60))

elif test == 65:
    print(ritprijs(leeftijd=65, weekendrit='ja', afstandKM=10))
    print(ritprijs(leeftijd=65, weekendrit='ja', afstandKM=60))
    print(ritprijs(leeftijd=65, weekendrit='nee', afstandKM=10))
    print(ritprijs(leeftijd=65, weekendrit='nee', afstandKM=60))
