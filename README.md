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
    
    
 # Milestone 5
 This milestone required for me to adapt the code that was tested in Milestone 3 so that it could be implemented in the RPS game. This was done by assigning the code to a function called get_prediction. In this function I added 2 extra lines of code so that the program would be able to accurately detect amd assign the gestures from the webcam to the choice:
 
 max_value = np.argmax(prediction[0])
 user_choice = self.choice[max_value]
 
 After this I created a 3 second countdown timer that would run before the execturion of the get_prediction function and the get_computer_choice function.
   def countdown(self,time_sec):
        print ("Ready?")
        while time_sec:
            mins,secs = divmod(time_sec,60)
            time_format   = "{:02d}:{:02d}".format(mins,secs)
            print(time_format, end="\r")
            time.sleep(1)
            time_sec -=1
        print ("Start")
      
 Finally after initialising the user_wins and computer_wins in the __init__ method I was able to create a while loop in the game function that would run until either the user or computer wins 3 rounds. 
     while game.user_wins < 3 or game.computer_wins < 3:
        game.countdown(3)
        computer = game.get_computer_choice()
        user = game.get_prediction()
        game.get_winner(user,computer)
        rounds += 1
        if game.user_wins == 3:
            print("You have won the game")
            exit()
        elif game.computer_wins == 3:
            print("You have lost the game ")
            exit()
            
Below is the completed code for this project:

from itertools import count
import random
import re
import cv2
from keras.models import load_model
import numpy as np
import time
class camera_rps:
    def __init__(self, choice):
        # List comprehension to convert list into lowercase
        self.choice = [x.lower() for x in choice]
        self.user_wins = 0
        self.computer_wins = 0
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) 
    def countdown(self,time_sec):
        print ("Ready?")
        while time_sec:
            mins,secs = divmod(time_sec,60)
            time_format   = "{:02d}:{:02d}".format(mins,secs)
            print(time_format, end="\r")
            time.sleep(1)
            time_sec -=1
        print ("Start")
        
    def get_prediction(self):
        end_time = time.time() + 3
        while end_time > time.time():
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            max_value = np.argmax(prediction[0])
            user_choice = self.choice[max_value]
            print(user_choice)
            cv2.imshow('frame', frame)
                # Press q to close the window
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                        
            # After the loop release the cap object
        

        
        return user_choice


    def get_computer_choice(self):
        computer_choice = random.choice(self.choice[0:3])
        print(computer_choice)
        return computer_choice
    
    def get_winner(self, user_choice,computer_choice):
        if user_choice == "nothing":
            print("Please show either Rock, Paper or Scissors")
        elif user_choice == computer_choice:
           print("Game is a draw") 
        elif (user_choice == "rock" and computer_choice== "scissors") or ( user_choice == "paper" and computer_choice == "rock") or ( user_choice == "scissors" and computer_choice == "paper"):
            print(" You win")
            self.user_wins += 1
        else: 
            print(" You have lost")
            self.computer_wins += 1
    
def play(choice):
    game = camera_rps(choice)
    rounds=0
    while game.user_wins < 3 or game.computer_wins < 3:
        game.countdown(3)
        computer = game.get_computer_choice()
        user = game.get_prediction()
        game.get_winner(user,computer)
        rounds += 1
        if game.user_wins == 3:
            print("You have won the game")
            exit()
        elif game.computer_wins == 3:
            print("You have lost the game ")
            exit()
    game.cap.release()
            # Destroy all the windows
    cv2.destroyAllWindows()
   

if __name__ == '__main__':
    choice = ["Rock", "Paper" , "Scissors" , "Nothing"]
    play(choice)
