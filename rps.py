import random

#rps is list used to give the computer choice
#ques used whenever game function is called to define the variable "pick"

rps = ("rock", "paper", "scissors")
ques = "Choose either rock, paper, or scissors: "

#function for actual game, using inputs asked for down below

def game(pick, comp_pick):

    if pick in rps:

        #the item before thenext item in rps will always lose in that matchup
        #this checks if  the index of the users pick is 1 above the computers. If yes, user won. If no, it goes to the next if

        if (rps.index(pick) - 1) == rps.index(comp_pick):
            print("You chose "+pick+(", and the computer chose "+comp_pick+(", so you won!")))
        #this checks if the indexes are the same, meaning a tie
        elif pick == comp_pick:  
            print("You chose "+pick+(", and the computer chose "+comp_pick+(", so you tied with the computer. Play again."))) 

            #in the result of a tie, it will automatically play again, asking the user for their input. 
            #calls game function here

            game(pick = input(ques).lower(),
            comp_pick = random.choice(rps))

        #only other option is user loses, that outcome happens if the other 2 dont, so used here in else statement
                
        else: print("You chose "+pick+(", and the computer chose "+comp_pick+(", so you lost. ")))
    
    #if to ask if they are playing again

    again = input("Would you like to play again? Y/N: ").lower()
    
    if again == "y":
        game(pick = input(ques).lower(),
        comp_pick = random.choice(rps))
    
    else: print("Thanks for playing!")

    return


#call to run game for the first time

game(pick = input(ques).lower(),
comp_pick = random.choice(rps))
