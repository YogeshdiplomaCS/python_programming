balance=5000
pin=123
enter = int(input("Enter PIN : "))
if enter==pin:
    amt=int(input("Enter amount to withdraw : "))
    if amt<=balance:
        balance-=amt
        print("Balance : ",balance)
        print(f"Dispensed {amt}. balance : {balance}")
    else:
        print("Insufficient balance")
else:
    print("Insufficient balance!!!")
