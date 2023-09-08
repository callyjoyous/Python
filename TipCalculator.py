print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people will be splitting this bill? "))

bill_with_tip = tip / 100 * bill + bill 

bill_split = round(bill_with_tip / people, 2)

print("The bill split " + str(people) + " ways is: $" + str(bill_split))
