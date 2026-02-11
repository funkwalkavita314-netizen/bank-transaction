import modulebank as bank


while True:
    print("\n   Bank Menu    ")
    print("1.New customer ")
    print("2.Edit customer")
    print("3.Delete customer")
    print("4.Deposit form")
    print("5.Withdrawl form")
    print("6.transfer amount")
    print("7.transaction between date")
    print("8.exit")

    choice= input("enter your choice")

    if choice=="1":
        bank.new_customer()

    elif choice=="2":
        bank.edit_customer()

    elif choice=="3":
        bank.delete_customer()

    elif choice=="4":
        bank.deposit()

    elif choice=="5":
        bank.withdrawl()

    elif choice=="6":
        bank.tamount()

    elif choice=="7":
        bank.tbd()

    elif choice=="8":
        print("thankyou")
        break
    else:
        print("⭐️please enter a number from the above numbers⭐")
        

    
    


    
