#Getting the users name and storing it
sName = (input("Name of the person that we are calculating the grades for: "))

#Getting the four test scores and making sure they're whole numbers
sTestOne = int(input("Test 1: "))
sTestTwo = int(input("Test 2: "))
sTestThree = int(input("Test 3: "))
sTestFour = int(input("Test 4: "))

#Asking if the lowest grade should be dropped
dropGrade = input("Do you wish to Drop the Lowest Grade Y or N? ")

#Checking if the test scores are not less than 0
if sTestOne < 0 or sTestTwo < 0 or sTestThree < 0 or sTestFour < 0:
    print("Test scores cannot be less than 0.")
    exit()

#Getting the lowest score
if sTestFour < sTestOne and sTestFour < sTestTwo and sTestFour < sTestThree:
    lowestScore = sTestFour
elif sTestThree < sTestOne and sTestThree < sTestTwo and sTestThree < sTestFour:
    lowestScore = sTestThree
elif sTestTwo < sTestOne and sTestTwo < sTestThree and sTestTwo < sTestFour:
    lowestScore = sTestTwo
elif sTestOne < sTestTwo and sTestOne < sTestThree and sTestOne < sTestFour:
    lowestScore = sTestOne

#Getting the sum of all tests
testSum = sTestOne + sTestTwo + sTestThree + sTestFour

#Checking if drop lowest input equals Y or N and doing calculations
if dropGrade == "Y" or dropGrade == "y":
    gradeAverage = float((testSum - lowestScore) / 3)
elif dropGrade == "N" or dropGrade == "n":
    gradeAverage = float((testSum) / 4)
else:
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

#Getting the letter grade
if gradeAverage >= 97.0:
    letterGrade = 'A+'
elif gradeAverage >= 94.0:
    letterGrade = 'A'
elif gradeAverage >= 90:
    letterGrade = 'A-'
elif gradeAverage >= 87.0:
    letterGrade = 'B+'
elif gradeAverage >= 84.0:
    letterGrade = 'B'
elif gradeAverage >= 80.0:
    letterGrade = 'B-'
elif gradeAverage >= 77.0:
    letterGrade = 'C+'
elif gradeAverage >= 74.0:
    letterGrade = 'C'
elif gradeAverage >= 70.0:
    letterGrade = 'C-'
elif gradeAverage >= 67.0:
    letterGrade = 'D+'
elif gradeAverage >= 64.0:
    letterGrade = 'D'
elif gradeAverage >= 60.0:
    letterGrade = 'D-'
elif gradeAverage <= 59.9:
    letterGrade = 'F'

#Giving the average and giving the letter grade
print(sName,'test average is:',(format(gradeAverage,'.1f')))
print('Letter grade for the test is:',letterGrade)


