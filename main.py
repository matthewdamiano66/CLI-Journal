import datetime
import os
def instance():
    with open("journal.txt", "a+") as cursor:
        cursor.seek(0)
        contents = cursor.read()
        print(contents)

        entry = input("New entry: ")
        timestamp = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        cursor.write(entry +"\n"+ timestamp+"\n")

        print("Entry saved.")

def remove():
       print("Deleting...")
       os.remove("journal.txt")
       print("Journal Removed")       

    
def main():
    commands = ("new", "delete", "close")

    while True:
        user = input("Enter a command (new, delete, close): ").strip().lower()

        if user == "new":
            instance()

        elif user == "delete":
            remove()

        elif user == "close":
            break

        else:
            print("Invalid command.")





if __name__ == "__main__" :
    main()  
