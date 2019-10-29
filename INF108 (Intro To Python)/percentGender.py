#Asks the user for the number of males and females registered in class and display the percentages of males & females in the class

#Ask for user input
numOfMales = input("Enter the number of registered males in your class: ")
numOfFemales = input("Enter the number of registered females in your class: ")


#Convert variables
numOfMales = int(numOfMales)
numOfFemales = int(numOfFemales)
#Percentage variables for Male/Female as floating point numbers
mPercent = 1.0
fPercent = 1.0
mPercent = float(mPercent)
fPercent = float(fPercent)

#Calculate percentages
total = numOfMales + numOfFemales
mPercent = (numOfMales / total) * 100
fPercent = (numOfFemales / total) * 100


#Print the result
print("Percentage of Males: ", mPercent, "%")
print("Percentage of Females: ", fPercent, "%")
