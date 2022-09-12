# Rock_Paper_Scissors
Objective: To create a Rock, Paper & Scissors game where the user can play via the webcam with the computer.


# Milestone 1
Created a GIT repository for the Rock,Paper Scissors game simulation

# Milestone 2
I have used the teachable machine software to create a machine learning model using my webcam. I created 3 classes ( Rock, Paper & Scissors), where I captures various different images of my hand which corrolated to each class. I then processed this information through program to create the model. This machine could then identify which hand gestrures belonged to which class. After I was satisfied with the accuracy of the model I downloaded the model as a TensorFlow model which will be used on python to program the rest of the game. 

# Milestone 3 & 4
1. Downnloaded a testfile which can run the exported Tensorflow model. This uses the webcam and numpy to detect the accuracy of the gestures which is outputted as a decimal in the form of a list.

2. Next I created a Manual RPS game where the user would compete with the computer. I used OOP as learnt in the previous project to create this game. Below is the code that was written:
import random

class rps:
    def __init__(self, choice):
        # List comprehension to convert list into lowercase
        self.choice = [x.lower() for x in choice]

    def get_computer_choice(self):
        computer_choice = random.choices(self.choice)
        print(computer_choice)
        return computer_choice
    
    def get_user_choice(self):
            user_choice = input("Please enter either Rock, Paper or Scissors: ").lower()
            return user_choice
            
    
    def get_winner(self, user_choice,computer_choice):
        if user_choice == computer_choice:
           print("Game is a draw") 
        elif (user_choice == "rock" and computer_choice== "scissors") or ( user_choice == "paper" and computer_choice == "rock") or ( user_choice == "scissors" and computer_choice == "paper"):
            print(" You win")
        else: 
            print(" You have lost")

def play(choice):
    game = rps(choice)
    rounds = 0
    while rounds < 3:
        computer = game.get_computer_choice()
        user = game.get_user_choice()
        game.get_winner(user,computer)
        rounds += 1
        

if __name__ == '__main__':
    choice = ["Rock", "Paper" , "Scissors" ]
    play(choice)
