# Name: Darien Colon

#User input for name and weight
print("Find out your weight on different planets!!")
print(" ")
uName =(input("Your Name?: "))
uWeight = float(input("Your Weight?: "))
print (" ")

#Variables for the different planets gravity
meGrav = 0.38
veGrav = 0.91
moGrav = 0.165
maGrav = 0.38
juGrav = 2.34
saGrav = 0.93
urGrav = 0.92
neGrav = 1.12
plGrav = 0.066

#Calculating your weight on different planets
meWeight = float(uWeight * meGrav)
veWeight = float(uWeight * veGrav)
moWeight = float(uWeight * moGrav)
maWeight = float(uWeight * maGrav)
juWeight = float(uWeight * juGrav)
saWeight = float(uWeight * saGrav)
urWeight = float(uWeight * urGrav)
neWeight = float(uWeight * neGrav)
plWeight = float(uWeight * plGrav)

#Printing out the output of everything
print(uName + " here are your results!")
print(" ")
print("Weight on Mercury:" + format(meWeight,'10.2f'))
print("Weight on Venus:" + format(veWeight,'10.2f'))
print("Weight on Moon:"  + format(moWeight,'10.2f'))
print("Weight on Mars:" + format(maWeight,'10.2f'))
print("Weight on Jupiter:" + format(juWeight,'10.2f'))
print("Weight on Saturn:" + format(saWeight,'10.2f'))
print("Weight on Uranus:" + format(urWeight,'10.2f'))
print("Weight on Neptune:" + format(neWeight,'10.2f'))
print("Weight on Pluto:" + format(plWeight,'10.2f'))
print(" ")
print("Wow, isnt that interesting?")
