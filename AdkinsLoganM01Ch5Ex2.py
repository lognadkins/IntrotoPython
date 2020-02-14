#Defninition of main
def main():
#Get purchase amount.
    purchaseAmount = getinput()
    print("The amount of purchase:",purchaseAmount)

#Calculation functions
    statesalestax = calstatesalestax(purchaseAmount)
    print("The state tax:", statesalestax)

    countysalestax = calcountysalestax(purchaseAmount)
    print("The county tax:", countysalestax)

    Totalsalestax = caltotalsalestax(statesalestax, countysalestax)
    print("The total sales tax:", Totalsalestax)

    Totalofthesale = totalofsale (purchaseAmount, Totalsalestax)
    print("The total of your purchase:", Totalofthesale)
    print(restart())

#define all functions/calculations
def getinput():
    purchaseAmount = float(input("Enter the amount of purchase:"))
    return purchaseAmount
def calstatesalestax(purchaseAmount):
    Statesalestaxpercentage = 0.05
    statesalestax = (purchaseAmount * Statesalestaxpercentage)
    return statesalestax
def calcountysalestax(purchaseAmount):
    countysalestaxpercentage = 0.025
    countysalestax = (purchaseAmount * countysalestaxpercentage)
    return countysalestax
def caltotalsalestax(statesalestax, countysalestax):
    Totalsalestax = statesalestax + countysalestax
    return Totalsalestax
def totalofsale(purchaseAmount, totalsalestax):
    Totalofthesale = (purchaseAmount + totalsalestax)
    return Totalofthesale
#I originally had a note here stating I had not figured out how to repeat the
#restart but have since fixed this as you have seen in screenshots just wanted to clarify!
def restart():
    restart = input("Do you have another purchase?") .lower()
    if restart == "yes":
        main()
    else:
        exit()

#Calling main
main()
restart()
