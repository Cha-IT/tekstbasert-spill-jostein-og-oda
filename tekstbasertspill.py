weapon = False

def strangeCreature():
  actions = ["fight","flee"]
  global weapon
  print("A strange goul-like creature has appeared. You can either run or fight it. What would you like to do?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
      if weapon:
        print("You kill the goul with the knife you found earlier. After moving forward, you find one of the exits. Congats!")
      else:
        print("The goul-like creature has killed you.")
      quit()
    elif userInput == "flee":
      showSkeletons()
    else:
      print("Please enter a valid option.")
      
def showSkeletons():
  directions = ["Luftforsvaret","Hæren","Sjøforsvaret"]
  global weapon
  print("Så bra du vill ble med i militæret, her finns det masse muligheter hva ønsker du å gjøre?")
  userInput = ""
  while userInput not in directions:
    print("Options: Luftforsvaret/Hæren/sjøforsvaret")
    userInput = input()
    if userInput == "Luftforsvaret":
      print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
      weapon = True
    elif userInput == "backward":
      introScene()
    elif userInput == "forward":
      strangeCreature()
    else:
      print("Please enter a valid option.")
      

def hauntedRoom():
  directions = ["right","left","backward"]
  print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      print("Multiple goul-like creatures start emerging as you enter the room. You are killed.")
      quit()
    elif userInput == "left":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option.")

def cameraScene():
  directions = ["forward","backward"]
  print("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      showShadowFigure()
    else:
      print("Please enter a valid option.")
      
def showShadowFigure():
  directions = ["right","backward"]
  print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      cameraScene()
    elif userInput == "left":
      print("You find that this door opens into a wall.")
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option.")


def introScene():
  directions = ["Ja,nei"]
  print("Du har blitt spurt om å dra til militæret, har du lyst til dette?")
  userInput = ""
  while userInput not in directions:
    print("Options: Ja/Nei")
    userInput = input()
    if userInput == "Ja":
      showShadowFigure()
    elif userInput == "Nei":
      showSkeletons()
    else: 
      print("Please enter a valid option.")

if __name__ == "__main__":
  while True:
    print("Velkommen til dette tekstbaserte spillet av Oda og Jostein!")
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    introScene()