import random
import time
import math

money = 50000
print(f'Welcome to the egg hatching simulator, you start with {money} dollars!')
pets = []
autodelete_list = []
COMMONEGG_OUTCOMES = ['Sad bunny','Cat', 'Dog', 'Very Happy bunny', 'Fox','Dogcat']
COMMONEGG_WEIGHT = [50,30,10,5,3,2]

UNCOMMONEGG_OUTCOMES = ['Rabbit', 'Wolf','Bloodhound', 'Red Panda', 'Rubicon']
UNCOMMONEGG_WEIGHT = [40,32,16,11.999,0.001]
total_egg_hatched = 0

userhatchspeedlevel = 0
hatchspeedlevel = 1
hatchspeed = 1

COMMONPET_PAYMENT = [3,4,8,16,32,64]
UNCOMMONPET_PAYMENT = [11,12,20,50,100000]

def loops():
        global money
        global total_egg_hatched
        global userhatchspeedlevel
        global hatchspeedlevel
        global hatchspeed
        print('1. Look at eggs!')
        print('2. Shop')
        print('3. Stats')
        print('4. Inventory')
        print('5. Adoption')
        print('6. Add Pet to Auto-Delete')
        print('7. Remove Pet from Auto-Delete')
        gameinput = input('Which of the following would you like to do! ')
        print('')
        if gameinput == '1':
            print('1. Common egg (Cost: 2)')
            print('2. Uncommon egg (Cost: 10)')
            egginput = input('Which egg would you like to hatch? ')
            if egginput == '1':
                amountofeggshatched = int(input(f'How many eggs would you like to hatch? Your Hatch speed is {hatchspeed}, and you have {money} dollars! '))
                total_egg_hatched += amountofeggshatched
                while amountofeggshatched > 0:
                    commonegg()
                    time.sleep(hatchspeed)
                    amountofeggshatched -= 1
            elif egginput == '2':
                amountofeggshatched = int(input(f'How many eggs would you like to hatch? Your Hatch speed is {hatchspeed}, and you have {money} dollars! '))
                total_egg_hatched += amountofeggshatched
                while amountofeggshatched > 0:
                    uncommonegg()
                    time.sleep(hatchspeed)
                    amountofeggshatched -= 1
        elif gameinput == '2':
            if userhatchspeedlevel < 15:
                userhatchspeedlevel += 1
                hatchspeedcost = userhatchspeedlevel ** 2 + userhatchspeedlevel * 3
                localinput = input(f'Would you like to upgrade hatchspeed, Cost is {hatchspeedcost}. (y/n) ')
                if localinput.lower() == 'y':
                    money -= hatchspeedcost
                    hatchspeedlevel += 0.1
                    negtivehatchspeedlevel = hatchspeedlevel * -1
                    hatchspeed = round(math.pow(hatchspeedlevel, negtivehatchspeedlevel),2)
                    print(f'Your Hatch speed level is now {userhatchspeedlevel}')
                    print(f'It now takes {hatchspeed} seconds to hatch.')
                elif localinput.lower() == 'n':
                    print('Thank you for coming to the shop!')
            else:
                print('You can not have a hatch level over 15.')

        elif gameinput == '3':
            print(f'Your current egg count is: {total_egg_hatched}!')
            print(f'Current hatch speed is: {hatchspeed}!')
        elif gameinput == '4':
            print(*pets)
        elif gameinput == '5':
            adopt = input('Which pet would you like to put up for adoption? ')
            if adopt in pets:
                pets.remove(adopt)
                print(pets)
            else:
                print('No puedes dar en adopción una mascota que no tienes')
        elif gameinput == '6':  # Add pet to auto-delete
            autodelete = input('Which pet would you like to put up for auto-delete? ')
            if autodelete in pets:
                autodelete_list.append(autodelete)
                print(f'{autodelete} marked for auto-delete.')
            else:
                print(f'{autodelete} is not in your inventory.')

        elif gameinput == '7':  # Remove pet from auto-delete
            cancel_delete = input('Which pet would you like to remove from auto-delete? ')
            if cancel_delete in autodelete_list:
                autodelete_list.remove(cancel_delete)
                print(f'{cancel_delete} is no longer marked for auto-delete.')
            else:
                print(f'{cancel_delete} was not in auto-delete.')


def commonegg():
    global pets
    global money
    money -= 2
    print("This egg cost 2 Money's")
    print('Hatching common egg')
    hatched_item = random.choices(COMMONEGG_OUTCOMES, weights=COMMONEGG_WEIGHT, k=1)[0]

    print(f"You hatched: {hatched_item}")
    pets.append(hatched_item)  # Use .append() for adding a single item
    print("Your current pets:", ', '.join(pets))  # Print without brackets
    if hatched_item == 'Sad bunny':
        money += COMMONPET_PAYMENT[0]
    elif hatched_item == 'Cat':
        money += COMMONPET_PAYMENT[1]
    elif hatched_item == 'Dog':
        money += COMMONPET_PAYMENT[2]
    elif hatched_item == 'Very Happy bunny':
        money += COMMONPET_PAYMENT[3]
    elif hatched_item == 'Fox':
        money += COMMONPET_PAYMENT[4]
    elif hatched_item == 'Dogcat':
        money += COMMONPET_PAYMENT[5]
    print(f'After pet payments your money is {money}!')
    print('')

def uncommonegg():
    global pets
    global money
    money -= 10
    print("This egg cost 10 Money's")
    print('Hatching uncommon egg')
    hatched_item = random.choices(UNCOMMONEGG_OUTCOMES, weights=UNCOMMONEGG_WEIGHT, k=1)[0]

    print(f"You hatched: {hatched_item}")
    pets.append(hatched_item)  # Use .append() for adding a single item
    print("Your current pets:", ', '.join(pets))  # Print without brackets
    if hatched_item == 'Rabbit':
        money += UNCOMMONPET_PAYMENT[0]
    elif hatched_item == 'Wolf':
        money += UNCOMMONPET_PAYMENT[1]
    elif hatched_item == 'Bloodhound':
        money += UNCOMMONPET_PAYMENT[2]
    elif hatched_item == 'Red Panda':
        money += UNCOMMONPET_PAYMENT[3]
    elif hatched_item == 'Rubicon':
        money += UNCOMMONPET_PAYMENT[4]
    print(f'After pet pet payments your money is {money}!')
    print('')
while money >= 0:
    while any(pet in pets for pet in autodelete_list):  # Keep running until all auto-delete pets are gone
        for pet in autodelete_list[:]:
            if pet in pets:
                pets.remove(pet)
                print(f'{pet} was automatically removed.')
    time.sleep(0.3)
    loops()