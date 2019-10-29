#Credit card numbers follow a standard system. For example, Visa, MasterCard, and American Express Card all have 16 digits, and the first digit serves to indicate the card brand. All Visa cards start with a 4; MasterCard cards always starts with a 5; and American Express cards start with a 3.
#Write a program that prompts for a 16-digit credit card and emits the name of the brand. If the card brand cannot be determined, the program should output “Unknown Card.”

def main():
    #Ask for user input
    creditCard = input("Enter  your 16-digit credit card number: ")

    #Convert variable
    creditCard = int(creditCard)
    cardBrand = str("")

    #Check if input is valid
    if creditCard >= 1000000000000000 & creditCard <= 9999999999999999:

        #Check for cardBrand
        if creditCard >= 4000000000000000 & creditCard <= 4999999999999999:
            cardBrand = str("Visa")
        elif creditCard >= 5000000000000000 & creditCard <= 5999999999999999:
            cardBrand = str("MasterCard")
        elif creditCard >= 3000000000000000 & creditCard <= 3999999999999999:
            cardBrand = str("American Express")

        #Else print unknown card
        else:
            cardBrand = str("Unkown Card")

    #Else print invalid credit card
    else:
        cardBrand = str("Invalid Credit Card")


    #(Print output)
    print("Your card is a(n): " + cardBrand)


main()
