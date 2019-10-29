#Using a WHILE loop write a program that asks the user to guess your favorite number. The program should end when the user guesses correctly, but otherwise provides hints for guessing higher or lower.



def main():

    counter = int(1)

    #Generate random favorite number? / Create favorite number
    favoriteNum = int(17)

    try:

        #Welcome Message
        userNum = input("Guess my favorite number: ")
        userNum = int(userNum)

    except:

        print("ERROR! Non-numeric value")
        userNum = input("Guess my favorite number: ")
        userNum = int(userNum)

    else:

        #Loop to keep asking until number is guess correctly
        while userNum != favoriteNum:               #Compare user number to favorite number

            #Determine whether to guess higher or lower
            if userNum < favoriteNum:

                print("WRONG! Guess higher!")

                try:

                    #Welcome Message
                    userNum = input("Guess my favorite number: ")
                    userNum = int(userNum)

                except:

                    print("ERROR! Non-numeric value")
                    userNum = input("Guess my favorite number: ")
                    userNum = int(userNum)

                else:

                    #Increment counter to record number of tries
                    counter = counter + 1

            elif userNum > favoriteNum:

                print("WRONG! Guess lower!")

                try:

                    #Welcome Message
                    userNum = input("Guess my favorite number: ")
                    userNum = int(userNum)

                except:

                    print("ERROR! Non-numeric value")
                    userNum = input("Guess my favorite number: ")
                    userNum = int(userNum)

                else:
                    #Increment counter to record number of tries
                    counter = counter + 1


    if userNum == favoriteNum:

        #When guessed correctly, display message and # of tries before a correct guess
        print("Correct! You guessed my number in " + str(counter) + " tries!")

    else:

        userNum = input("Guess my favorite number: ")
        userNum = int(userNum)

        counter = counter + 1


main()
