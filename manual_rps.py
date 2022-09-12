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

    
        
                
            
        