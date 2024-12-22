print("Darien Colon's Temp Converter:")
print("")
#Getting user input for temp
uTemp = float(input("Enter a temperature: "))
uType = input("Is the temp F for Fahrenheit or C for Celsius? ")

#Making sure the user inputs only F or C and printing results
if uType == "F":
    if uTemp > 212:
        print("Temp can not be > 212")
    else:
        Celsius = (5.0 / 9) * (uTemp - 32)
        print("The Celsius equivalent is:", format(Celsius,',.1f'))
elif uType == "C":
    if uTemp > 100:
        print("Temp can not be > 100")
    else:
        Fahrenheit = ((9.0 / 5.0) * uTemp) + 32
        print("The Fahrenheit equivalent is:", format(Fahrenheit,',.1f'))
else:
    print("Enter a F or C")


