balance = 5000

print("Welcome to Python Bank ATm")
print("1.Check Balance")
print("2.Withdrow Amount")

choice = int(input("enter chois (1-2):"))

if choice ==1:
    print(f"your Balance: {balance}")
elif choice ==2:
    Withdraw_amount = float(input("enter amount to withdraw:"))

    if Withdraw_amount <= balance:
        balance = balance -Withdraw_amount
        print("Transaction Successful")
        print(f"Remaining Balance: {int(balance)}")
 
    else:
     print("Insufficient Balance")

else:
    print("Invalid Choice")
   
  

