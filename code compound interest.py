#Getting user inputted numbers
nStarting_principal = float(input("Enter the starting principal: "))
nInterest_rate = float(input("Enter the annual interest rate: "))
fCompound = float(input("How many times per year is the interest compunded? "))
fPeriods = float(input("For how many years will the account earn interest? "))

#Making the interest rate into a decimal point since its a percentage
nINTEREST_PERCENT = nInterest_rate / 100

#Doing the formula to get the future value

nFuture_value = nStarting_principal * (1 + nINTEREST_PERCENT / fCompound) ** (fPeriods * fCompound)

#Printing the future value
print("At the end of " + format(fPeriods, '.0f') + " years you will have $" + format(nFuture_value, '.2f'))
