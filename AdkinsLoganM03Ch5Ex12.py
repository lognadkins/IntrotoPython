#Define max value
def max(integer1, integer2):
    if integer1 > integer2:
        return integer1
    else:
        return integer2

#Define restart
def restart():
    restart = input("Do you have more comparing integers?") .lower()
    if restart == "yes":
        main()
    else:
        exit()

#Define main function
def main():
    # Get numbers
    integer1 = input("Please enter your first number: ")
    integer2 = input("Please enter your second number: ")

    # Return/Print which number is greater.
    print (max(integer1, integer2), "is the max value.")
    print(restart())


# Call the main function.
main()
