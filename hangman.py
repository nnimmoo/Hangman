from random import randint  # Do not delete this line
import random


def displayIntro():
    intro = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
        """
    str = """       RULES
     Try to guess the hidden word one letter at a   
     time. The number of dashes are equivalent to   
     the number of letters in the word. If a player 
     suggests a letter that occurs in the word,     
     blank places containing this character will be 
     filled with that letter. If not hangman will be one 
     step closer to death. player has 5 lives. 
     Goal is to guess the word before the man hangs!
     Good Luck"""
    print(intro)
    print(str)


def displayEnd(result):
    badend = """
 __     __           _           _   _                                    
 \ \   / /          | |         | | | |                                   
  \ \_/ /__  _   _  | | ___  ___| |_| |                                   
   \   / _ \| | | | | |/ _ \/ __| __| |                                   
    | | (_) | |_| | | | (_) \__ \ |_|_|                                   
    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
        _______ _                                        _ _          _ _ 
       |__   __| |                                      | (_)        | | |
          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)"""
    goodend = """                                                          
         (_)                                (_)                         
__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
 \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|   """
    if result is False:
        print(badend)
    else:
        print(goodend)


def displayHangman(state):
    stateList = ["""
     ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___       """, """
    ._______.   
     |/      |   
     |           
     |           
     |           
     |           
     |           
 ____|___    """, """ 
     ._______.   
     |/      |   
     |      (_)  
     |           
     |           
     |           
     |           
 ____|___    """, """
    ._______.   
     |/      |   
     |      (_)  
     |       |   
     |       |   
     |           
     |           
 ____|___ """, """
    ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |           
     |           
 ____|___  """, """   
     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |      / \  
     |           
 ____|___     """]
    return print(stateList[state])


def getWord():
    words = open("hangman-words.txt", "r")
    lines = [random.randint(0, 852)]

    for x, line in enumerate(words):
        if x in lines:
            wo = line
    return wo


def valid(c):
    if c.isalpha() and len(c) == 1 and ord(c) < 123 and ord(c) > 96:
        return True
    else:
        print("invalid input, please enter lowercase english word")
        return False


def play():
    word = getWord()
    Keylst = []
    displayHangman(0)
    fail=1
    for i in range(0, len(word) - 1):
        Keylst.append("#")
    print(Keylst)
    # for x in Keylst:
    #     print(x, end='')
    while True:
        usinput = input("please enter the letter")
        if valid(usinput) is True:
            if usinput in word:
              for x in range(0, len(word)):
                 if word[x] == usinput:
                    Keylst[x] = usinput
              print(Keylst)
              if "#" not in Keylst:
                return True
            else:
                displayHangman(fail)
                fail += 1
                print(Keylst)
                if fail==6:
                  return False


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        decision=input('Do you want to play again? (yes/no)')
        if decision=="yes":
            continue
        elif decision=="no":
            break


if __name__ == "__main__":
    hangman()
