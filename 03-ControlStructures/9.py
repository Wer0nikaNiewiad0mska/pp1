ilosc_zadan = int(input('Enter the total number of test tasks:'))
dobre_zadania = int(input('Enter the number of correctly completed tasks: '))

if dobre_zadania/ilosc_zadan>=0.5:
    print('Test passed')