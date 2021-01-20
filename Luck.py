import random # for generating numbers

# Generates the position of the user
def generate():
    """
    This function generates number that is
    the position of the player.
    """
    global num
    num = random.randrange(1, 6)

# Generates the position of the elements
# Police
def police():
    """
    Generates the position of the
    police in the game
    """
    global pol
    pol = random.randrange(1, 6)

def animal():
    """
    Generates the position of the 
    animal in the game 
    """
    global ani
    ani = random.randrange(1, 6)

# Generating bonus number till 5 for no special condition for one more 6
def six():
    """
    Generates the number after you got a six
    thats a bonus
    """
    global bonus
    bonus = random.randrange(1, 5)

# Games Logic Here {**}
# Position
pos = 0
# Life gets less as soon as police shoots you
life = 5 

# Main Game Loop
while True:
    # Checks for life and for game over
    if life == 0 or life < 0:
        print("Sorry you are in the jail and\n so your game is over")
        break
    # Press Enter For Generating The Position Of The User
    enter = input("Press Enter ")
    if enter == "": # Logic after position
        generate()
        police()
        animal()
        # Generates real position
        pos += num
        print(f"Your position now {pos}/100")
        # Condition for colide
        if pos != 100 or pos < 100: # Game Is ON
            if num == pol:
                pos -= 10
                life -= 1
                print("Oh!! no police put you i the jail")
                print(f"You current position bro {pos}/100")
                print(f"Sorry to Say but police shooted you\n and so your life remains {life}")
                
            elif num == ani:
                pos += 1
                print(f"You killed a animal man, and your\n position got increased.\nYour position now is {pos}.")

            if num == 6: # Controls for the condition of 6
                six()
                pos += bonus
                print(f"Yeah you got a six!! Bonus time....\n Oh yeah you even got {bonus} after a bonus \nspin.\n So now your position is {pos}")

        else:
           if pos == 100 or pos > 100: # Checks the condition for wining the game
               print("You won the match!!") 
               break

    if enter == "q": # FOR DEBUGING
        break

# Condition to protect animal
if ani == pol:
    ani += 1

