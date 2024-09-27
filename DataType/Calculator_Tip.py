print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_convert=(tip/100) + 1
total =(bill/people)*tip_convert
total_rounded=round(total,2)
print(f"Each person should pay: ${total_rounded}")
