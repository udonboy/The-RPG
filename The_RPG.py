import sys
import random
x = 2543
y = 2342
sys.path.append(r'C:\\Users\\david\\OneDrive\\Desktop\\The RPG Folder\\RPG Battle Code.py')
sys.path.append(r'C:\\Users\\david\\OneDrive\\Desktop\\The RPG Folder\\gamevariables.py')
from gamevariables import excalibur, rustysword, musket, greatsword, prisonexplored, daggerdrawn, GamePartOneDone, GamePartTwoDone, damagedDagger, walked, GameOver, alreadywalkedtwice, alreadyexamined, alreadyexaminedtwice, alreadyexaminedthreetimes, alreadyexaminedfourtimes, annoyance_level_beginning, hasDagger, doorseen, currentweapon, newweapon
import time
number = random.randint(1, 50)
delay = 0.1

ohmypc = """
OHHHHHHHHHHHHHHHHHHH MY PCCCCCCCCCCCCCCCCCCCCCCCCCC
"""
servercheats = """
You just tried to activate server cheats, which, of course, runs the risk of breaking the entire game.
You've got no respect for the strict order of scripted narrative events and I just can't have that.
I would have thought that the Stanley Parable would have taught you how serious of a problem this is,
but it seems not even infinity years in the serious room could teach you that. But you'll agree with
me when you hear of your new punishment-

ENDING ???= ONE BILLION TRILLION INFINITIES IN THE SERIOUS ROOM


"""
foundstairs = """
You kick down a door and find a set of stairs. You're ready for the long journey ahead.

"""

alreadyhavethat = """
You find another weapon, but it seems you already have one of
the same. To make it worse, this one is lesser quality.
"""
alreadyhaveExcalibur = """
You examine Excalibur. It gleams in the morning sun, and you know
in your heart that you earned this blade through persistence.

"""
getgreatsword = """
You find a massive blade. Even though it feels rather unsteady
in your grasp, you know that this blade will serve you well.

"""
getmusket = """
You find an old musket. You'll have to find gunpowder
and ammunition, but other than that, you have a good weapon.

"""
getrustysword = """
You find a rusty sword. It's not pretty,
but it'll do the job better than your dagger.

"""
nodice = """
No dice. You come up empty handed.
But don't be discouraged! Your luck could yet turn.
"""
getexcalibur = """
You recieve a vison of a lady in the middle of the lake,
holding an almost glowing blade. Your eyes fall upon your hands,
and you now wield Excalibur.

"""
easyexit = """
Good news! The exit is easy to find. The bad news is that it's a
hole in the wall leading to a sharp drop onto equally sharp
rocks. It's obvious that it was used to execute inmates, since the
rocks below are adorned with broken skeletons.

"""
british = """
Like a British gangster, you shank the rat repeatedly in the neck
and face. It shrieks, but it's protests are cut off as you sever it's
brain stem. If that didn't kill it, the tetanus would.
"""
daggerdraw = """
Great call. You draw the dagger and sneak up on the sleeping rat.
It is none the wiser to your plot as it sleeps peacefully.
"""
exploreprison = """
You peek around the prison. It smells like mildew, feces
and all the pleasantries you'd expect from a seaside prison.
The morning dew tickles your nostrils, but you become aware of
a giant rat sleeping in the corner of one of the cells.

"""
homefree = """
You angle the dagger around and jiggle it in the lock.
In a few tense moments, the lock comes free and the door
comes open. Now the world is your oyster!

"""
DoorSeen = """
You examine the cell door, noticing that it consists of thick metal bars.
You also notice that the cell door is locked by a simple lock. Your
dagger could be usefull here.

"""
damageddagger = """
I'm not sure what you were going for here. But the best you can do is
carve your name into the stone, ruining the historical value of this
medieval prison cell. And you also break the tip off of your rusty dagger.
Good going, jackass.
"""
donthavethat = """
Hey, buddy. I bet that would have been real cool
if you had that item in your possession. But you
don't, so you can't do that.

"""
cc = """
Right then, a bit of a workout! You walk around your cell,
hoping to warm up your legs. At least you're working on that.

"""
ending4 ="""
You probably should have drawn your weapon before getting the
rat's attention. Rats are usually some of the easiest to kill,
but this one's jaws are bigger than your head, and the rodent's
teeth make quick work of your frontal lobe.

ENDING 4: Was That The Bite of '87???

"""
ending3 = """
Your dagger breaks. The problem is, you realize later that it was supposed
to help you pick the lock on your cell door. So, you end up stuck in there
for the rest of your severely shortened life, killed by dehydration.

ENDING 3: Not Very Sharp

"""
ending2 = """
Ah, you thought I'd stop you? I'm just the narrarator! But as your
lifeblood spills onto the broken flooring, you realize your mistake as
your life comes to an end.

ENDING 2: You Did It For The Platinum
"""
ending1meta = """
After ignoring the pleas and threats of my fellow narrator who just
quit on the spot, you discover the molecular structure of the cell,
and you realize you are in a video game. But alas, the digital deity
that oversees the game realizes you know too much, and you cease to exist.

ENDING 1: A Bit Too Meta
"""
aaaa = """
Seriously, you need to move on.
It's quite warm in this cell, meaning
if you don't find a way out, dehydration
will eventually be your downfall.
"""
aaa = """
I don't get why you need to take ANOTHER look around, but I guess I'll humor you.
After taking another look around the room, you discover that someone else was here
before you, since that lovely hole in the ground is home to a nice bit of bile on
the bottom.
"""
aa = """
Even though it seemed it would serve no merit to look around again,
a second look around seems to reveal a dagger in the corner. It's a bit
dirty, but it'll do in a pinch.
"""
a = """
For a nuisance to society, this would seem like home sweet home.
A nice bed made of straw and a hole in the ground to... yeah.
The bars seem to be made of a thick iron.
"""
b = """
You awaken in a cold cell. It doesn't seem that there are any guards around.
Your head is buzzing, and you don't remember where you came from,
or why you are seemingly incarcerated.
"""
c = """
You walk around, hoping the exercise will help jog your memory. (Get it? Jog?)
But to no avail. At least the exercise keeps you busy and active. Wouldn't want
those calves of yours to shrivel up, would we?
"""

def TheGamePartOne():
    global walked, alreadywalkedtwice, hasDagger,damagedDagger,doorseen, GamePartOneDone, x,y
    global alreadyexamined, alreadyexaminedtwice, alreadyexaminedthreetimes, alreadyexaminedfourtimes
    global annoyance_level_beginning, GameOver, delay, currentweapon

    while not GameOver:
        if annoyance_level_beginning >= 5:
            print("Don't you have anything better to do?")
        if annoyance_level_beginning >= 10:
            print("Quit messing with me!")
        if annoyance_level_beginning >= 15:
            print("GET OUT!!!")
            print("Achievement unlocked! Dude, STOP!")
            if annoyance_level_beginning >= 90001:
                print("Achievement unlocked! LITERALLY BRAINDEAD!")                
            exit()
        user_input = input("""Welcome to the game! You are currently in a dreamscape. What will you do?
        
        Wake up
        Say hello
        Oh my PC
        
        (type 'exit' to quit): """).lower()
        
        match user_input:
            case 'skibidi rizz'|'i like my cheese drippy bruh'|'respect the drip':
                print("I don't know what that means.")
                annoyance_level_beginning += 90001
            case 'oh my pc':
                while True:
                    x = x*2321
                    y = y*4321
                    z = (x*y)
                    w = z * z
                    print(z)
                    print(ohmypc)
                    time.sleep(delay)
                    delay = delay + 0.01
                    if z >= 35232998000351984430380884104457591810391269244051350961553407661528772192347981560842776902171698192782087994940028123206162395471645314604751929383135548499418914001282259701835492753301223131045396033418448283992089180477853397451623179810771563626904757160762151537408870840796419273403816823435711688375635743459033892414354499310147951747349044960323318870097509459602479187394251150651785671660912397775951442148093869005688696668910364389917933226858171241038960932517592803965121987546338056749706736089678662998915267975345001414649090536027709407886673384353213405207974301686179221952224898375539834580978839331042587914016521807173431071008166372645090567717368463263387198346446430375612305572292941953802052007777459515367126995757554482122555776834587752967232396297629896546347742262:
                        print("Your PC has exploded.")
                        quit()
            case 'hello' | 'hi' | 'hola' | 'how are you':
                print("Um, hi? It's kinda weird that you're talking to your subconsciousness.")
                annoyance_level_beginning += 1
            case 'be my husbando':
                print("Get outta here, pervert.")
                quit()
            case 'exit':
                print("Exiting...")
                break
            case 'wake up' | 'awaken' | 'get up':
                print(b)
                break
            case 'sv_cheats 1':
                print(servercheats)
                time.sleep(31,536,000)
                exit

    # Once you "wake up" in the cell
    while not GameOver:
        
        if doorseen == True:
            user_input = input("""
        
        You are in a cell. You clutch the dagger in your hand. What will you do?(type 'exit' to quit):

        Examine
        Walk around
        Pick lock

        """).lower()
            
        elif hasDagger == True:
            user_input = input("""
        
        You are in a cell. You clutch the dagger in your hand. What will you do?(type 'exit' to quit):

        Examine
        Walk around
        Examine door

        """).lower()
        else:
            user_input = input("""

        You are in a cell. What will you do?(type 'exit' to quit):

        Examine
        Walk around

        """).lower()

        match user_input:
            case 'exit':
                print("Exiting...")
                break
            case 'examine' | 'survey' | 'look':
                if not alreadyexamined:
                    print(a)
                    alreadyexamined = True
                elif not alreadyexaminedtwice:
                    print(aa)
                    alreadyexaminedtwice = True
                    hasDagger = True
                    newweapon = "dagger"
                elif not alreadyexaminedthreetimes:
                    print(aaa)
                    alreadyexaminedthreetimes = True
                elif not alreadyexaminedfourtimes:
                    print(aaaa)
                    alreadyexaminedfourtimes = True
                else:
                    print(ending1meta)
                    GameOver = True
            case 'walk around' | 'excercise' | 'poke around':
                if walked == False:
                    print(c)
                    walked = True
                elif not alreadywalkedtwice:
                    print(cc)
                    alreadywalkedtwice = True
            case 'use dagger on self' | 'seppuku' | 'pro gamer move':
                if hasDagger == True:
                    print(ending2)
                    GameOver = True
                else:
                    print(donthavethat)
            case 'use dagger on wall' | 'stab wall with dagger' | 'chip at wall':
                if hasDagger == True:
                    print(damageddagger)
                    damagedDagger = True
                else:
                    print(donthavethat)
                if damagedDagger == True:
                    print(ending3)
                    GameOver = True
            case 'examine door' | 'analyze door' | 'look at door' | 'survey door':
                print(DoorSeen)
                doorseen = True
            case 'pick lock' | 'use dagger on lock' | 'open lock with dagger':
                if doorseen == True:
                    print(homefree)
                    GamePartOneDone = True
                    break

def simulated_wait(seconds):
    while seconds > 0:
        # Wait for smaller chunks of time, such as 10 seconds
        wait_time = min(10, seconds)
        time.sleep(wait_time)
        seconds -= wait_time
        print(f"{seconds} seconds remaining...")

def TheGamePartTwo():
    global GameOver,prisonexplored,daggerdrawn,number, excalibur, rustysword, musket, greatsword,GamePartTwoDone
    global currentweapon, newweapon
    while not GameOver:
        user_input = input("Be cautious of your surroundings. (type 'exit' to quit): ").lower()
        
        match user_input:
            case 'walk around':
                print(exploreprison)
                battlechance()
            case 'examine':
                if prisonexplored == False:
                    print(exploreprison)
                    prisonexplored = True
                    battlechance()
                else:
                    print("Could you be a bit more specific about that? You've already poked around.")
            case 'draw dagger' | 'unsheathe dagger' | 'brandish dagger' | 'reach for dagger' | 'take out dagger':
                print(daggerdraw)
                daggerdrawn = True
            case 'use dagger on rat':
                if daggerdrawn == True:
                    print(british)
                else:
                    print(ending4)
                    GameOver = True
            case 'look for exit' | 'search for exit' | 'seek an exit' | 'locate exit' | 'find a way out' | 'look for a way out' | 'find an exit':
                print(easyexit)
                battlechance()
            case 'search for weapons' | 'search for weapon' | 'weapon':
                number = random.randint(1, 100)  # Using 1 to 100 for better percentage control

                if number == 17:  # 1% chance to get Excalibur
                    if excalibur == False:
                        print(getexcalibur)
                        excalibur = True
                        newweapon = "excalibur"
                        weaponswap()
                    else:
                        print(alreadyhaveExcalibur)
                elif number <= 50:  # 50% chance to get 'nodice'
                    print(nodice)
                elif number <= 70:  # 20% chance to get a Rusty Sword
                    if rustysword == False:
                        print(getrustysword)
                        rustysword = True
                        newweapon = "rustysword"
                        weaponswap()
                    else:
                        print(alreadyhavethat)
                elif number <= 85:  # 15% chance to get a Musket
                    if musket == False:
                        print(getmusket)
                        musket = True
                        newweapon = "musket"
                        weaponswap()
                    else:
                        print(alreadyhavethat)
                else:  # 15% chance to get a Greatsword
                    print(getgreatsword)
                    greatsword = True
                    newweapon = "greatsword"
                    weaponswap()
            case 'look for stairs' | 'look for other exit' | 'stairs' :
                print(foundstairs)
                GamePartTwoDone = True
                break
def weaponswap():
    global currentweapon, newweapon
    if currentweapon != "":  # If there's already a weapon
        print(f"You already have your {currentweapon}. Would you like to swap it for {newweapon}?")
        choice = input("Yes or no? ").lower()  # Corrected input usage
        
        match choice:
            case 'no':
                newweapon = ""
                print(f"You keep your {currentweapon}. I hope you don't regret this later.")
            case 'yes':
                print(f"You toss your old {currentweapon} away for your new {newweapon}. I hope you don't regret this later.")
                currentweapon = newweapon  # Assign new weapon
                newweapon = ""
                weaponcheck()
    else:  # If no weapon currently equipped
        currentweapon = newweapon  # Equip the new weapon directly
        newweapon = ""
        print(f"You now wield the {currentweapon}.")
        weaponcheck()
def battlechance():
    battlestart = random.randint(1, 50)
    if battlestart >= 100:
        from RPG_Battle_Code import Battle
        Battle()
def weaponcheck():
    if currentweapon != "dagger":
        hasDagger = False
    if currentweapon != "excalibur":
        excalibur = False
    if currentweapon != "rustysword":
        rustysword = False
    if currentweapon != "musket":
        musket = False
    if currentweapon != "greatsword":
        greatsword = False
        
# Start the game
def TheGame():
    TheGamePartOne()
    if GamePartOneDone == True:
        print("Well done! Now the game begins.")
        TheGamePartTwo()
    if GamePartTwoDone == True:
        print("Thank you for playing the demo!")
        
TheGame()
if GameOver == True:
    retry = input("""
Would you like to restart the game?""").lower()
    match retry:
        case 'yes':
            GameOver = False
            TheGame()
        case 'no':
            print("Thanks for playing the game!")
            exit()