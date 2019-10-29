#Write a program to determine if a family is eligible for Medicaid based on the size of the family and the monthly income of the family.

#only families of size 3 or more are eligible for this service (a family is defined as containing at minimum one adult and one child; therefore a family of size 3 could either be 2 adults and one child OR one adult and 2 children)

#households must have at least one adult and at most 2 adults; the remaining household members must be all children

#only children  under the age of 18 are considered eligible
#=======================================================================================================================

#For exit function after determining invalid family structure (Too many adults or too little kids)
import sys

#Create variables
child = 0
adult = 0
child = int(child)
adult = int(adult)

#Checks age and determines if child or adult
def checkAge(age):

     if age < 18:
         #This is a child
         global child #To change variable
         child = child + 1
     else:
        #This is an adult
        global adult
        adult = adult + 1


def validateFamily():
    #Checks if there are 1-2 adults in family
    if adult == 1 or adult == 2:
        #Checks if there is at least one child in family
        if child >=1:
            return True
        else:
            print("Sorry, your family is not eligible.")
            return False
    else:
        print("Sorry, your family is not eligible.")
        return False

#bool?
def findEligibility(size, income):

    adds = 0
    adds = int(adds)
    addIncome = 0.0
    addIncome = float(addIncome)


    if size == 3:
        if income < 2981.0:
            return True
        else:
            return False
    elif size == 4:
        if income < 3356.0:
            return True
        else:
            return False
    elif size == 5:
        if income < 3561.0:
            return True
        else:
            return False
    elif size == 6:
        if income < 3689.0:
            return True
        else:
            return False
    elif size >=7:
        #Determine how many additional children
        adds = size - 6
        #Calculate additional income based on the additional children
        addIncome = adds * 622
        if income < (3689.0 + addIncome):
            return True
        else:
            return False

    #else:
        #



def main():




    #Print welcome message
    print("Welcome! Determine your Medicaid eligibility below! \n")

    try:
        #Ask for user inputs (Size of family (min 3), age of members, income)
        familySize = int(input("Enter the size of your family: "))
    except:
        print("Error! Non-numeric value!")
    else:

        #Determine if size of family < 3
        if familySize >= 3:

            #loop iteration variable
            i = 0
            while i < familySize:

                #Determine if members are adults or children (use function)
                try:
                    memberAge = int(input("Enter the age for Family Member " + str(i+1) + ": "))
                except:
                    print("Error! Non-numeric value!")
                else:
                    #
                    checkAge(memberAge)
                    i = i + 1

            print("Adults :" + str(adult))
            print("Children :" + str(child))
            #Check if there are 1-2 adults in the family + at least 1 child
            result = validateFamily()
            if result == False:
                sys.exit()
            else:

                try:
                    income = float(input("Enter your monthly income: "))
                except:
                    print("Error! Non-numeric value!")
                else:

                    #Analyze income level based on family size
                    eligible = findEligibility(familySize, income)

                    if eligible == False:
                        print("Your family does not meet the monthly income requirement. Non-eligible")
                    elif eligible == True:
                        print("Your family meets the monthly income requirement. Eligible")
                    else:
                        print("Error determining eligibility")



        #Else Family Size not eligible
        else:
            print("Family size not eligible.")

main()
