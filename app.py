import os as nt
from Bank import Bank


def main():
    nt.system('cls')
    myBank=Bank()
    myBank.loadFromFiletolist()
    while(True):
        print("-------------------------")
        print("a----add account")
        print("s----search account")
        print("p----print all accounts")
        print("p2----print how many members")
        print("c----close your account")
        print("w----withraw")
        print("d----deposit")
        print("x----exit")
        userselection=input("enter your choise")
        nt.system('cls')
        if(userselection=='x'):
            myBank.savetoFileFromlistAndCounter()
            return
        if(userselection=='a'):
            myBank.addaccountToBank(input("name?"),int(input("amount")))
        if(userselection=='p2'):myBank.printhowmanymembers()
        if(userselection=='p'):myBank.printAllmembers()
        if(userselection=='c'):myBank.closeAccountOrSearching(int(input("ID ??")))
        if(userselection=='w'):(myBank.closeAccountOrSearching(int(input("ID ??")),True)).withdraw()
        if(userselection=='d'):(myBank.closeAccountOrSearching(int(input("ID ??")),True)).deposit()
        if(userselection=='s'):print(myBank.closeAccountOrSearching(int(input("ID ??")),True))
        if(userselection=='t'):print(Bank.i)

      




if   __name__ == '__main__':
    main()



