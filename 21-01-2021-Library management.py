import os
from datetime import timedelta,date

adm=[{"user":"admin1@gmail.com","pass":0},
     {"user":"admin2@gmail.com","pass":1}]


br=[{"user":"br1@gmail.com","name":"ram","pass":1,"books_br":[],"fines":0,"wallet":1500},
    {"user":"br2@gmail.com","name":"raj","pass":2,"books_br":[],"fines":0,"wallet":1500}]

bo={"Harry potter":450,"Peaks and valleys":500,"Sherlock homes":750}

cart=[]

books=[{"ISBN no.":100,"name":"Harry potter","count":30,"brcount":0,"cost":450,"lostcount":0},
       {"ISBN no.":101,"name":"Peaks and valleys","count":20,"brcount":0,"cost":500,"lostcount":0},
       {"ISBN no.":102,"name":"Sherlock homes","count":4,"brcount":0,"cost":700,"lostcount":0}]

brbooks=[]


def addBorrower():
    os.system("cls")
    d={}
    r=[]
    print("\t----------Add New Borrower------------")
    x=input("Enter New user mail:")
    k=input("Enter name:")
    y=int(input("Enter password:"))
    for i in br:
        if i["user"]==x:
            r.append(i)
    if len(r)==0:
        d["user"]=x
        d["name"]=k
        d["pass"]=y
        d["books_br"]=[]
        d["fines"]=0
        d["wallet"]=1500
        br.append(d)
        print()
        print("Deposit Rs.1500 as initial deposit in Book bank...")
        input("Press Enter to continue...")
        print("\t----------New Borrower Added----------")
        for i in br:
            print("user mail : ",i["user"])
            print("User name: ",i["name"])
            print("Books Borrowed: ",i["books_br"])
            print("Fines: ",i["fines"])
            print("Wallent balance: ",i["wallet"])
            print("\t--------------------")
    else:
        os.system("cls")
        print("Mail Already Available...")
    input("press Enter to continue...")
    os.system("cls")
    

def addadm():
    os.system("cls")
    d={}
    r=[]
    print("\t----------Add New Admin------------")
    x=input("Enter New Admin mail:")
    y=int(input("Enter password:"))
    for i in adm:
        if i["user"]==x:
            r.append(i)
    if len(r)==0:
        d["user"]=x
        d["pass"]=y
        d["books_br"]=0
        adm.append(d)
        print("\t----------New Admin Added----------")
        for i in adm:
            print("user : ",i["user"])
            print("\t--------------------")
    else:
        print("Mail Already available....")
    input("press Enter to continue...")
    os.system("cls")


def addbook():
    os.system("cls")
    f={}
    k=[100,101,102]
    x=input("Enter New Book name:")
    c=int(input("Enter count of book:"))
    p=int(input("Enter price of book:"))
    f["ISBN no."]=k[-1]+1
    k.append(k[-1]+1)
    f["name"]=x
    f["count"]=c
    f["brcount"]=0
    f["cost"]=p
    f["lostbook"]=0
    books.append(f)
    bo[x]=p
    print("Book Added Successfully!")
    for i in books:
        print("\t---------------------")
        print("ISBN no.:",i["ISBN no."])
        print("Book: ",i["name"])
        print("Count: ",i["count"])
        print("\t---------------------")
    input("Press Enter to continue...")
     


def bookreport():
    os.system("cls")
    borrowcount=[]
    for i in books:
        borrowcount.append(i["brcount"])
    m2=max(borrowcount)
    while(True):
        c=int(input("""\t\n1.Books with less quantity \n2.Books not borrowed \n3.Books Borrowed many times \n4.Exit \nEnter choice:"""))
        if c==1:
            os.system("cls")
            for i in books:
                if i["count"]<5:
                    print("\t---------------")
                    print("ISBN no.: ",i["ISBN no."])
                    print("Book name: ",i["name"])
                    print("Book count: ",i["count"])
                    print("Borrowed Books: ",i["brcount"])
                    print("\t---------------")
            input("Press Enter to continue...")
        elif c==2:
            os.system("cls")
            for i in books:
                if i["brcount"]==0:
                    print("\t---------------")
                    print("ISBN no.: ",i["ISBN no."])
                    print("Book name: ",i["name"])
                    print("Book count: ",i["count"])
                    print("Borrowed Books: ",i["brcount"])
                    print("\t---------------")
            input("Press Enter to continue...")
        elif c==3:
            os.system("cls")
            for i in books:
                if i["brcount"]==m2:
                    print("\t---------------")
                    print("ISBN no.: ",i["ISBN no."])
                    print("Book name: ",i["name"])
                    print("Book count: ",i["count"])
                    print("Borrowed Books: ",i["brcount"])
                    print("\t---------------")
            input("Press Enter to continue...")
        elif c==4:
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Invalid choice")
            break
                             


def view():
    os.system("cls")
    while(True):
        x=int(input("""\t\n1.sorted by ISBN \n2.Sorted Alphabetically \n3.sorted by count \n4.Exit \nEnter choice:"""))
        if x==1:
            os.system("cls")
            p=[]
            for i in books:
                p.append(i["ISBN no."])
            s=sorted(p)
            for j in s:
                print("\t------------")
                print("ISBN no.: ",j)
                for i in books:
                    if i["ISBN no."]==j:
                        print("Book: ",i["name"])
                        print("Book count: ",i["count"])
                        print("Borrowed count:",i["brcount"])
                        print("Lost count:",i["lostcount"])
                        break
                print("\t------------")
        elif x==2:
            os.system("cls")
            p=[]
            for i in books:
                p.append(i["name"])
            s=sorted(p)
            for j in s:
                print("\t------------")
                print("Book:",j)
                for i in books:
                    if i["name"]==j:
                        print("ISBN no.: ",i["ISBN no."])
                        print("Book count: ",i["count"])
                        break
                print("\t------------")
        elif x==3:
            os.system("cls")
            p=[]
            for i in books:
                p.append(i["count"])
            s=sorted(p)
            for j in s:
                print("\t------------")
                print("Book count:",j)
                for i in books:
                    if i["count"]==j:
                        print("ISBN no.:",i["ISBN no."])
                        print("Book :",i["name"])
                        break
                print("\t------------")
        elif x==4:
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Invalid choice")
            break
    input("Press Enter to continue...")
    

def bostatus():
    os.system("cls")
    x=int(input("Enter ISBN number:"))
    if len(brbooks)==0:
        print("No books borrowed")
    else:
        for i in brbooks:
            if i["ISBN num."]==x:
                print("\t---------------------")
                print("Borrowed user: ",i["user"])
                print("Book Borrowed: ",i["Book"])
                print("Borrowed Date: ",i["brdate"])
                print("Expected return date: ",i["redate"])
                print("\t----------------------")
    input("Press Enter to continue...")
    

def rebook():
    os.system("cls")
    t=input("Enter user mail:")
    u=int(input("Enter password:"))
    for i in brbooks:
        if i["mail"]==t and i["pass"]==u:
            if len(i["books_br"])!=0:
                b=i["books_br"].index(i["Book"])
                print()
                print(i["books_br"][b])
                k=input("Enter return date:")
                for j in cart:
                    p=(int(j["redate"][:2])-int(k[:2]))
                    if p<0:
                        i["fines"]+=(2**abs(p))
                        i["wallet"]-=(2**abs(p))
                        i["brcount"]-=1
                        i["count"]+=1
                        for m in books:
                            if m["name"]==i["Book"]:
                                m["brcount"]-=1
                                m["count"]+=1
                                break
                        for l in br:
                            if l["user"]==t and l["pass"]==u:
                                l["books_br"].remove(i["Book"])
                                l["fines"]+=(2**abs(p))
                                l["wallet"]-=(2**abs(p))
                                break
                        print("You have charged Rs.2/day for late return...")
                        print(p)
                        break
                else:
                    j["brcount"]-=1
                    j["count"]+=1
                    for n in books:
                        if n["name"]==i["Book"]:
                            n["brcount"]-=1
                            n["count"]+=1
                            break
                    for l in br:
                        if l["user"]==t and l["pass"]==u:
                            l["books_br"].remove(i["Book"])
                            break       
                    print("Returned within last date...")
            break
    else:
        print("No Books borrowed by user...")
    input("Press enter to continue...")
    
    
def rests():
    os.system("cls")
    t=input("Enter user mail:")
    u=int(input("Enter password:"))
    for i in brbooks:
        if i["mail"]==t and i["pass"]==u:
            if len(i["books_br"])!=0:
                b=i["books_br"].index(i["Book"])
                print()
                print(i["books_br"][b])
                q=int(input("""\t\n1.Book lost \n2.Membership card lost \n3.Exit \nEnter choice:"""))
                if q==1:
                    for j in cart:
                        s=j["Book"]
                        j["lostcount"]+=1
                        i["wallet"]-=(bo[s]//2)
                        i["fines"]+=(bo[s]//2)
                        j["count"]-=1
                        j["brcount"]-=1
                        for l in br:
                            if l["user"]==t and l["pass"]==u:
                                l["books_br"].remove(i["Book"])
                                l["fines"]+=(bo[s]//2)
                                l["wallet"]-=(bo[s])//2
                                break     
                        print("You have charged 50% cost of book for the loss")
                        break
                            
                elif q==2:
                    for l in br:
                        if l["user"]==t and l["pass"]==u:
                            l["wallet"]-=10
                            l["fines"]+=10
                            break
                    print("You have been charged Rs.10 for loss of membership card")
                elif q==3:
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Invalid choice")
                    break
            break
    else:
        print("No user Available")


def bobook():
    os.system("cls")
    t=input("Enter user mail:")
    u=int(input("Enter password:"))
    for i in br:
        if i["user"]==t and i["pass"]==u:
            q={}
            p=date.today()
            s=p+timedelta(days=15)
            if i["wallet"]>=500 and len(i["books_br"])<3:
                x=input("Enter book name:")
                if x not in i["books_br"]:
                    i["books_br"].append(x)
                    for j in books:
                        if j["name"]==x:
                            c=int(input("""\t\n1.Add to cart \n2.Exit \nEnter choice:"""))
                            if c==1:
                                q["books_br"]=i["books_br"]
                                q["mail"]=i["user"]
                                q["pass"]=i["pass"]
                                q["fines"]=i["fines"]
                                q["wallet"]=i["wallet"]
                                q["ISBN num."]=j["ISBN no."]
                                q["user"]=i["name"]
                                q["Book"]=j["name"]
                                q["lostcount"]=j["lostcount"]
                                q["count"]=j["count"]
                                q["brcount"]=j["brcount"]
                                q["brdate"]=p.strftime("%d/%m/%y")
                                q["redate"]=s.strftime("%d/%m/%y")
                                brbooks.append(q)
                                cart.append(q)
                                print("Book Added to cart...")
                                crt()
                            elif c==2:
                                os.system("cls")
                                break
                            else:
                                os.system("cls")
                                print("Invalid choice")
                                break
                            break
                    else:
                        os.system("cls")
                        print("No Book Available")
            break
    else:
        os.system("cls")
        print("No user Available...")
    input("Press Enter to continue...")


def crt():
    os.system("cls")
    p=date.today()
    s=p+timedelta(days=15)
    for k in cart:
        x=int(input("""\t\n1.Borrow book \n2.Exit \nEnter the choice:"""))
        if x==1:
            for j in books:
                if j["name"]==k["Book"]:
                    j["count"]-=1
                    j["brcount"]+=1
                    print("\t-------------")
                    print("BOOK: ",j["name"])
                    print("Borrowed on: ",p.strftime("%d/%m/%y"))
                    print("Expected Return date: ",s.strftime("%d/%m/%y"))
                    print("\t-------------")
                    break
        elif x==2:
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Invalid choice")
            break


def admin():
    os.system("cls")
    x=input("Enter mail:")
    y=int(input("Enter pass:"))
    for i in adm:
        if i["user"]==x and i["pass"]==y:
            os.system("cls")
            print("Welcome Admin!")
            while(True):
                print("\t------Admin------")
                z=int(input("""\t\n1.Add Borrowers \n2.Add Admins \n3.View books \n4.Book report \n5.Add books \n6.Book status \n7.Borrow book \n8.Return Book \n9.Lost status \n10.Exit \nEnter choice:"""))
                if z==1:
                    addBorrower()
                elif z==2:
                    addadm()
                elif z==3:
                    view()
                elif z==4:
                    bookreport()
                elif z==5:
                    addbook()
                elif z==6:
                    bostatus()
                elif z==7:
                    bobook()
                elif z==8:
                    rebook()
                elif z==9:
                    rests()
                elif z==10:
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Invalid choice")
                    break
            break
    else:
        os.system("cls")
        print("Invalid mail/pass")
        input("press enter to continue...")
        

def viewfines(i):
    for i in br:
        print("\t--------------------")
        print("user : ",i["name"])
        print("Books Borrowed: ",i["books_br"])
        print("Fines: ",i["fines"])
        print("Wallent balance:",i["wallet"])
    
        
def borbook(i):
    for j in br:
        if j["user"]==i["user"]:
            print("\t-------------------")
            print("Boorower:",i["name"])
            print("Borrowed books:",*j["books_br"])
            print("Fines:",j["fines"])
            print("Wallet:",j["wallet"])
            break
    else:
        print("User not available...")


def student():
    os.system("cls")
    x=input("Enter mail:")
    y=int(input("Enter pass:"))
    for i in br:
        if i["user"]==x and i["pass"]==y:
            os.system("cls")
            print("Welcome!")
            while(True):
                v=int(input("""\t\n1.view fines and Reasons \n2.Borrowed books \n3.Exit \nEnter choice:"""))
                if v==1:
                    viewfines(i)
                elif v==2:
                    borbook(i)
                elif v==3:
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    print("Invalid choice")
                    break
            break
    else:
        os.system("cls")
        print("No User Available...")
        input("press Enter to continue...")

while(True):
    x=int(input("""\t\n1.Admin \n2.Student \n3.Exit \nEnter choice:"""))
    if x==1:
        admin()
    elif x==2:
        student()
    elif x==3:
        os.system("cls")
        break
    else:
        os.system("cls")
        print("Invalid choice")
        break