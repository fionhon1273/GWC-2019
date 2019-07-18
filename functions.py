
# --- Define your functions below! ---
def greetingFunction():
    print("Bonjour!")

def respondToUser(userAnswer):
    if(userAnswer == "good"):
        print("I'm happy to hear that. I'm good too.")
        if(userAnswer == "bad"):
            print("I'm sorry. How can I help?")
    else:
        print("That's good. Hope it gets better!")

def respondToUser2(userAnswer2):
    if(userAnswer2 == "yes"):
        print("What has a head, a tail, is brown, and has no legs? ")
    if(userAnswer2 == "no"):
        print("Byte me! Too bad!")
        print("What has a head, a tail, is brown, and has no legs? ")

# def respondToUser2.5(userAnswer2.5):
#         if(userAnswer2.5 == yes):
#             print()
#         else:
#             print("I'm done talking to you. Bye!")

def respondToUser3(userAnswer3):
    if(userAnswer3 == "a penny" or "penny"):
        print("YAS GOOD JOB!")
    else:
        print("OOPS! You got it wrong! The answer is a penny.")

# --- Put your main program below! ---

def main():
  while True:

     greetingFunction()

     answer = input("What's your name? ")
     print("That's a dope name!")

     user_input = input("How are you today? ")
     respondToUser(user_input)

     userAnswer2 = input("Would you like to hear a riddle? ")
     respondToUser2(userAnswer2)

     userAnswer3 = input("Answer: ")
     respondToUser3(userAnswer3)

     print("Nice talking to you! Bye!")

# DON'T TOUCH! Setup code that runs your main() function.

if __name__ == "__main__":

  main()
