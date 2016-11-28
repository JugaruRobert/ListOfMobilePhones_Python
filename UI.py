from Operations import *
import sys
def printMenu():
    """
    Function used for printing the menu in the console for the user.
    Input: -
    Output: The menu is printed
    """
    msg =" There is a list with availavle commands:"
    msg += "\n\t- Press 1 to add a phone"
    msg += "\n\t- Press 2 to remove a phone"
    msg += "\n\t- Press 3 to update the price of  a phone"
    msg += "\n\t- Press 4 to print all the phones sorted by increasing price"
    msg += "\n\t- Press 5 to print all the phones"
    msg += "\n\t- Press 6 to print the menu with commands"
    msg += "\n\t- Press 0 to exit"
    print(msg)

def readPhone():
    """
    Function used for reading the manufacturer and the model from the console.The user is asked to introduce
    both of them  and after that the information is verified.
    If the information is wrong, the user is asked to introduce it again.
    input:-
    output:x - a list containing the manufacturer and the model of the phone
    """
    x=[]
    manu=input("Please enter the manufacturer:")
    while len(manu)==0:
        print("\tInvalid manufacturer!")
        manu = input("Please enter the manufacturer:")

    model=input("Please enter the model of the phone:")
    while len(model)==0:
        print("Invalid model!")
        model = input("Please enter the model of the phone:")

    x.append(manu)
    x.append(model)
    return x

def readCommand(l):
    """
    Function used for reading the command introduced by the user.Until the user has introduced the value 0 ( exit app) , can introduce
    commands.Firstly the menu with available commands is printed, then for each commands it is called the specific function from Operations module.
    input:l-the list with all the phones
    output:- modified list

    """
    printMenu()
    keepAlive=True
    while keepAlive==True:
        cmd=input("\nPlease enter your command:")
        if cmd =="1":
            x=readPhone()

            price = input("Enter the price of the phone:")
            while price.isdigit() == False:
                print("Invalid price! The price must be a natural number.")
                price = input("Enter the price of the phone:")

            x.append(price)

            if len(x[0])<3 or len(x[1])<3 or len(x[2])<3:
                print("One of the field has the lenght less than 3 characters!")
            else:
                l=addPhone(x[0],x[1],x[2],l,0)

        elif cmd=="2":
            x = readPhone()
            l=removePhone(x[0],x[1],l,0)

        elif cmd=="3":
            x=readPhone()
            price = input("Enter the new price of the phone:")
            while price.isdigit() == False:
                print("Invalid price! The price must be a natural number.")
                price = input("Enter the new price of the phone:")
            x.append(price)
            l=updatePhone(x[0],x[1],x[2],l,0)

        elif cmd=="4":
            sortedPhone(l)

        elif cmd=="5":
            listAll(l)

        elif cmd=="6":
            printMenu()

        elif cmd=="0":
            print("Goodbye! :)")
            sys.exit()

        else:
            print("Invalid command")

l=[]
l=Tests()
l=addElements(l)
readCommand(l)
