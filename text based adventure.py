print("===TEXT BASED ADVENTURE GAME===")
print("you find a weird looking amulet in the forest")
choice1=input("What do you do ? (1-inspect amulet 2-leave it there) type : (1/2) :")
if choice1=="1":
    print("you decided to inspect the amulet, but you held it for the first time you fainted, while unconscious you got a weird vision : an old man calls your name and tells you to get it (the amulet) back to him, you wake up again")
    choice2=input("a note falls on your head, a small cabin is drawn on it, you recognize this cabin, you've seen it somewhere but you don't remember anything about it, you pick up the amulet and you start wandering around until you come across a river, the amulet lits up, what do you do ? (1-throw it in the river 2-go on as if nothing happened)")
    
    if choice2=="1":
        print("are you dumb ? the river has taken the amulet and you go chase after it but don't catch it, just like that, its gone")
    else:
        choice3=input("after a few more steps you manage to find the cabin, you go in but find nothing, suddenly a swarm of bats attack it, what do you do ? (1-fight the bats 2-hide and hold onto the amulet hoping something happens")
        if choice3=="1":
            print("you try to combat the threat, after a fierce fight you manage to make them go away, but they left with some serious wounds, one more attack and you're done")
        else:
            print("you take the amulet tightly in your hands out of fear, a paralyzing light came out of it, all the bats just fell to the floor, you escaped this one")
        choice4=input("you come across a bear, it looks angry and agressive (1-leave him alone 2-try to fight him using the amulet)")
        if choice4=="1":
            print("a pacific choice, you both go on, a fog starts to build up")
        else:
            print("poor bear, he dropped dead in an instant, a fog starts to build up")
        choice5=input("the fog gets very dense, you're scared and its nightime, a dark and tall silhouette appears, you're frightned, this time you might not escape (1-use the amulet and protect yourself 2-don't do anything)")
        if choice5=="1":
            print("an agonizing noise comes from the now deceased body, you take a look, and its the same old man from the vision you had, what have you done ? you throw away the amulet and bury it, this shouldn't find itself between bad hands")
        else:
            print("its the old man ! he calls your name, you feel relieved, he takes you back to his cabin where he uhhhh i don't want to continue im tired this code aint working anyways i coded this shit on a phone dont blame me")
        
else:
    print("you go back to house and live peacefully, the game ends btw ")