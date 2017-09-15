cijferICOR = 5
cijferPROG = 6
cijferCSN = 7

gemiddelde = (cijferCSN + cijferICOR + cijferPROG) / 3
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30
overzicht = 'Mijn cijfers zijn gemiddeld een ' + str(gemiddelde) + ' en leveren een beloning op van: ' + str(beloning)
print(gemiddelde)
print(beloning)
print(overzicht)