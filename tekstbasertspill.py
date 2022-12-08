weapon = False

def jægerHistorie():
  directions = ["Dreper han", "Dreper han ikke"]
  print()
  print("Du får et oppdrag om å følge en spesialtrent russisk soldat som befinner seg på norsk territorium, når du ser soldaten finner du ut at det er en du har hatt førstegangstjeneste med. Hva gjør du?")
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

def hærensValg():
  actions = ["Jægersoldat","Artillerist"]
  global weapon
  print("De er altid fint å ha flere i hæren hvilken stilling ønsker du å ha?")
  userInput = ""
  while userInput not in actions:
    print("Options: Jægersoldat/Artillerist")
    userInput = input()
    if userInput == "Jægersoldat":
      if weapon:
        jægerHistorie()
    elif userInput == "Artillerist":
      artilleristHistorie()
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
        luftforsvaretValg()
    elif userInput == "Hæren":
        hærensValg()
    elif userInput == "Sjøforsvaret":
        sjøforsvaretValg()
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
  print("Norge hadde for lite soldater til krigen, Russland har tatt over landet og du har blitt sendt til en konsentrasjonsleir i Sibir")
  quit()

def introScene():
  directions = ["Ja,nei"]
  print("Du har blitt spurt om å dra til militæret, har du lyst til dette?")
  userInput = ""
  while userInput not in directions:
    print("Options: Ja/Nei")
    userInput = input()
    if userInput == "Nei":
      showShadowFigure()
    elif userInput == "Ja":
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