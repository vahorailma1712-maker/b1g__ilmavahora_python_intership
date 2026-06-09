count = 0
number = -1

print("keep entering numbers.enter 0 to stop.")
print("-" * 40)

while number !=0:
    number = int(input("enter  a number (0 to stop):"))

    if number !=0:
        print(f"you entered :{number}")
        count +=1

print("-" * 40) 
print(f"you entered {count} number(s)befor stopping.") 
      