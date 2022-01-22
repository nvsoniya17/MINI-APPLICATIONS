import os
ven =[{"sellId":1000,"ven":"sam","pass":"1708"},
      {"sellId":1001,"ven":"som","pass":"1911"}]
cus =[{"cusId":200,"cus":"Tom","pass":"3005","wallet":500},
      {"cusId":201,"cus":"Tim","pass":"2610","wallet":200}]
pro =[{"proId":100,"sellId":1000,"pro":"pencil","price":10,"Discount":"2%","stock":50},
      {"proId":101,"sellId":1000,"pro":"pen","price":20,"Discount":"3%","stock":50},
      {"proId":102,"sellId":1000,"pro":"notebook","price":30,"Discount":"3%","stock":50},
      {"proId":100,"sellId":1001,"pro":"pencil","price":10,"Discount":"2%","stock":50},
      {"proId":102,"sellId":1001,"pro":"notebook","price":50,"Discount":"2%","stock":90},
      {"proId":101,"sellId":1001,"pro":"pen","price":20,"Discount":"3%","stock":50},]

proD ={"pencil":100,"pen":101,"notebook":102,"ruler":103,"Eraser":104,"sharpner":105}

wltm =[{"pass":"3005","Acc no.":1234,"balance":5000},
       {"pass":"2610","Acc no.":5678,"balance":10000}]

rev=[]
crt=[]
mo=[]

adm = [{"user":"a","pass":0},
       {"user":"b","pass":1}]
order =[]
new =[] 
l=[1000,1001]

def add_remove():
    os.system("cls")
    global ven
    y = ven
    ven=[]
    for i in y:
        print(i)
        c =int(input("""\t\n1.keep \n2.discard \n3.Exit \nEnter choice:"""))
        if c==1:
            ven.append(i)
        elif c==2:
            y.remove(i)
        elif c==3:
            os.system("cls") 
            break
        else:
            print("Invalid choice")
            break
    print(ven)
    
    
def approve():
    os.system("cls")
    global new
    n = new
    new=[]
    if len(n)!=0:
        f = int(input("""\t\n1.Check \nEnter choice:"""))
        if f==1:
            for i in n:
                print(i)
                c =int(input("""\t\n1.keep \n2.discard \n3.Exit \nEnter choice:"""))
                if c==1:
                    ven.append(i)
                elif c==2:
                    l.remove(i["sellId"])
                    del i
                elif c==3:
                    os.system("cls")
                    break
                else:
                    print("Invalid choice")
        else:
            os.system("cls")
            print("Invalid choice")
    else:
        print("No new vendors")
    
def addproD():
    os.system("cls")
    global proD
    x = input("Enter New product:")
    c = list(proD.values())
    k = c[-1]+1
    if x not in list(proD.keys()):
        proD[x]=k
    else:
        print("product Already Available")
    
    print(proD)
    
def admin():
    os.system("cls")
    p = input("Enter user name:")
    q = int(input("Enter pass:"))
    for i in adm:
        if i["user"]==p and i["pass"]==q:
            print("\t Welcome Admin")
            while(True):
                x = int(input("""\t\n1.Add/Remove vendor \n2.Approve \n3.Add proD \n4.Exit \nEnter choice:"""))
                if x==1:
                    add_remove()
                elif x==2:
                    approve()
                elif x!=3 and x!=2 and x!=1 and x!=4:
                    os.system("cls")
                    print("Invalid choice")
                    break
                elif x==3:
                    addproD()
                elif x==4:
                    os.system("cls")
                    break
            break
    else:
        print("Invalid user/pass")

    
def changeprice(j):
    x=int(input("Enter new Price:"))
    j["price"]=x
    print(j)
    print("Changes saved!")
    
    
def changeDis(j):
    y = input("Enter New Discount:")
    j["Discount"]=y
    print(j)
    print("Changes saved!")
    
    
def changestock(j):
    z = int(input("Enter new stock:"))
    j["stock"]=z
    print(j)
    print("Changes saved!")

        
def product(i):
    while(True):
        k = int(input("""\t\n1.Add_product \n2.Edit product details \n3.Exit \nEnter choice:"""))
        if k==1:
            d={}
            v=[]
            b = list(proD.keys())
            os.system("cls")
            x=int(input("Enter sellerId:"))
            y=input("Enter Product name:")
            for j in pro:
                if j["sellId"]==x and j["pro"]==y:
                    v.append(j)
            if len(v)==0:
                if y in b:
                    p=int(input("Enter price of product:"))
                    dis=input("Enter discount in %:")
                    st=int(input("Enter stock:"))
                    d["proId"]=proD[y]
                    d["sellId"]=i["sellId"]
                    d["pro"]=y
                    d["price"]=p
                    d["Discount"]=dis
                    d["stock"]=st 
                    pro.append(d)
                    print("Product Added Successfully!")
                    print()
                    print(pro)
            else:
                print("Product Already added!")
        elif k==2:
            os.system("cls")
            f = int(input("Enter Product ID:"))
            for j in pro:
                if j["sellId"]==i["sellId"] and j["proId"]==f:
                    v = int(input("""\t\n1.Change price \n2.change Discount \n3.change stock \n4.Exit \nEnter choice:"""))
                    if v==1:
                        changeprice(j)
                    elif v==2:
                        changeDis(j)
                    elif v==3:
                        changestock(j)
                    elif v==4:
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
                        print("Invalid choice")
                        break
                    break
        elif k==3:
            os.system("cls")
            break
        
        
        

def vreview(i):
    global rev
    for j in rev:
        if j["sellId"]==i["sellId"]:
            print(j)

def sales(i):
    for j in mo:
        if j["sellId"]==i["sellId"]:
            y=j["stock"]
            y-=1
            j["stock"]=y
            print(j)

def compare(i):
    os.system("cls")
    global pro
    print(pro)
    print()
    y=[]
    x = int(input("Enter product ID:"))
    for j in pro:
        if j["sellId"]!=i["sellId"] and j["proId"]==x:
            y.append(j)
    if len(y)!=0:
        print(*y,sep="\n")
    else:
        print("No other sellers of this product")

def new_user():
    os.system("cls")
    d={}
    n = input("Enter new user name:")
    k = input("Enter new user pass:")
    m=int(l[-1]+1)
    d["sellId"]=m
    d["ven"]=n
    d["pass"]=k
    print(d)
    l.append(d["sellId"])
    new.append(d)
    print(l)
    print("Account sent for verification")
            
        
def vendor():
    while(True):
        x =int(input("""\t\n1.New user \n2.Existing user \n3.Exit \nEnter choice:""" ))
        if x==1:
            new_user()
        elif x==2:
            os.system("cls")
            y = input("Enter Name:")
            z = input("Enter pass:")
            for i in ven:
                if i["ven"]==y and i["pass"]==z:
                    print("Welcome",i["ven"])
                    while(True):
                        c = int(input("""\t\n1.Product \n2.Review \n3.sales \n4.compare \n5.Exit \nEnter Choice:"""))
                        if c==1:
                            product(i)
                        elif c==2:
                            vreview(i)
                        elif c==3:
                            sales(i)
                        elif c==4:
                            compare(i)
                        elif c==5:
                            os.system("cls")
                            break
                        else:
                            os.system("cls")
                            print("Invalid choice")
                            break
                    break
            else:
                print("No Account Available")
        elif x==3:
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Invalid user")
            break
        
    
 
def cart(i,o):
    os.system("cls")
    print(crt)
    print()
    for j in crt:
        print(j)
        x=int(input("""\t\n1.place the order \n2.remove \n3.Exit \nEnter choice:"""))
        if x==1:
            os.system("cls")
            y = i["wallet"]
            z = j["price"]
            if z<y:
                y-=z
                i["wallet"]=y
                o.append(j)
                mo.append(j)
                print("Order Placed successfully!")
            else:
                print("No available balance in wallet")
            break
        elif x==2:
            crt.remove(j)
        elif x==3:
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Invalid choice")
            break
 
    
def search(i,o):
    os.system("cls")
    global crt
    os.system("cls")
    x = input("Enter product name:")
    for j in pro:
        if j["pro"]==x:
            os.system("cls")
            for k,m in j.items():
                print(k,"-",m)
            c = int(input("""\t\n1.Add to cart \n2.place the order \n3.Exit \nEnter choice:"""))
            if c==1:
                if j not in crt:
                    crt.append(j)
                    print("Added to cart!")
            elif c==2:
                os.system("cls")
                y = i["wallet"]
                z = j["price"]
                if z<y:
                    y-=z
                    i["wallet"]=y
                    o.append(j)
                    mo.append(j)
                    print("Order placed successfully!")
                else:
                    print("No available balance in wallet")
                break
            elif c==3:
                os.system("cls")
                break
            else:
                os.system("cls")
                print("Invalid choice")
                break
    else:
        print("NO other sellers")


def Filter(i):
    os.system("cls")
    c=[]
    x=input("Enter product name:")
    y,z=map(int,input("Enter price range:").split())
    for k in pro:
        if k["pro"]==x:
            if k["price"]<z and k["price"]>y:
                c.append(k)
    print(c)
    input("Press Enter to continue....")
    print()
    for j in c:
        print(j)
        f = int(input("""\t\n1.place the order \n2.Add to cart \n3.Exit \nEnter choice:"""))
        if f==1:
            os.system("cls")
            y = i["wallet"]
            z = j["price"]
            if z<y:
                y-=z
                i["wallet"]=y
                o.append(j)
                mo.append(j)
                print("Order placed successfully!")
            else:
                print("No available balance in wallet")
                break
        elif f==2:
            if j not in crt:
                crt.append(j)
        elif f==3:
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Invalud choice")
            break


def myorders(o):
    os.system("cls")
    for j in o:
        print(j)


def wlt(i):
    os.system("cls")
    x=int(input("Enter amount of transfer:"))
    z = int(input("Enter acc no.:"))
    p = input("Enter pass:")
    y=i["wallet"]
    for j in wltm:
        if j["Acc no."]==z and j["pass"]==p:
            if x<j["balance"]:
                y+=x
                i["wallet"]=y
    print(i)
    
 
def creview(i,o):
    os.system("cls")
    d={}
    d["cus"]=i["cus"]
    for j in o:
        print(j)
        x=int(input("""\t\n1.Add review \n2.Exit \nEnter choice:"""))
        if x==1:
            y=input("Add your Review:")
            d["proId"]=j["proId"]
            d["pro"]=j["pro"]
            d["sellId"]=j["sellId"]
            d["Review"]=y
            rev.append(d)
        elif x==2:
            os.system("cls")
            break
    
 
    
def cust():
    while(True):
        x =int(input("""\t\n1.New user \n2.Existing user \n3.Exit \nEnter choice:""" ))
        if x==1:
            os.system("cls")
            d={}
            r=[]
            e={}
            n = input("Enter new user name:")
            p= input("Enter pass:")
            a=int(input('Enter new Acc no.:'))
            c=0
            for i in cus:
                if i["cus"]==n:
                    r.append(i)
            if len(r)==0:
                d["cus"]=n
                d["pass"]=p
                d["wallet"]=c
                cus.append(d)
                print(cus)
                print("New customer created!")
                e["pass"]=p
                e["Acc no."]=a
                e["balance"]=10000
                wltm.append(e)
            else:
                print("User Already Exists...please try with other name")
            
        elif x==2:
            os.system("cls")
            y = input("Enter Name:")
            z = input("Enter pass:")
            for i in cus:
                if i["cus"]==y and i["pass"]==z:
                    print("Welcome",i["cus"])
                    o=[]
                    while(True):
                        c = int(input("""\t\n1.search \n2.Filter \n3.cart \n4.myorders \n5.wallet \n6.Add review \n7.check balance \n8.Exit \nEnter Choice:"""))
                        if c==1:
                            search(i,o)
                        elif c==2:
                            Filter(i)
                        elif c==3:
                            cart(i,o)
                        elif c==4:
                            myorders(o)
                        elif c==5:
                            wlt(i)
                        elif c==6:
                            creview(i,o)
                        elif c==7:
                            print("Balance is",i["wallet"])
                        elif c==8:
                            os.system("cls")
                            break
                        else:
                            os.system("cls")
                            print("Invalid choice")
                            break
                    break
            else:
                print("No Account Available")
        elif x==3:
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Invalid user")
            break

while(True):
    print("\tAMAZON")
    x = int(input(""" \t\n1.ADMIN \n2.VENDOR \n3.CUSTOMER \n4.Exit \nEnter choice:"""))
    if x==1:
        admin()      
    elif x==2:
        vendor()
    elif x==3:
        cust()
    elif x==4:
        os.system("cls")
        break
    else:
        os.system("cls")
        print("Invalid choice")