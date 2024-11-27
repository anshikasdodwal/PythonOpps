print("*************** Welcome to ATM **************")
print("Please select Language:")
print("1.English")
print("2.Hindi")
print("3.Punjabi")
balance=35800
lan=int(input())
if(lan==1 or lan ==2 or lan==3):
    print("Please Insert Your Card")
    cardin=int(input())
    if(cardin==1):
        pin=int(input("Please Enter 4 digit Security pin:"))
        if(pin==1234):
            print("Please select Operation:")
            print("1. Cash Withdrawal")
            print("2. Deposits")
            print("3. Balance Enquiry ")
            operation=int(input())
            if(operation==1):
                amount=int(input("Enter amount:"))
                if(amount<balance):

                    print("Processing")
                    print("Please Collect Your Cash")
                    print("Thank You")
                else:
                    print("Invalid Operation!")
            elif(operation==2):
                amountd=int(input("Enter amount to be deposited:"))
                print("Please insert Money")
                print("Processing")
                print("Done")
                print("Thank You")
            else:
                print("Your Bank Balance is:",balance)
                print("Thank You")
                
        else:
            print("Pin is Invalid! Please Try Again")   
    else:
        print("Please Insert Your Card ")  
else:
    print("Please Enter Valid Input and Try Again")  