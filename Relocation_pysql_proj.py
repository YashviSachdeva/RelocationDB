cusn=[]
import pymysql
conn = pymysql.connect(user='root', password='yashvivik',host='localhost')
cursor=conn.cursor()
print("_"*100)
print("RELOCATION SERVICES:Moving Made Easy!")
print("-"*100)
print("MS RELOCATION SERVICES PVT.LTD.")
query="drop database if exists MSRELO"
cursor.execute(query)
print("Moving to a new place? Let relocation services handle all the details so you can enjoy a stress-free move.")
      
print("Here’s what we typically cover:")

ch="y"
while ch=="y" or ch=="Y":
    
    print("1)CREATE RELO DATABASES")
    print("2)CREATE RELOCATION TABLE")
    print("3)INSERT RELOCATION DETAILS IN RELOCATION TABLE")
    print("4)PRINT RECORDS FROM RELOCATION TABLE")
    print("5)SEARCH CUSTOMERS NUMBER")
    print("6)DELETE RECORD IN RELOCATION TABLE")
    print("7)UPDATE RECORD IN RELOCATION TABLE")
    print("8)CREATE SERVICES TABLE")
    print("9)INSERT CUSTOMER DETAILS IN SERVICE TABLE")
    print("10)PRINT CUSTOMER DETAILS ALONG WITH DETAILS OF PRODUCT PURCHASE")
    print("_"*100)
    print(""*100)
    r=int(input("enter choice"))
    
    if r not in {1,2,3,4,5,6,7,8,9,10}:
        print("Invalid input. Please enter a valid number")
    if r==1:
        query="create database MSRELO"
        cursor.execute(query)
        print("Database MSRELO created successfully.")

    if r==2:
        query1="use MSRELO"
        cursor.execute(query1)
        query="create table RELOCATION (Custno integer primary key,custname char(30),origin char(40), DOD Date, Weight integer)"
        cursor.execute(query)
        print("Table RELOCATION created successfully.")
        conn.commit()
        

    if r==3:
        query="use MSRELO"
        cursor.execute(query)
        lol=int(input("enter how many values"))
        for i in range (lol):
            scustno=int(input("enter customer no"))
            cusn.append(scustno)
            scustname=input("enter name")
            sorigin=input("enter origin")
            sDOD=input("enter date of delivery")
            sweight=int(input("enter weight of goods"))
            L=[scustno,scustname,sorigin,sDOD,sweight]
            query="insert into RELOCATION values(%s,%s,%s,%s,%s)"
            cursor.execute(query,L)
            print("records succesfully stored")
            conn.commit()
    if r==4:
        cursor.execute("use MSRELO")
        cursor.execute("select * from RELOCATION")
        ROW=cursor.fetchall()
        print("Custno\t\tcustname\t\torigin\t\t\tDOD\t\t\tweight")
        print("_"*100)
        for L in ROW:
            print (L[0],"\t\t",L[1],"\t\t",L[2],"\t\t",L[3],"\t\t",L[4])
    if r==5:
        cursor.execute("use MSRELO")
        print("search by customer number")
        sCustno=int(input("enter the customer number to be searched="))
        query="select * from RELOCATION where custno=%s"
        cursor.execute(query,sCustno)
        ROW=cursor.fetchall()
        print("Custno\t\tcustname\t\torigin\t\t\tDOD\t\t\tweight")
        print("_"*70)
        
        for R in ROW:
            print (R[0],"\t\t",R[1],"\t\t",R[2],"\t\t",R[3],"\t\t",R[4])
            print("Customer number =",R[0])
        
        
    if r==6:
        while True:
            cursor.execute("use MSRELO")
            sCustno=int(input("enter customer number to be deleted="))
            sql="delete from RELOCATION where custno = %s" 
            cursor.execute(sql,sCustno)
            conn.commit()
            x = cursor.rowcount
            print("Row affected=",x)
            
            if x>0:
                print("Records deleted")
            else:
                print("Record does not exist")
            break
            
    if r==7:
        cursor.execute("use MSRELO")
        ch="z"
        while ch=="z" or ch=="Z":
            print("1,if you want to change the customer name")
            print("2,if you want to change the origin")
            print("3,if you want to change the date")
            print("4,if you want to change the weight")
            x=int(input("enter your choice="))
            if x==1:
                sCustno=int(input("enter the customer no="))
                if sCustno in cusn:
                    Scustname=input("enter the new customer name=")
                    l=[Scustname, sCustno]
                    cursor.execute("update RELOCATION set Custname=%s where Custno=%s",l)
                    conn.commit()
                    print("sucessfuly updated")
                else:
                    print("wrong customer no.")
            if x==2:
                sCustno=int(input("enter the customer number="))
                if sCustno in cusn:
                    sorigin=input("enter the new origin=")
                    val=[sorigin,sCustno]
                    cursor.execute("update RELOCATION set origin=%s where Custno=%s", val)
                    conn.commit()
                    print("sucessfuly updated")
                else:
                    print("wrong customer no.")
            if x==3:
                sCustno=int(input("enter the customer number "))
                if sCustno in cusn:
                    sDOD=input("enter the new date=")
                    val=[sDOD,sCustno]
                    cursor.execute("update RELOCATION set DOD =%s where Custno=%s",val)
                    conn.commit()
                    print("sucessfuly updated")
                else:
                    print("wrong customer no.")
            if x==4:
                sCustno=int(input("enter the customer number ="))
                
                if sCustno in cusn:
                    sweight=input("enter the new weight=")
                    val=[sweight,sCustno]
                    cursor.execute("update RELOCATION set weight=%s where Custno=%s",val)
                    conn.commit()
                    print("sucessfuly updated")
                else:
                     print("wrong customer no.")
            break
        
    if r==8:
        cursor.execute("use MSRELO")
        cursor.execute("create table SERVICES (Custno int primary key,Custname char(30),Destination char(40),weight int, foreign key(Custno) references RELOCATION(Custno))")
        print("Table SERVICES created successfully.")
        conn.commit()

    if r==9:
        lol=int(input("enter how many values"))
        for i in range (lol):
            cursor.execute("use MSRELO")
            sCustno=int(input("enter the customer number="))
            scustname=input("enter the customer name")
            destination=input("enter the destination of delivery=")
            weight=int(input("enter the weight to be delivered="))
            L=[sCustno,scustname,destination,weight]
            cursor.execute("insert into services values(%s, %s,%s,%s)",L)
            print("Records inserted sucessfully")
            conn.commit()
    if r == 10:
        cursor.execute("USE MSRELO")
        
        cursor.execute("SELECT RELOCATION.Custno, RELOCATION.custname, RELOCATION.origin, SERVICES.destination, RELOCATION.DOD, SERVICES.weight FROM SERVICES JOIN RELOCATION ON SERVICES.Custno = RELOCATION.Custno")
        k = cursor.fetchall()
        
        if not k:
            break
        
        # Print header for the results
        print("Custno\t\tcustname\t\torigin\t\tdestination\tDOD\t\tweight")
        print("_" * 80)  
        
        # Print each row of results
        for R in k:
            print(f"{R[0]}\t\t{R[1]}\t\t{R[2]}\t\t{R[3]}\t\t{R[4]}\t\t{R[5]}")

        
    ch=input("do you wish to continue with the programme? (Y/N)")
    if ch[0].upper()!="Y":
        print("THANK YOU FOR USING MS RELOACTION SERVICES PVT.LTD.PLEASE CONTACT US FOR ANY FURTHER REQUIREMENTS.")
cursor.close()
conn.close()

