#Your program should prompt the user for a file name to write to.
#Your program should let the user specify how many random numbers will be generated and added to the file.
#Each random number should be in the range of 1 through 250. Hint: use random.randint
#After the program completes writing to the output file, open the file to read and print the contents.
#Print one random number per line


#To generate random numbers
import random


def main():

    #Welcome message
    print("Welcome to my program! I will be printing random integers from 1-250 into a file for you! ")


    #Prompt user to enter fileName to write to
    fileName = input("Enter the file you want me to write to  (followed by .txt): ")

    #Ask for the amount of random numbers to be generated
    try:
        amount = int(input("Enter the amount of numbers you want to be generated: "))
    except:
        print("ERROR! Non-numeric value!")
    else:

        i = int(0)

        #Open file
        writeFile = open(fileName, "w")     #w for writing to file


        #Generate random number from 1-250
        for x in range(amount):
            #Write randomNum
            writeFile.write(str(random.randint(1,251)) + " \n")

        #Close file
        writeFile.close()



        #Open the file to read and print contents

        #Open file
        writeFile = open(fileName, "r") #r for reading file

        #Read file
        print(writeFile.read())

        #Close file
        writeFile.close()



main()
