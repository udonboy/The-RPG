import sys
sys.path.append(r'C:\\Users\\david\\OneDrive\\Desktop\\The RPG Folder\\gamevariables.py')
from gamevariables import yourhp, yourmp, youratk, enemyhp, enemymp, enemyatk, gameover, hitchance, defchance, turnused, pastries, potions, battleOver, musketmiss, enemyexp, enemyname, playerlevel, yourexp, expreq
import random

def Battle():
    global gameover, enemyhp, expreq, yourhp, turnused, yourmp, hitchance, enemymp, shield, musketmiss, yourexp, enemyexp, playerlevel, youratk
    defineenemy()
    while gameover == False:
        if enemyhp <= 0:
            print ("Your foe has fallen! You win!")
            yourexp = yourexp + enemyexp
            while playerlevel < 1000:
                if yourexp >= expreq:  # Adjust the required experience threshold if needed
                    yourexp -= expreq   # Subtract the experience needed for this level
                    playerlevel += 1
                    print(f"Level up! You are now level {playerlevel}.")
                    expreq = expreq + 20
        
        # Increase player stats
                    yourhp += 20
                    yourmp += 20
                    youratk += 10
                else:
                    break  # Exit the loop if the experience is not sufficient for the next level
        if yourhp <= 0:
            print ("Your eyes roll back into your skull as you perish.")
            gameover = True
        if turnused == False:
            if gameover == False:
                print(f"A {enemyname} stands before you! What will you do? You have {yourhp} health and {yourmp} magic.")
                userinput = input("""
        Attack
        Defend
        Ability
        Item
        Magic
        Run

        """).lower()
                turnused = True
                match userinput:
                    case "attack":
                        hitchance = random.randint(1, 50)
                        print("You attack the monster!")
                        if hitchance > 30:
                            print ("The attack lands! You deal 15 damage!")
                            enemyhp = enemyhp - youratk
                        else:
                            print ("The monster blocks your attack!")
                    case "defend":
                        print ("You put up your shield!")
                        shield = True
                    
                    case 'ability':
                        if shield == True:
                            print("Rage of the Shield Hero")
                        if excalibur == True:
                            print("Light of Arthur")
                        if musket == True:
                            print("Sharpshooters Glory")
                        if greatsword == True:
                            print("Mighty Blow")
                        if hasDagger == True:
                            print("British Shank")                    
                        if rustysword == True:
                            print("Old Warrior's Pride")                    
                        abilitychoice = input("Which ability in your roster do you wish to use?").lower()

                        match abilitychoice:
                            case 'light of arthur':
                                if yourmp == 100:
                                    print("You unleash the holy sword's flame upon your foe! You deal 50 damage!")
                                    enemyhp = enemyhp - 50
                                    yourmp = yourmp - 100
                                else:
                                    print("You don't have enough Magic for that.")
                            case 'sharpshooters glory':
                                musketmiss = False
                                if yourmp >= 50:
                                    while musketmiss == False:                               
                                        hitchance = random.randint(1, 50)
                                        if hitchance > 25:
                                            print("You blast a hole in your foe!")
                                            enemyhp = enemyhp - 20
                                        else:
                                            print("You miss! Spree ends.")
                                            yourmp = yourmp - 50
                                            musketmiss = True
                                else:
                                    print("You don't have enough Magic for that.")
                        #case 'mighty blow'
                        #case 'british shank'
                        #case 'old warriors pride'
            
                    case 'item':
                        if pastries > 0:
                            print (f"You have {pastries} pasteries left.")
                        if potions > 0:
                            print (f"You have {potions} potions left.")
                        itemchoice = input("What item do you want?").lower()
                        
                        match itemchoice:
                            case 'pastry':
                                print ("You eat the pastry and gain 20 HP!")
                                yourhp = yourhp + 20
                                if yourhp > 100:
                                    yourhp = 100
                            case 'potion':
                                print("You drink the potion and recover 20 MP!")
                                yourmp = yourmp + 20
                                if yourmp > 100:
                                    yourmp = 100
            if turnused == True:
                turnused = False
                hitchance = random.randint(1, 50)
                print ("The monster attacks!")
                if hitchance > 30:
                    if shield == True:
                        print ("You block the attack, but take a little damage!")
                        yourhp = yourhp - (enemyatk - 10)
                        shield = False
                    else:
                    
                        print (f"The attack lands! You take {enemyatk} damage!")
                        yourhp = yourhp - enemyatk
                else:
                    print ("You manage to dodge the attack!")

def defineenemy():
    global enemyhp, enemyatk, enemymp, enemyexp, enemyname
    enemytype = random.randint(1,100)
    if enemytype <= 20:
        enemyhp = 200
        enemymp = 200
        enemyatk = 20
        enemyexp = 20
        enemyname = "Dire Wolf"
    elif enemytype <= 40:
        enemyhp = 250
        enemymp = 100
        enemyatk = 25
        enemyexp = 25
        enemyname = "Troll Guard"
    elif enemytype <= 60:
        enemyhp = 100
        enemymp = 100
        enemyatk = 30
        enemyexp = 30
        enemyname = "Troll Bruiser"
    elif enemytype <= 80:
        enemyhp = 400
        enemymp = 150
        enemyatk = 35
        enemyexp = 35
        enemyname = "Giant Enemy Spider"
    elif enemytype <=100:
        enemyhp = 400
        enemymp = 150
        enemyatk = 35
        enemyexp = 50
        enemyname = "Skeletor"