import os
from datetime import datetime
amt = {2000:0,500:0,200:0,100:0}
customers =[{"ACC no.":123,"user":"jai","pass":"0903","balance":30000,"Bank":"KVB","Mobile no.":9487484736,"l":0},
            {"ACC no.":456,"user":"raj","pass":"8008","balance":40000,"Bank":"IOB","Mobile no.":8695552731,"l":0},
            {"ACC no.":789,"user":"ram","pass":"4488","balance":50000,"Bank":"SBI","Mobile no.":7339255734,"l":0}]
Transaction = []
OTP = [123,234,456,678]

def pinchange(i):
    m = i["Mobile no."]
    x = int(input("Enter your Mobile Number:"))
    if x==m:
        print("OTP sent")
        y = int(input("Enter OTP:"))
        if y in OTP:
            p = input("Enter New Pin:")
            i["pass"]=p
    else:
        print("Invalid mobile num")
    

def drtDepo(i):
    d={}
    da = datetime.now()
    p = da.strftime("%d/%m/%Y   %H:%M:%S")
    d["DateTime"]=p
    d["user"]=i["user"]
    d["Total Balance"]=i["balance"]
    d["Withdrawed/T/D"] = 0
    d["Balance"]=0
    x = int(input("Enter Amt of Deposit:"))
    y = i["balance"]
    b = list(amt.keys())
    if x<y and x%100==0:
        m = 0
        for j in amt:
            k = int(input("Enter count of"+str(j)+":"))
            m+=(k*j)
            if j==b[-1] and m<x:
                print("Please check correct denomination")
                break
            elif m==x:
                if k>=amt[j]:
                    amt[j]+=k
                    continue
            elif m>x: 
                print("Denomination exceeded")
                break
        else:
            y+=x
            d["Withdrawed/T/D"]=x
            i["balance"]=y
            d["Balance"]+=i["balance"]
            print("Amt Deposited successfully!")
    Transaction.append(d)

def amtTransfer(i):
    d={}
    da = datetime.now()
    p = da.strftime("%d/%m/%Y   %H:%M:%S")
    d["DateTime"]=p
    d["user"]=i["user"]
    d["Total Balance"]=i["balance"]
    d["Withdrawed/T/D"] = 0
    d["Balance"]=i["balance"]
    x = int(input("Enter ACC no.:"))
    y = int(input("Enter amt of Transfer:"))
    for j in customers:
        if j["ACC no."]==x:
            s = i["balance"]
            r = j["balance"]
            if s>y:
                s-=y
                d["Withdrawed/T/D"] = y
                i["balance"]=s
                r+=y
                j["balance"]=r
                d["Balance"] =i["balance"]
                print("Amount Transferred successfully!")
                break
            else:
                print("No enough amt available")
                break
    else:
        os.system("cls")
        print("Invalid user")
    Transaction.append(d)
                

def statement():
    if len(Transaction)>=6:
        print("Date","\t\tTime","\t  User","\t  Total Balance","\t Withdrawed amt/T/D","\t Available Balance")
        for i in Transaction:
            print(i["DateTime"],"\t","",i["user"],"\t\t",i["Total Balance"],"\t\t\t",i["Withdrawed/T/D"],"\t\t\t",i["Balance"])
    else:
        print("Not more than 6 Transactions Done")
    
def addamt():
    os.system("cls")
    for i in amt:
        x = int(input("Enter num of"+str(i)+":"))
        amt[i]+=x
    print("\tAmount added successfully!")
    
def checkamt():
    os.system("cls")
    t = 0
    for i in amt:
        print(i,"--",amt[i])
        t += (amt[i]*i)
    print("Total amt:",t)
        
def withdraw(i):
    d={}
    da = datetime.now()
    p = da.strftime("%d/%m/%Y   %H:%M:%S")
    d["DateTime"]=p
    d["user"]=i["user"]
    d["Total Balance"]=i["balance"]
    d["Withdrawed/T/D"] = 0
    d["Balance"]=i["balance"]
    x = int(input("Enter Withdrawal amount:"))
    y = i["balance"]
    z = amt.values()
    b = list(amt.keys())
    if all(z)==0:
        print("NO amount in ATM")
    elif x<y and x<10000 and x%100==0 :
        m = 0
        for j in amt:
            k = int(input("Enter count of"+str(j)+":"))
            m+=(k*j)
            if j==b[-1] and m<x:
                print("Please check correct denomination")
                break
            elif m==x:
                if k<=amt[j]:
                    amt[j]-=k
                else:
                    print("Denomination not available") 
                    break   
            elif m>x:
                print("Denomination exceeded")
                break
        else:
            d["Withdrawed/T/D"] += x
            y-=x 
            i["balance"] = y
            d["Balance"] = i["balance"]
            print("Available Balance after withdrawal:",y)
    elif x%100!=0:
        print("Invalid amt")
    else:
        print("Amount is more than daily limit")
    Transaction.append(d)
        
    
    

def checkbalance(i):
        print("Balance is:",i["balance"])
    
def admin():
    l = ["XYZ","PQR","ABC"]
    d = {"XYZ":1,"PQR":2,"ABC":3}
    os.system("cls")
    x = input("Enter userName:")
    if x in l:
        y = int(input("Enter Password:"))
        if y==d[x]:
            os.system("cls")
            print("Welcome Admin")
            while(True):
        
                z = int(input(""" \t\n1.Addamount \n2.checkbalance \n3.Exit \nEnter choice:"""))
                if z==1:
                    addamt()
                elif z==2:
                    checkamt()
                elif z==3:
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Invalid Input")
                    break
        
        else:
            os.system("cls")
            print("Invalid pass")
    else:
        os.system("cls")
        print("Invalid user")

        
        
def cust():
    os.system("cls")
    x  = input("Enter UserName:")
    y = input("Enter password:")
    for c in customers:
        if c["user"]==x and c["pass"]==y:
            print("Welcome",c["user"])
            d={}
            da = datetime.now()
            p = da.strftime("%d/%m/%Y   %H:%M:%S")
            y = c["balance"]
            d["DateTime"]=p
            d["user"]=c["user"]
            d["Total Balance"]=y
            d["Withdrawed/T/D"] = 0
            d["Balance"]=c["balance"]
            i = c
            i["l"]+=1
            if i["l"]>2 and i["Bank"]!="KVB":
                y=y-50
                i["balance"]=y
                d["Withdrawed/T/D"] = 50
                d["Balance"]-=50
            Transaction.append(d)
            while(True):       
                z = int(input("""\n1.Withdraw \n2.checkBalance \n3.pinChange \n4.Transactions \n5.Direct Deposit \n6.Amount Transfer \n7.Exit \nEnter choice:"""))
                os.system("cls")
                if z==1:
                    withdraw(i)
                elif z==2:
                    checkbalance(i)
                elif z==3:
                    pinchange(i)
                elif z==4:
                    statement()
                elif z==5:
                    drtDepo(i)
                elif z==6:
                    amtTransfer(i)
                elif z==7:
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    break
            break
    else:
        os.system("cls")
        print("Invalid user")
        c["l"]+=1
        if c["l"]>2:
            print("Attempt exceeded")
                
    
    
while(True):
    print("\tATM MACHINE")
    x = int(input("""\t\n1.ADMIN \n2.CUSTOMER \n3.EXIT \nENTER CHOICE:"""))
    if x==1:
        admin()
    elif x==2:
        cust()
    elif x==3:
        os.system("cls")
        exit()
    else:
        print("Invalid Input")
        os.system("cls")
        continue