import mysql.connector

def get_connection():
    return mysql.connector.connect(host="localhost",user="root",passwd="121234",database="bank")

def new_customer():
    while True:
        accno=input("enter account number")
        if not accno.isdigit():
            print("account number must be in digits")
            continue
        if len(accno)!=12:
            print("account number must be in 12 digits")
            continue
        accno=int(accno)
        name=input("enter name")
        fathername=input("enter father name")
        address=input("enter address")
        city=input("enter city name")
        state=input("enter state name")
        adharno=input("enter adhaar number")
        if not adharno.isdigit():
            print("adhar number must be in digits")
            continue
        if len(adharno)!=12:
            print("adhar number must be in 12 digits")
            continue
        adharno=int(adharno)
        amount=float(input("enter amount"))
        if amount<0:
            print("amount must be positive")
            continue

        con=get_connection()
        if con.is_connected():
            cur=con.cursor()
            query="insert into customer values('{}','{}','{}','{}','{}','{}','{}','{}')".format(accno,name,fathername,address,city,state,adharno,amount)
            print(query)

            cur.execute(query)
            con.commit()
            con.close()
            print("new customer added")
        else:
            print("Database not connected")
        choice=input("continue y/n")
        if choice=="n":
            break

def tbd():
    accno=int(input("enter account number"))
    fdate=input("enter first date")
    ldate=input("enter last date")

    con=get_connection()
    if con.is_connected():
        cur=con.cursor()
        select="select*from dw where account='{}' and date between '{}' and '{}'".format(accno,fdate,ldate)
        cur.execute(select)
        data=cur.fetchall()
        for row in data:
            for column in row:
                print(row,end="\t")
                print()
        con.close()
    else:
        print("not connected")

def tamount():
    taccno=int(input("enter transferring account number"))
    raccno=int(input("enter receiving account number"))
    amount=float(input("enter amount to transfer"))

    con=get_connection()
    if con.is_connected:
        cur=con.cursor()
        select="select amount from customer where accno='{}' and '{}'".format(taccno,raccno)
        cur.execute(select)
        result=cur.fetchone()
        if result is None:
            print("account number not found")
        else:
            print("account found and amount tranfered")

            insert="insert into th values('{}','{}','{}')".format(taccno,raccno,amount)
            cur.execute(insert)
            con.commit()

            update="update customer set amount=amount+'{}' where accno='{}'".format(amount,raccno)
            cur.execute(update)
            con.commit
            update="update customer set amount=amount-'{}' where accno='{}'".format(amount,taccno)
            cur.execute(update)
            con.commit()
            con.close()
    else:
        print("not connected")

def deposit():
    accno=int(input("enter account number"))
    ttype="deposit"
    amount=float(input("enter amount"))
    date=input("enter date of transaction")

    con=get_connection()
    if con.is_connected():
        cur=con.cursor()
        select="select amount from customer where accno='{}'".format(accno)
        cur.execute(select)
        result=cur.fetchone()
        if result is None:
            print("account number not found")
        else:
            balance=result[0]
            print("old balance=",balance)
        
            query="insert into dw values('{}','{}','{}','{}')".format(accno,ttype,amount,date)
            cur.execute(query)
            con.commit()
            update="update customer set amount=amount+'{}' where accno='{}'".format(amount,accno)
            cur.execute(update)
            con.commit()
            con.close()
    else:
        print("not connected")

def withdrawl():
    accno=int(input("enter account number"))
    ttype="withdrawl"
    amount=float(input("enter amount"))
    date=input("enter date of transaction")

    con=get_connection()
    if con.is_connected():
        cur=con.cursor()
        select="select amount from customer where accno='{}'".format(accno)
        cur.execute(select)
        result=cur.fetchone()
        if result is None:
            print("account number not found")
        else:
            balance=result[0]
            print("old balance=",balance)
            print("account found and amount withdrawl")
        
            query="insert into dw values('{}','{}','{}','{}')".format(accno,ttype,amount,date)
            cur.execute(query)
            con.commit()
    
            update="update customer set amount=amount-{} where accno={}".format(amount,accno)
            cur.execute(update)
            con.commit()
            con.close()
    else:
        print("not connected")


def delete_customer():
    accno=int(input("enter account number"))
    con=get_connection()
    if con.is_connected():
        cur=con.cursor()
        query="delete from customer where accno='{}'".format(accno)
        cur.execute(query)
        con.commit()
        dw="delete from dw where account='{}'".format(accno)
        cur.execute(dw)
        con.commit()
        con.close()
        print("customer deleted")
    else:
        print("not connected")


def edit_customer():
    con=get_connection()
    if con.is_connected():
        cur=con.cursor()
        
        accno=int(input("enter account number"))
            
        print('''
which detail do you want to update?
1.name
2.fathername
3.address
4.city
5.state
6.adharno
7.amount
''')

        cho=int(input("enter choice between 1-7"))

        if cho==1:
            new_value=input("enter new name")
            query="update customer set name='{}' where accno='{}'".format(new_value,accno)
            
        elif cho==2:
            new_value=input("enter father's name")
            query="update customer set fathername='{}' where accno='{}'".format(new_value,accno)

        elif cho==3:
            new_value=input("enter new address")
            query="update customer set address='{}' where accno='{}'".format(new_value,accno)

        elif cho==4:
            new_value=input("enter city name")
            query="update customer set city='{}' where accno='{}'".format(new_value,accno)

        elif cho==5:
            new_value=input("enter state name")
            query="update customer set state='{}' where accno='{}'".format(new_value,accno)

        elif cho==6:
            new_value=int(input("enter new adhar number"))
            query="update customer adharno state='{}' where accno='{}'".format(new_value,accno)

        elif cho==7:
            new_value=float(input("enter new amount"))
            query="update customer set amount='{}' where accno='{}'".format(new_value,accno)

        else:
            print("invalid choice")
            con.close()
            exit()

        cur.execute(query)
        con.commit()
        if query is None:
            print("account number not found")
        else:
            print("customer record updated successfully")


    else:
        print("not connected")
                




            
        
    



    


    



    
        




        

