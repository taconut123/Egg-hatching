import random
import time
import math

money = 500 #remember to change this
total_egg_hatched = 0
userhatchspeedlevel = 0
hatchspeedlevel = 1
hatchspeed = 1
luck = 1
print(f'Welcome to the egg hatching simulator, you start with {money} dollars!')
pets = []
autodelete_list = []
common_pets = ['Sad bunny','Cat', 'Dog', 'Very Happy bunny', 'Fox','Dogcat']
common_weight = [50,30,10,5,3,2]

UNCOMMONEGG_OUTCOMES = ['Rabbit', 'Wolf','Bloodhound', 'Red Panda', 'Rubicon']
UNCOMMONEGG_WEIGHT = [40,32,16,11.999,0.001]

DIAMONDEGG_OUTCOMES = ['Diamond Dog','Diamond Rabbit','Diamond Bunny','Diamond Wolf','Diamond Hex','Diamond Dogcat','Diamond Prism','Diamond Ring','Apex Diamond']
DIAMONDEGG_WEIGHT = [26,25,25,23.8389,0.1,0.05,0.01,0.001,0.0001]

COMMONPET_PAYMENT = [1,3,6,12,24,64]
UNCOMMONPET_PAYMENT = [9,11,16,36,100000]
DIAMONDEGG_PAYMENT = [53,53,55,56,9000,10000,10000,40000, 50000000 ]
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
        print('8. Quit')
        gameinput = input('Which of the following would you like to do! ')
        print('')
        if gameinput == '1':
            print('1. Common egg (Cost: 2)')
            print('2. Uncommon egg (Cost: 10)')
            print('3. Diamond egg (Cost: 100)')
            egginput = input('Which egg would you like to hatch? ')
            if egginput == '1' and money >= 2 :
                amountofeggshatched = int(input(f'How many eggs would you like to hatch? Your Hatch speed is {hatchspeed}, and you have {money} dollars! '))
                total_egg_hatched += amountofeggshatched
                while amountofeggshatched > 0:
                    commonegg()
                    time.sleep(hatchspeed)
                    amountofeggshatched -= 1
            else:
                print('You did not have enough money to hatch!')
            if egginput == '2':
                amountofeggshatched = int(input(f'How many eggs would you like to hatch? Your Hatch speed is {hatchspeed}, and you have {money} dollars! '))
                total_egg_hatched += amountofeggshatched
                while amountofeggshatched > 0:
                    uncommonegg()
                    time.sleep(hatchspeed)
                    amountofeggshatched -= 1
            if egginput == '3' and money >= 100:
                amountofegghatched = int(input(f'How many eggs would you like to hatch? Your Hatch speed is {hatchspeed}, and you have {money} dollars! '))
                total_egg_hatched += amountofegghatched
                while amountofegghatched > 0:
                    diamondegg()
                    time.sleep(hatchspeed)
                    amountofegghatched -= 1

        elif gameinput == '2':
            if userhatchspeedlevel < 35:
                nextlevel =  userhatchspeedlevel + 1
                hatchspeedcost = nextlevel ** 2 + nextlevel * 3
                localinput = input(f'Would you like to upgrade hatchspeed, Your current level is {userhatchspeedlevel}, Cost is {hatchspeedcost}. (y/n) ')
                if localinput.lower() == 'y' and money > hatchspeedcost:
                    userhatchspeedlevel = nextlevel
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
        elif gameinput == '8' or 'quit' or 'Quit':
            print('Quitting The Process.')
            time.sleep(0.3)
            money = -1


def commonegg():
    global pets
    global money
    money -= 2
    print("This egg cost 2 Money's")
    print('Hatching common egg')
    previous_lucky_weight = 0
    lucky_weight = []
    for weight in common_weight:
        current_lucky_weight = weight * luck
        cumulative_lucky_weight = current_lucky_weight + previous_lucky_weight
        lucky_weight.append(cumulative_lucky_weight)
        previous_lucky_weight = cumulative_lucky_weight

    print(lucky_weight)
    large_number = max(lucky_weight)
    smallest_number = min(lucky_weight)
    print(common_weight)

    test = random.uniform(smallest_number, large_number)
    print(f'Your odds are')
    print(test)
    if test > lucky_weight[0]:
        pets.append(common_pets[0])
        money += COMMONPET_PAYMENT[0]

    elif lucky_weight[0] < test > lucky_weight[1]:
        pets.append(common_pets[1])
        money += COMMONPET_PAYMENT[1]

    elif lucky_weight[1] < test > lucky_weight[2]:
        pets.append(common_pets[2])
        money += COMMONPET_PAYMENT[2]

    elif lucky_weight[2] < test > lucky_weight[3]:
        pets.append(common_pets[3])
        money += COMMONPET_PAYMENT[3]

    elif lucky_weight[3] < test > lucky_weight[4]:
        pets.append(common_pets[4])
        money += COMMONPET_PAYMENT[4]

    elif lucky_weight[4] < test > lucky_weight[5]:
        pets.append(common_pets[5])
        money += COMMONPET_PAYMENT[5]

    elif lucky_weight[5] < test > lucky_weight[6]:
        pets.append(common_pets[6])
        money += COMMONPET_PAYMENT[6]

    print(pets)

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

def diamondegg():
    global pets
    global money
    money -= 100
    print("This egg cost 100 Money's")
    print('Hatching diamond egg')
    hatched_item = random.choices(DIAMONDEGG_OUTCOMES, weights=DIAMONDEGG_WEIGHT, k=1)[0]
    print(f"You hatched: {hatched_item}")
    pets.append(hatched_item)  # Use .append() for adding a single item
    print("Your current pets:", ', '.join(pets))  # Print without brackets
    if hatched_item == 'Diamond Dog':
        money += DIAMONDEG_PAYMENT[0]
    elif hatched_item == 'Diamond Rabbit':
        money += DIAMONDEG_PAYMENT[1]
    elif hatched_item == 'Diamond Bunny':
        money += DIAMONDEG_PAYMENT[2]
    elif hatched_item == 'Diamond Wolf':
        money += DIAMONDEG_PAYMENT[3]
    elif hatched_item == 'Diamond Hex':
        money += DIAMONDEG_PAYMENT[4]
    elif hatched_item == 'Diamond Dogcat':
        money += DIAMONDEG_PAYMENT[5]
    elif hatched_item == 'Diamond Prism':
        money += DIAMONDEG_PAYMENT[6]
    elif hatched_item == 'Diamond Ring':
        money += DIAMONDEG_PAYMENT[7]
    elif hatched_item == 'Apex Diamond':
        money += DIAMONDEG_PAYMENT[8]
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