import os # For making terminal able to play with files
from datetime import date

today = date.today()

# Input Part Here
while True:
    ask = input("What do you want to do?\n")
        
    # List Directories
    if ask == "ls":
        for files in os.listdir():
            print(files, end=", ")
        print()
        continue

    if ask == "files":
        Task = input("What do you want to do in this folder?\n")


        # Create Files
        if Task == "create":
            name = input("Enter the name of the file: ")
            f = open(name, "x")
            f.close()
            continue

        # Write in a file ----> overwrite
        elif Task == "overwrite":
            files = input("Enter the name of the file: ")
            content = input("Enter your content that to be written:\n")
            f = open(files, "w")
            f.write(content)
            f.close()

        # Append a file ----> write
        elif Task == "write":
            files = input("Enter the name of the file: ")
            content = input("Enter the content of the file here: \n")
            f = open(files,'a')
            f.write(content)
            f.close()

        # Content of a file ----> content
        elif Task == "content":
            files = input("Enter the name: ")
            f = open(files, "r")
            print(f.read())
            f.close()

        else:
            print(f"'{Task}' -----> this is not a keyword of terminal.exe")
            continue
        continue


    # Quit Condition
    elif ask == "quit()":
        print("================Thanks Message=============")
        print("\tThankyou for using this terminal.")
        print("\tLast active on", today)
        break

    # Maths Condition
    elif ask == "Maths":
        while True:
            tell = input("Enter what should I do: ")
            if tell == "callc":
                math_quantity = int(input("How many numbers do you want to enter?\n"))

                numbers_align = []
                i = 0
                while i < math_quantity:
                    num = int(input("Enter your number: "))
                    i += 1
                    numbers_align.append(num)
                # print(numbers_align)
                
            total = 0
            if tell == "add":
                for q in numbers_align:
                    total += q
                print(total)

            elif tell == "sub":
                for q in numbers_align:
                    total -= q
                print(total)

            elif tell == "prod":
                for q in numbers_align:
                    total *= q
                print(total)

            elif tell == "div":
                for q in numbers_align:
                    total /= q
                print(total)

            elif tell == "q":
                break


        print("You got out of our Maths Services")
        continue

    else:
        print(f"'{ask}' -----> this is not a keyword of terminal.exe")
        continue

# Thanks
# 'https://www.programiz.com/python-programming/datetime/current-datetime' for the code of date time module