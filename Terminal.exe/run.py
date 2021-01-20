import os # For making terminal able to play with files
from datetime import date

today = date.today()

# Input Part Here
while True:
    ask = input("What do you want to do?\n")
        
    if ask == "files":
        Task = input("What do you want to do in this folder?\n")

        # List Directories
        if Task == "ls":
            for files in os.listdir():
                print(files, end=", ")
            print()
            continue

        # Create Files
        elif Task == "create":
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
        print("You completed Maths Services")
        continue

    else:
        print(f"'{ask}' -----> this is not a keyword of terminal.exe")
        continue

# Thanks
# 'https://www.programiz.com/python-programming/datetime/current-datetime' for the code of date time module