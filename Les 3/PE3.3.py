leeftijd = eval(input('Geef je leeftijd: '))
paspoort = input('Heeft u een Nederlands paspoort? ')
if leeftijd > 18 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen.')
else:
    print('Je mag niet stemmen.')

