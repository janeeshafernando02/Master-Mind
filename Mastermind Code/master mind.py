#--- GameInt ---
play_again = "yes"
while (play_again == "yes"): 
    #Get user inputs
    student_name=input("Enter your name:")
    print("\n")
      
    print("                                                         Hi",student_name,"Welcome to GameInt \n")
    print("_________________________________________________________________________________________________________________________________________________________")
    print("\n")
    print("  Number to Guess - XXXX",end="                                                      ")
    print("  Color Mapping:") 
    print("                                                                                  1 - White , 2 - Blue , 3 - Red")
    print("                                                                                  4 - Yellow , 5 - Green , 6 - Purple.\n ") 
    print("\n")
    print("  Enter a 4 digit number and you will get maximum 8 guesses.")
   
    #Importing random to generate random numbers
    import random
    hidden_peg=[]
    #Computer randomly picks four digit code in the range of 1 to 6
    for i in range(0,4):
        a = random.randint(1,6)
        hidden_peg.append(a)
    #print(hidden_peg)

    #Intializing variables
    attempts=0
    player_guess=[]
    option1=""
    option2=""
    option3=""
    option4=""
    null_list = [0,0,0,0]
    score=100

    print("_________________________________________________________________________________________________________________________________________________________")
    print("  Attempt No",end="                                ")
    print("Guess",end="                                       ")
    print("Result")
    print("_________________________________________________________________________________________________________________________________________________________")
    print("\n")
    #Player guesses the hidden peg	
    while attempts <8:
         att=attempts+1
         print(" ",att,end="                                   ")
         num1,num2,num3,num4=input("      ")
         #Converting the input guesses to integers in order to perform the next functions.  
         num1=int(num1)
         num2=int(num2)
         num3=int(num3)
         num4=int(num4)

         #Store the values of the player guess to player_guess list.
         player_guess.append(num1)
         player_guess.append(num2)
         player_guess.append(num3)
         player_guess.append(num4)
         #print(player_guess)
         #print()

         
         # terminating the game without going into 8th guess
         if player_guess == null_list:
            print("You ended the game")
            break
         #checking the player guess and giving points according to the attempts.
         if player_guess == hidden_peg:
            print("_________________________________________________________________________________________ 1 1")
            print("                                                                                          1 1")
            score=score-12.5*attempts
            print("Congratulations !!!!! You have won the game…")
            print("You have scored",score,"points.")
            break

         # checking if player's input is correct
         if len(player_guess) != 4:
            print("Enter a 4 digit number")
            break 
         
        #comparison between player's input and secret code
         if player_guess[0] == hidden_peg[0]:
            option1 ="1"
         elif player_guess[0] in hidden_peg:
            option1 ="0"
         else:
            option1="-"

         if player_guess[1] == hidden_peg[1]:
            option2="1"
         elif player_guess[1] in hidden_peg:
            option2="0"
         else:
            option2="-"

         if player_guess[2] == hidden_peg[2]:
            option3="1"
         elif player_guess[2] in hidden_peg:
            option3="0"
         else:
            option3="-"

         if player_guess[3] == hidden_peg[3]:
            option4="1"
         elif player_guess[3] in hidden_peg:
            option4="0"
         else:
            option4="-"

         
         # clearing the list to restart the game
         player_guess =[]
         attempts=attempts+1

         print("_________________________________________________________________________________________",option1,option2)
         print("                                                                                         ",option3,option4)

    # mark the end of the game.
    play_again ="no"
    play_again = str(input("Do you want to play another game (yes/no)? "))
    continue
print("Thankyou for playing the game.")

    
