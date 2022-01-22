import os
adm=[{"user":"a","pass":0},
     {"user":"b","pass":1}]

pasnger=[{"pasnId":100,"user":"ram","pass":123,"wallet":5000},
         {"pasnId":101,"user":"raj","pass":456,"wallet":7000}]
ID=[100,101]

t={"xxx":0,"yyy":0}

cost={"xxx":750,"yyy":500}

acc=[{"Acc.no":111,"pass":123,"balance":15000},
     {"Acc.no":222,"pass":456,"balance":20000}]

Trains=[{"xxx":{"cbe":1,"Tup":2,"Erode":3,"villupuram":4,"chennai":5}},
       {"yyy":{"salem":1,"Erode":2,"Tup":3,"cbe":4}}]


s={}

wait=[]


def addRoutes():
    os.system("cls")
    d={}
    k={}
    x=input("Enter new Train name:")
    y=int(input("Enter number of routes:"))
    print()
    for i in range(1,y+1):
        c=input("Enter"+str(i)+"st Junction name:")
        k[c]=i
    d[x]=k
    Trains.append(d)
    t[x]=0
    print()
    print("New Train and Routes are Added!")
    

def seatAvail():
    os.system("cls")
    for i in Trains:
        for j,k in i.items():
            seats=[]
            print()
            x=int(input("Enter seat Availabilty of Train"+" "+j+":"))
            t[j]+=x
            for p in range(x):
                l=[0 for r in range(len(k))]
                seats.append(l)
            for i in seats:
                print(*i)
            print("Seat Availability of Train"+" "+j+" "+"is updated!")
            s[j]=seats
            
        
    

def admin():
    os.system("cls")
    n = input("Enter user name:")
    p = int(input("Enter pass:"))
    for i in adm:
        if i["user"]==n and i["pass"]==p:
            print("Welcome Admin!")
            while(True):
                c = int(input("""\t\n1.Add Routes/stations \n2.Seat Availability \n3.Exit \nEnter choice:"""))
                if c==1:
                    addRoutes()
                elif c==2:
                    seatAvail()
                elif c==3:
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Invalid choice")
                    break
            break
    else:
        print("Incorrect username/pass")


def bookTickets(i):
    os.system("cls")
    n=int(input("Enter number of Tickets:"))
    x=input("Enter Train name:")
    se=s[x]
    amt=0
    b=i["wallet"]
    if b>(n*cost[x]):
        amt+=(n*cost[x])
        for p in range(n):
            print()
            st,ed=map(int,input("Enter st&ed value for person"+" "+str(p+1)+":").split())
            for q in range(t[x]):
                if sum(se[q][st-1:ed-1])==0:
                    print("Seat Allocated for person"+" "+str(p+1)+" "+"is",q+1)
                    for h in range(st-1,ed): 
                        se[q][h]=i["pasnId"]
                    break
            else:
                wait.append([i["pasnId"],st,ed])
                print()
                print("Seat not Available")
        b-=amt
        i["wallet"]=b
        print("The Tickets costs",amt,"The waiting lists if cancelled will be refunded....")
    else:
        print("No available balance in wallet...")
    print(wait)
    for m in se:
        print(*m)
    


def cancelTickets(i):
    os.system("cls")
    n=int(input("Enter number of cancelling Tickets:"))
    x=input("Enter Train name:")
    se=s[x]
    amt=(n*cost[x])
    b=i["wallet"]
    b+=amt
    i["wallet"]=b
    for p in range(n):
        print()
        if len(wait)!=0:
            st,ed=map(int,input("Enter st&ed cancellation value for person"+" "+str(p+1)+":").split())
            for h in wait:
                if h[-2]>=st and h[-1]<=ed:
                    wait.remove(h)
                    for q in range(t[x]):
                        if se[q][st-1]==i["pasnId"] and se[q][ed-1]==i["pasnId"]:
                            for j in range(st-1,ed):
                                se[q][j]=h[0]
                            print("Waiting list updated!")
                            break
        elif len(wait)==0:
            st,ed=map(int,input("Enter st&ed cancellation value for person"+" "+str(p+1)+":").split())
            for q in range(t[x]):
                if se[q][st-1]==i["pasnId"] and se[q][ed-1]==i["pasnId"]:
                    for j in range(st-1,ed):
                        se[q][j]=0
                    print("No waiting list")
                    break
            
        print(wait)
    


def viewTrain(i):
    os.system("cls")
    for p in Trains:
        for j,k in p.items():
            print()
            print(j,k)
            while(True):
                c=int(input("""\t\n1.View seats \n2.Book Tickets \n3.Exit \nEnter choice:"""))
                if c==1:
                    print("seats Availabilty")
                    for d in s:
                        if d==j:
                            for e in range(t[j]):
                                print(*s[d][e])
                elif c==2:
                    bookTickets(i)
                elif c!=3 and c!=2 and c!=1:
                    os.system("cls")
                    print("Invalid choice")
                    break
                elif c==3:
                    os.system("cls")
                    break
                    

def wallet(i):
    os.system("cls")
    x=int(input("Enter Acc.no:"))
    y=int(input("Enter pass:"))
    z=int(input("Enter Amount of transfer:"))
    for j in acc:
        b=j["balance"]
        if z<b:
            if j["Acc.no"]==x and j["pass"]==y:
                b-=z
                j["balance"]=b
                i["wallet"]=z
                print("Amount Transferred Successfully!")
                break
        else:
            print("Amount not available...")
    else:
        print("Account Not found...")
    print(acc)


def passenger():
    os.system("cls")
    while(True):
        v=int(input("""\t\n1.new user \n2.Existing user \n3.Exit \nEnter choice:"""))
        if v==1:
            os.system("cls")
            d={}
            e={}
            r=[]
            x=input("Enter username:")
            y=int(input("Enter password:"))
            a=int(input("Enter Acc.no:"))
            for i in pasnger:
                if i["user"]==x:
                    r.append(i)
            if len(r)==0:
                k=ID[-1]+1
                d["pasnId"]=k
                d["user"]=x
                d["pass"]=y
                d["wallet"]=0
                e["Acc.no"]=a
                e["pass"]=y
                e["balance"]=10000
                pasnger.append(d)
                acc.append(e)
                print("New user Created!")
                print(pasnger)
                print(acc)
            else:
                print("Username Available...Try with other name")
        elif v==2:
            os.system("cls")
            x=input("Enter username:")
            p=int(input("Enter pass:"))
            for i in pasnger:
                if i["user"]==x and i["pass"]==p:
                    print("Welcome"+" "+i["user"]+"!")
                    while(True):
                        l=int(input("""\t\n1.Book Tickets \n2.Cancel Tickets \n3.view Train Availabity \n4.Add wallet amount \n5.check balance \n6.Exit \nEnter choice:"""))
                        if l==1:
                            bookTickets(i)
                        elif l==2:
                            cancelTickets(i)
                        elif l==3:
                            viewTrain(i)
                        elif l==4:
                            wallet(i)
                        elif l==5:
                            os.system("cls")
                            print("Balance is ",i["wallet"])
                        elif l==6:
                            os.system("cls")
                            break
                        else:
                            os.system("cls")
                            print("Invalid choice")
                            break
                    break
            else:
                os.system("cls")
                print("No user exists...")
        elif v==3:
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Invalid choice")
            break


while(True):
    x=int(input("""\t\n1.Admin \n2.Passenger \n3.Exit \nEnter choice:"""))
    if x==1:
        admin()
    elif x==2:
        passenger()
    elif x==3:
        os.system("cls")
        break
    else:
        os.system("cls")
        print("Invalid choice")
        break