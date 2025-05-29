balance = 50000
pin = 1234

def menu():
    print("1. CHECK BALANCE")
    print("2. BUY AIRTIME")
    print("3. WITHDRAW")
    print("4. DEPOSIT")
    print("5. TRANSFER")
    print("6. PAY BILLS")

def confirm():
     print("Do you wish to perform another  function")
     print("1. YES     2. NO")
     aa = int(input())
     if aa == 1:
         menu()
         bb = int(input())
         if bb == 1:
             check_balance()

         elif bb == 2:
             buy_airtime()
         elif bb == 3:
             withdraw()
         elif bb ==  4:
             transfer()
         elif bb == 5:
             transfer()
         elif bb == 6:
             pay_bills()
     else:
        return

def check_balance():
  print(f"Your current balance is: {globals()['balance']}")
  confirm()

def buy_airtime():
    print("1. MTN    2. AIRTEL   3. GLO    4. Etisalat")
    line = int(input())
    if line == 1:
        print( "Enter Mtn line ")
    elif line == 2:
        print("Enter Airtel line")
    elif line == 3:
        print("Enter GLO line")
    elif line == 4:
        print("Enter Etisalat line")
    else:
        print("Wrong input")
        return
    # network = str(input())
    # if network != str:
    #     print("wrong input")
    #     return
    # else:
    #     print("Enter Phone Number")
    mtn= ['0803', '0806', '0813', '0816']
    airtel = ['0907','0807','0707','0817']
    glo = ['0705','0805','0905','0815']
    Etisalat = ['0804','0904', '0814', '0704']
    phone = input("")
    if len(phone) == 11 and line ==1 and phone[0:4] in mtn:
        amount = int(input("Enter Amount"))
        if amount <= balance:
            print(f"{amount} recharged successfully")
            confirm()
        else:
            print("Insufficient Balance")
            confirm()
    elif len(phone) == 11 and line ==2 and phone[0:4] in airtel:
        amount = int(input("Enter Amount"))
        if amount <= balance:
            print(f"{amount} recharged successfully")
            confirm()
        else:
            print("Insufficient Balance")
            confirm()
    elif len(phone) == 11 and line ==3 and phone[0:4] in glo:
        amount = int(input("Enter Amount"))
        if amount <= balance:
            print(f"{amount} recharged successfully")
            confirm()
        else:
            print("Insufficient Balance")
            confirm()
    elif len(phone) == 11 and line == 4 and phone[0:4] in Etisalat:
        amount = int(input("Enter Amount"))
        if amount <= balance:
            print(f"{amount} recharged successfully")
            confirm()
        else:
            print("Insufficient Balance")
        confirm()
    else:
        print("INVALID INPUT")
        confirm()

def deposit():
    print("Enter Amount")
    amount = int(input())
    #balance = 50000
    if amount > 1000 and amount % 1000 == 0:
         globals()['balance'] += amount
         #newbalance = balance
         print(f"{amount} deposited successfully.")
         print(f"{globals()['balance']} is your new balance")
         confirm()
    else:
         print("Invalid deposit amount.")
    confirm()

def transfer ():
    print("1. First bank 2. Providus Bank 3. UBA 4. Fidelity bank")
    #balance = 50000
    bank = int(input())
    if bank == 1:
        print("Enter Account Number")
    elif bank == 2:
        print("Enter Account Number")
    elif bank == 3:
        print("Enter Account Number")
    elif bank == 4:
        print("Enter Account Number")
    else:
        print("Wrong Input")
    AccNo = input()
    if len(AccNo) == 10:
        print("Enter Amount")
        amount = int(input())
        if amount <= globals()['balance']:
            globals()['balance'] -= amount
            print(f"{amount} successfully transferred")
            print(f"your new balance is {globals()['balance']}")
            confirm()
        else:
            print("Insufficient balance")
            confirm()
    else:
        print("Wrong input")
        confirm()

def pay_bills():
    print("1. DSTV 2. PHCN ")
    pb = int(input())
    if pb == 1:
        print("Enter DSTV number")
        #balance = 50000
        compact = 29000
        compactplus = 45000
        superb = 60000
        dstv = input()
        if len(dstv) == 10:
            print("1. Compact 2.Compactplus 3. Superb")
            package = int(input())
            # if package == 1:
            #     amount = compact
            # elif package == 2:
            #     amount = compactplus
            # elif package == 3:
            #     amount = superb
            if package == 1 and globals()['balance'] > compact:
                print("DSTV package subscribed successfully")
                confirm()
            elif package == 2 and globals()['balance'] > compactplus:
                print("DSTV package subscribed successfully")
                confirm()
            elif package == 3 and globals()['balance'] > superb:
                print("DSTV package subscribed successfully")
                confirm()
            else:
                print("Insufficient balance")
                confirm()
                # if newpackage <= balance:
                #     print(f"{package} successfully subscribed")
                # else:
                #     print("insufficient balance")
        else:
            print("Wrong Input")
            confirm()
    if pb == 2:
        print("Enter PHCN number")
        PHCN = input()
        balance = 50000
        # import random
        # x = random.randrange(0,10)
        if len(PHCN) == 11:
            print("How much token would you like?")
        else:
            print("Check number")
        import random
        token = ''.join([str(random.randint(0, 9)) for _ in range(20)])
        unit = 66
        amount = int(input())
        if amount <= globals()['balance']:
            globals()['balance'] -= amount
            print(f"you have purchased {amount/unit} KWH worth of energy")
            print(f"{token} is your token")
            #print(f"{x} is your token ")
            confirm()
        else:
            print("Insufficient Balance")
    else:
        return


def withdraw():
    print("1. 1000 2. 2000 3. 5000 4. 10000 5. Others")
    amount = int(input())
    if amount == 1:
        globals()['balance'] -= 1000
        print(f"{amount} has been withdrawn successfully")
        print(f"{globals()['balance']} is your new balance")
        confirm()
    elif amount  == 2:
        globals()['balance'] -= 2000
        print(f"{amount} has been withdrawn successfully")
        print(f"{globals()['balance']} is your new balance")
        confirm()
    elif amount == 3:
        globals()['balance'] -= 5000
        print(f"{amount} has been withdrawn successfully")
        print(f"{globals()['balance']} is your new balance")
        confirm()
    elif amount == 4:
        globals()['balance'] -= 10000
        print(f"{amount} has been withdrawn successfully")
        print(f"{globals()['balance']} is your new balance")
        confirm()
    elif amount == 5:
        if amount <= globals()['balance']:
            if amount % 1000 == 0:
                globals()['balance'] -= amount
                print(f"{amount} has been withdrawn successfully")
                print(f"{globals()['balance']} is your new balance")
                confirm()
            else:
                print("Enter a multiple of 1000")
                confirm()
    else:
        print("Insufficient balance.")
        confirm()

    # balance = 50000
   # new_balance = globals()['balance']




print("WELCOME TO ECOBANK")
print("**************")
print()
enter_pin =int(input("PLS ENTER YOUR 4 DIGIT PIN  "))
if pin == enter_pin:
     print("1. Check balance")
     print("2. Buy airtime")
     print("3. Withdraw")
     print("4. Deposit")
     print("5. TRANSFER")
     print("6. PAY BILLS")
     second = int(input())
     if second ==1:
         check_balance()
     elif second == 2:
         buy_airtime()
     elif second == 3:
         withdraw()
     elif second == 4:
         deposit()
     elif second == 5:
         transfer()
     elif second == 6:
         pay_bills()

else:
     print("INVALID PIN, TRY AGAIN")