import json
from Account import Account

class Bank():
    accounts=[]
    id=0
    i=0
    
    def __init__(self):
        Bank.i+=1

    def closeAccountOrSearching(self,idid, x=False):
        s=0
        for a in self.accounts:
            if a.id==idid:
                s+=1
                if x==True:
                    return a
                else:
                    self.accounts.remove(a)
                    print("succes")  
        if s==0:print("I can't find this account...")            
        
        
    def loadFromFiletolist(self):
        listdata=[]
        try:
            with open("AcoountsAndID.json" ,"r") as f:
                listdata=json.load(f)
        except FileNotFoundError:
            print("I cant fint the file") 
            return []
        except:
            print("I don't know what the fuck")  
            return []  
        else:
            self.id=listdata[-1]
            listdata.remove(self.id)
            for acc in listdata:self.accounts.append(Account(acc["Name"],acc["Amount"],acc["ID"]))
            print("Loading Data succesfuly")
        finally:print("Let's go")

    def savetoFileFromlistAndCounter(self):
        newlist=[]
        for acc in self.accounts:newlist.append(acc.accountDataDic())
        newlist.append(self.id)
        with open("AcoountsAndID.json", "w") as f:
            json.dump(newlist, f)

    def addaccountToBank(self, _name , _amount):
        if(_amount<100):return
        if(len(_name)<3):_name="Dan"
        self.id+=1
        self.accounts.append(Account(_name,_amount,self.id))

    def printhowmanymembers(self):
        print( len(self.accounts))
    
    def printAllmembers(self):
        if self.accounts==[]:print("NO ACCOUNTS!")
        else:
            for x in self.accounts:
                print("-------------------------")
                print(x)

