#Define restart
def restart():
    restart = input("Would you like to view list again?") .lower()
    if restart == "yes":
        main()
    else:
        exit()

#Define function that calculates prime vs even
def isPrime( number ):
    evenDivisions = 0
    if number <= 1:
        return False
    for currentNumber in range(1, number + 1):
        if number % currentNumber == 0:
            evenDivisions = evenDivisions + 1
            if evenDivisions > 2:
                return False
    return True

#Define main function call isPrime to prevent even numbers
def main():
    for currentNumber in range(1, 101):
        if isPrime (currentNumber):
            print(currentNumber)
    print(restart())



#Call main
main()
