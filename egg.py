import random
import threading
import time

Cash: int = 1_000_000_000_000
current_luck = 0
MainGameInput: str = ''
pets: list = []
petsvalue: dict = {'dog': 2, 'cat': 3, 'bird': 5}
potionactive = False
autodelete_list = []
Eggwantinghatched = None
settingconfirmpets = True
userhatchspeedlevel = 0
base_hatch_time = 1.0
speed_increase_per_level = 0.05
hatchspeed = 1

def luckpotionend():
    global current_luck
    global potionactive
    print('')
    print('!!!YOUR POTION HAS ENDED!!!')
    current_luck = 0
    potionactive = False


def mainloop():
    global Cash
    global current_luck
    global MainGameInput
    global pets
    global petsvalue
    global potionactive
    global autodelete_list
    global Eggwantinghatched
    global settingconfirmpets
    global userhatchspeedlevel
    global base_hatch_time
    global hatchspeed
    global speed_increase_per_level

    print('1. Hatch eggs')
    print('2. Sell Pets')
    print('3. Shop')
    print('4. Pets!')
    print('5. Put Pet up for auto-delete.')
    print('6. Remove pet from auto-delete')
    print('7. Settings')
    try:
        MainGameInput = input('What do you want to do! ')
    except ValueError:
        print('Something went wrong please try agian')
    if MainGameInput == '1':
        print('')
        print('1. Common Egg: 2 Cash')
        print('2. Rare Egg: 5 Cash')
        print('3. Diamond Egg: 10 Cash')
        userwantegg: str = input('Which egg do you want to hatch ')
        if userwantegg == '1':
            Eggwantinghatched = 'Common egg'
            print(f'Egg hatching: {Eggwantinghatched}')
        elif userwantegg == '2':
            Eggwantinghatched = 'Rare Egg'
            print(f'Egg hatching: {Eggwantinghatched}')
        elif userwantegg == '3':
            Eggwantinghatched = 'Diamond Egg'
            print(f'Egg hatching: {Eggwantinghatched}')

    elif MainGameInput == '2':
        print('')

        usersellingpet = input('Which pet do you want to sell: ')
        if usersellingpet not in pets:
            print('That is not a pet or you dont own it')
            return
        else:
            try:
                sell_amount = petsvalue[usersellingpet]
            except KeyError:
                print(
                    'Something went wrong please try agian with a pet in your'
                    ' inventory!'
                )
                return
            print(f'The pet your selling is worth {sell_amount} Cash.')
            if settingconfirmpets is True:
                areyousure = input('Are you sure you want to sell this pet? (y/n) ')
                if (
                    usersellingpet in pets
                    and usersellingpet in petsvalue
                    and areyousure == 'y'
                ):
                    sell_amount = petsvalue[usersellingpet]
                    print(sell_amount)
                    Cash += sell_amount
                    print(f'Your Cash is now {Cash}')
                    pets.remove(usersellingpet)
                    print(pets)
                else:
                    print('You ethier dont own the pet your trying to sell or it does not have a value or you said No to the are you sure question' )
            elif settingconfirmpets is False:
                if usersellingpet in pets and usersellingpet in petsvalue:
                    sell_amount = petsvalue[usersellingpet]
                    print(sell_amount)
                    Cash += sell_amount
                    print(f'Your Cash is now: {Cash}')
                    pets.remove(usersellingpet)
                    print(pets)
    if MainGameInput == '3':
        print('1. Hatch Speed Upgrades')
        print('2. Potion upgrades')
        try:
            shopinput = input('What thing do you want to do in the shop: ')
        except ValueError:
            return
        if shopinput == '1':
            if userhatchspeedlevel < 19:
                nextlevel =  userhatchspeedlevel + 1
                hatchspeedcost = nextlevel ** 2 + nextlevel * 3
                localinput = input(f'Would you like to upgrade hatchspeed, Your current level is {userhatchspeedlevel}, Cost is {hatchspeedcost}. (y/n) ')
                if localinput.lower() == 'y' and Cash > hatchspeedcost:
                  Cash -= hatchspeedcost
                  userhatchspeedlevel += 1
                  hatchspeed = base_hatch_time - (userhatchspeedlevel * speed_increase_per_level)
                  hatchspeed = max(hatchspeed, 0.05)
                  print(f'You upgraded your hatchspeed:{hatchspeed} seconds now!')
                elif localinput.lower() == 'n':
                    print('Thank you for coming to the shop!')
            elif userhatchspeedlevel >= 19:
                print('You can not have a hatch level over 19.')
        elif shopinput == '2' and not potionactive:
            print(f'Current Luck Level is {current_luck}')
            print('1. Potion Level 1, +1 Luck level for 2 minutes: 5 Cash')
            print('2. Potion Level 2, +2 Luck level for 3 minutes: 7 Cash')
            print('3. Potion Level 3, +3 Luck level for 5 minutes: 10 Cash')
            print('4. Potion Level 4, +4 Luck level for 6 minutes: 12 Cash')
            print('5. Potion Level 5, +5 Luck level for 7 minutes: 15 Cash')
            print('6. Potion Level 5, +6 Luck level for 8 minutes: 20 Cash')

            potionbuying = input('What Potion do you want to buy ')
            if potionbuying == '1' and Cash > 5:
                print('You bought a potion')
                Cash -= 5
                potionactive = True
                current_luck += 1
                timer = threading.Timer(60 * 2, luckpotionend)
                timer.start()
            elif potionbuying == '2' and Cash > 7:
                print('You bought a potion')
                Cash -= 7
                potionactive = True
                current_luck += 2
                timer = threading.Timer(60 * 3, luckpotionend)
                timer.start()
            elif potionbuying == '3' and Cash > 10:
                print('You bought a potion')
                Cash -= 10
                potionactive = True
                current_luck += 3
                timer = threading.Timer(60 * 5, luckpotionend)
                timer.start()
            elif potionbuying == '4' and Cash > 12:
                print('You bought a potion')
                Cash -= 12
                potionactive = True
                current_luck += 4
                timer = threading.Timer(60 * 6, luckpotionend)
                timer.start()
            elif potionbuying == '5' and Cash > 15:
                print('You bought a potion')
                Cash -= 15
                potionactive = True
                current_luck += 5
                timer = threading.Timer(60 * 7, luckpotionend)
                timer.start()
            elif potionbuying == '6' and Cash > 20:
                print('You bought a potion')
                Cash -= 20
                potionactive = True
                current_luck += 6
                timer = threading.Timer(60 * 8, luckpotionend)
                timer.start()
            else:
                print('Not valid input!')
        else:
            print('You have a potion active!')
    if MainGameInput == '4':
        print(f'Your pets are {pets}')
    elif MainGameInput == '5':  # Add pet to auto-delete
        autodelete = input(
            'Which pet would you like to put up for auto-delete? '
        )
        if autodelete in pets:
            autodelete_list.append(autodelete)
            print(f'{autodelete} marked for auto-delete.')
        else:
            print(f'{autodelete} is not in your inventory.')
    elif MainGameInput == '6':
        cancel_delete = input(
            'Which pet would you like to remove from auto-delete? '
        )
        if cancel_delete in autodelete_list:
            autodelete_list.remove(cancel_delete)
            print(f'{cancel_delete} is no longer marked for auto-delete.')
        else:
            print(f'{cancel_delete} was not in auto-delete.')
    elif MainGameInput == '7':
        print('1. Turn off confirm for selling pets')
        try:
            setting = input('Put the number of the setting you want to change, if you would like to exit type a letter ')
        except ValueError:
            print('exiting settings')
        if setting == '1':
            print('Setting Confirm pets sell to off')
            settingconfirmpets = False


def eggsystem():
    global Cash
    global current_luck
    global Eggwantinghatched
    global hatchspeed
    global speed_increase_per_level
    global base_hatch_time
    print('')
#IF SOMETHING HAS A _ YOU CHANGE THAT TO YOUR NAME OF EGG OR YOUR NUMBER (NUMBER IN CASE OF THE CASH)
#TO ADD A NEW EGG, JUST GO TO MAINGAININPUT, THEN PRINT A NUMBER THAN THE NAME OF YOUR EGG, ELIF USER WANTS YOUR NUMBER, 
# IF SO THAN MAKE THE Eggwantinghatched to Eggwantinghatched == 'YOUR_REAL_EGG_NAME_HERE':
# and then come to here and do if Eggwantinghatched == 'YOUR REAL EGG NAME HERE', Then ident, The have your odds for your egg in a list,
# and your pet names in a list with strings with commas inbetween egg names then do usingodds = the_name_of_your_odds_list, 
# and usingpets = the_name_of_your_pets_list
# !!!BUT THE LIST SHOULD HAVE THE SAME AMOUNT OF PETS AND ODDS TO KEEP FROM BREAKING THE SYSTEM!!!!
# Also if you want the egg to cost cash than add cost = amount_of_cash_you_want_to_charge
    ######################
    if Eggwantinghatched == 'Common egg':
        commonodds = [50, 40, 10, 1]
        commonpets = ['dog', 'cat', 'bird', 'elephant']
        usingodds = commonodds
        usingpets = commonpets
        cost = 3
    ######################
    if Eggwantinghatched == 'Rare Egg':
        rareodds = [90, 9, 0.9, 0.1]
        rarepets = ['Panda', 'Coyote', 'Giraff', 'Dogcat']
        usingodds = rareodds
        usingpets = rarepets
        cost = 5
    ######################
    if Eggwantinghatched == 'Diamond Egg':
        diamondodds = [26,25,25,23.8389,0.1,0.05,0.01,0.001,0.0001]
        diamondpets = ['Diamond Dog','Diamond Rabbit','Diamond Bunny','Diamond Wolf','Diamond Hex','Diamond Dogcat','Diamond Prism','Diamond Ring','Apex Diamond']
        usingodds = diamondodds
        usingpets = diamondpets
        cost = 10
    lucky_weights = []
    bump_map = {
        6: 0.11,  # luck=6 → 10% per point
        5: 0.10,  # luck=5 → 15% per point
        4: 0.09,  # luck=4 → 16% per point
        3: 0.08,  # luck=3 → 25% per point
        2: 0.07,
        1: 0.06,
        0: 0.05,
    }
    if Eggwantinghatched != None:
        for i in range(len(usingodds)):
            value = usingodds[i]
            bump = bump_map[current_luck]
            if value <= 10:
                factor = 1 + current_luck * bump
            else:
                factor = 1
            lucky_weights.append(value * factor)
        print(f'lucky_weights: {lucky_weights}')
        totalweight = sum(lucky_weights)
        try:
            amountsofeggwantinghatched = int(
                input('How many eggs do you want to hatch! ')
            )
        except ValueError:
            print('Not a valid input!')
            Eggwantinghatched = ''
            return
        

        while amountsofeggwantinghatched > 0:
            if Cash >= (cost + 1):
                Cash -= cost
                cumulative = 0
                eggroll = random.uniform(0, totalweight)
                for i in range(len(lucky_weights)):
                    cumulative += lucky_weights[i]
                    if eggroll < cumulative:
                        hatched = usingpets[i]
                        break
                amountsofeggwantinghatched -= 1
                if hatched in autodelete_list:
                    print(f'The pet you hatched:{hatched} is in auto delete, it will not be given')
                else:
                    pets.append(hatched)
                    print(f'You hatched {hatched}.')
                    time.sleep(hatchspeed)
            else:
                print('Your out of Cash please sell pets to make more!')
                break

    Eggwantinghatched = None


while Cash >= 0:
    while any(
        pet in pets for pet in autodelete_list
    ):  # Keep running until all auto-delete pets are gone
        for pet in autodelete_list[:]:
            if pet in pets:
                pets.remove(pet)
                print(f'{pet} was automatically removed.')
                
    mainloop()
    if Eggwantinghatched != '':
        eggsystem()
