#Import and define random number 1-3 for computer
import random

def generateRandomNumber():
    randomNumber = random.randint(1, 3)
    return randomNumber

#define translating integer to valid input
def getComputerChoice( randomNumber ):
    if randomNumber == 3:
        computerChoice = "scissors"
    elif randomNumber == 2:
        computerChoice = "paper"
    elif randomNumber == 1:
        computerChoice = "rock"

    return computerChoice

#Define getting input from user
def getUserChoice():
    userChoice = input("Choose rock, paper, or scissors:")
    return userChoice

#Defining determining function which choses winner with possible outcome
def determineWinner( userChoice, computerChoice ):

    rockMessage = "Rock beats scissors"
    scissorsMessage = "Scissors beats paper"
    paperMessage = "Paper beats rock"
    winner = "no winner"
    message = ""
    
    if computerChoice == "rock" and userChoice == "scissors":
        winner = "Computer"
        message = rockMessage
    elif computerChoice == "scissors" and userChoice == "rock":
        winner = "You"
        message = rockMessage

    if computerChoice == "scissors" and userChoice == "paper":
        winner = "Computer"
        message = scissorsMessage
    elif computerChoice == "paper" and userChoice == "scissors":
        winner = "You"
        message = scissorsMessage

    if computerChoice == "paper" and userChoice == "rock":
        winner = "Computer"
        message = paperMessage
    elif computerChoice == "rock" and userChoice == "paper":
        winner = "You"
        message = paperMessage

    return winner, message

#Defining restart function which will allow program to continue in event of a tie
def restart():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice(randomNumber)
    userChoice = getUserChoice()
    print("The computer has chose", computerChoice)
    winner, message = determineWinner( computerChoice, userChoice )

    if winner != "no winner":
        print(winner, "Won(", message, ")")

    return winner

#Defining play again function which allows users to play even without a tie
def playAgain():
    restart = input("Would you like to play again?") .lower()
    if restart == "yes":
        main()
    else:
        exit()

#Defining main function 
def main():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice(randomNumber)
    userChoice = getUserChoice()
    print("The computer has chose", computerChoice)
    winner, message = determineWinner( computerChoice, userChoice )

    if winner != "no winner":
        print(winner, "Won(", message, ")")

    while winner == "no winner":
        print("You both have chosen the same thing")
        winner = restart()

    print(playAgain())

#Call main
main()
        
    

