washing_thing = input('What do you want to wash? jacket/underwear/shoes: ')
spin=input('Do you want to spin it? y/n: ')
rinse=input('Do you want to rinde it? y/n: ')

if washing_thing == 'jacket':
    time=40
    time+=(9 if spin=='y' else 0)
    time+=(15 if rinse=='y' else 0)

if washing_thing == 'shoes':
    time=20
    time+=(9 if spin=='y' else 0)
    time+=(15 if rinse=='y' else 0)

if washing_thing == 'underwear':
    time=70
    time+=(9 if spin=='y' else 0)
    time+=(15 if rinse=='y' else 0)

print(f'Total washing time: {time} minutes')