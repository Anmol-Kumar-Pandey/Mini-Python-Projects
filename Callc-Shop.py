# Write a Python Program which will keep adding a stream of numbers inputted by the user. The adding stops when the user presses 'q' key on the keybord.

total = 0
while True:
    ask = input("What should I do now?\n")
    if (ask!='q'):
        cost = int(ask)
        total += cost
        print("User's input:",cost)
        print(f"Your total till now: {total}")
        continue
    elif (ask=='q'):
        print(f"""Thankyou for Shoping
Your total cost: {total}""")
        break