print(" ")
print("Hello! in this game, you and our bot are in a competition and you have to choose between three options, Sang, Kaghaz or Gheychi! Every time you win, you get points! Let's start!")
print("Tutorial: \n* Sang defeats Gheychi \n* Gheychi defeats Kaghaz \n* Kaghaz defeats Sang")
print(" ")

import random

YourScore = 0
BotScore = 0

while(True):
    You = input("You: ")
    Bot = random.randint(1, 3)
    
    if Bot == 1 :
        Bot = "Sang"
    elif Bot == 2 :
        Bot = "Kaghaz"
    elif Bot == 3 :
        Bot = "Gheychi"
        
    if You == Bot :
        YourScore = YourScore
        BotScore = BotScore
        
    elif You == "sang" and Bot == "Gheychi" :
        YourScore += 1
    elif You == "gheychi" and Bot == "Kaghaz" :
        YourScore += 1
    elif You == "kaghaz" and Bot == "Sang" :
        YourScore += 1
    elif Bot == "Sang" and You == "gheychi" :
        BotScore += 1
    elif Bot == "Gheychi" and You == "kaghaz" :
        BotScore += 1
    elif Bot == "Kaghaz" and You == "sang" :
        BotScore += 1
    
    if You == "sang" or You == "kaghaz" or You == "gheychi" :
        print(f"Bot: {Bot} \n")
        print("<----------LeaderBoard---------->")
        print(f"Your Score: {YourScore}")
        print(f"Bot Score: {BotScore} \n")
    
    elif You == "leave" :
        print("You left the game! \n")
        print("<----------LeaderBoard---------->")
        print(f"Your Score: {YourScore}")
        print(f"Bot Score: {BotScore}")
        break