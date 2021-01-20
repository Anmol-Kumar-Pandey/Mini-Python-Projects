import random

table = random.randrange(1, 10)

def invite(name,time,**kwarg):
    """
    This function invites people
    to our party
    """
    print("-----------------------------------")
    print(f"Good Morning {name}")
    print(f"You are requested to come to radisun\n blu with your family at {time}")
    print(f"Your food will be waiting for you!!")
    print(f"Your table number is {table}")
    print("Your orders :)")
    for food in kwarg:
        print(f"{food} ---> {kwarg[food]}")

    print("------------------------------------")

you = {
    "Chilli":"$10","Roti":"$1"
}
invite("Anmol","8pm",**you)

"""Below code is for getting documentation of
the function invite"""
# print(invite.__doc__)