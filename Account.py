

class Account():

    def __init__(self, _name , _amount , _id):
       self.name=_name
       self.amount=_amount
       self.id=_id
    
    def __str__(self):
        return (f'Name:{self.name}\nAmount:{self.amount}\nID:{self.id}')

    def accountDataDic(self):
        return {"Name":self.name,"Amount":self.amount,"ID":self.id}

    def dictionaryToObject(self,dic):
        return Account(dic["Name"],dic["Amount"],dic["ID"])

    def withdraw(self):
        a=int(input("how much?"))
        if(self.amount>a):
            self.amount-=a
            print("succesfuly")
        else:print("you don't have enough money")

    def deposit(self):
        self.amount+=int(input("how much?"))
        print("succesfuly")
