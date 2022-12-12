weapon = False

def jægerHistorie():
  directions = ["Dreper han", "Dreper han ikke"]
  print()
  print("Du får et oppdrag om å følge en spesialtrent russisk soldat som befinner seg på norsk territorium, når du ser soldaten finner du ut at det er en du har hatt førstegangstjeneste med. Hva gjør du?")
  userInput = ""
  while userInput not in directions:
    print("Valg: Dreper han/Dreper han ikke")
    userInput = input()
    if userInput == "Dreper han":
      print("Du velger å drepe han og deretter fullføre oppdraget, dette var en sentral person for den russiske siden og du får æresmedalje for din tjeneste.")
      quit()
    elif userInput == "Dreper han ikke":
      print("Du velger å la han gå, han klarer å skaffe viktig informasjon om Norge sin plan fremover i krigen, din øverste kommandant finner ut av at du lot han gå og du får dødsstraff. ")
      quit()
    else:
      print("Venligst skriv inn et svar, Dreper han/Dreper han ikke.")
      

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

def luftforsvaretValg():
  directions = ["Fallskjermjeger","Pilot"]
  print("Hva ønsker du å bli?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Fallskjermjeger/Pilot")
    userInput = input()
    if userInput == "Fallskjermjeger":
      Fallskjermjeger()
    elif userInput == "Pilot":
      Pilot()
    else:
      print("Vennligst skriv inn et gyldig svar, Fallskjermjeger/Pilot")

def Fallskjermjeger():
  directions = ["Gi til piloten","Ta den selv"]
  print("Flyet du sitter på i blir skutt av russiske krigsfly og 1 fallskjerm detter ut. Resten av bataljonen din hopper ut og det er kun deg og piloten igjen. Det er bare en fallskjerm igjen, hva gjør du?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Gi til piloten/Ta den selv")
    userInput = input()
    if userInput == "Gi til piloten":
      print(" Du gir fallskjermen til piloten og prøver å lande flyet trygt men overlever ikke. Du blir en helt.")
      quit()
    elif userInput == "Ta den selv":
      TaDenSelv()
    else:
      print("Vennligst skriv inn et gyldig svar, Kystvakt/Båtoperatør")
      
def TaDenSelv():
  directions = ["Skyt russisk soldat","Snik unna"]
  print("Du tar fallskjermen selv og klarer å hoppe ut av flyet. Du lander i en russisk sone. Du ser en russisk soldat som har fanget en sivil. Hva gjør du?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Skyt russisk soldat/Snik unna")
    userInput = input()
    if userInput == "Skyt russisk soldat":
      print("Du skyter den russiske soldaten, men de finner deg med en gang, du blir skutt på stedet.")
      quit()
    elif userInput == "Snik unna":
      prin("Du ser den sivile blir skutt og løper unna, en snikskyter ser deg løpe unna og du blir skutt.")
      quit()
    else:
      print("Vennligst skriv inn et gyldig svar, Kystvakt/Båtoperatør")

def militærvalg():
  directions = ["Luftforsvaret","Hæren","Sjøforsvaret"]
  global weapon
  print("Så bra du vil ble med i militæret, her finns det masse muligheter hva ønsker du å gjøre?")
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
      

def sjøforsvaretValg():
  directions = ["Kystvakt","Båtoperatør"]
  print("Hva ønsker du å bli?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Kystvakt/Båtoperatør")
    userInput = input()
    if userInput == "Kystvakt":
      Kystvakt()
    elif userInput == "Båtoperatør":
      Båtoperatør()
    else:
      print("Vennligst skriv inn et gyldig svar, Kystvakt/Båtoperatør")

def Kystvakt():
    directions = ["La de gå","Ikke la de gå"]
    print("Krigen har vart i 3 år nå, det er ekstrem sult og fattigdom i nord russiske hjem. Du er på vakt å tar noen i å snikfiske i norske vann. Hva gjør du?")
    userInput = ""
    while userInput not in directions:
      print("Valg: La de gå/Ikke la de gå")
      userInput = input()
      if userInput == "La de gå":
        print("De viser seg at det var ikke fiskere men en russisk militærbåt med misiler. De fyrer torpedoer på båten din. ")
        quit()
      elif userInput == "Ikke la de gå":
        print("Du undersøker båten deres og finner ut at det er russiske spioner, du klarer å stanse de og deres plan og du får utdelt en æresmedalje.")
        quit()
      else:
        print("Vennligst skriv inn et gyldig svar, La de gå/Ikke la de gå")

def Båtoperatør():
  directions = ["Varsler de andre","Varsler ikke de andre"]
  print("Du får vite at båten du styrer er et mål for russerne, du får også beskjed om å ikke varsle de andre om bord siden dette kan skape panikk. Hva gjør du?")
  userInput = ""
  while userInput not in directions:
    print("Options: varsle/ikke varsle")
    userInput = input()
    if userInput == "varsle":
      print("Du varsler de andre på båten og dere klarer å legge en plan sammen som får russerne til å styre unna, båten er reddet.")
      quit()
    elif userInput == "ikke varsle":
      print("Du velger å ikke varsle de andre, dette fører til at når russerne angriper båten din blir det full panikk om bord og båten ender opp med å synke.")
      quit()
    else:
      print("Vennligst skriv inn et gyldig svar, varsle/ikke varsle")
      
def ikkemilitær():
  print("Norge hadde for lite soldater til krigen, Russland har tatt over landet og du har blitt sendt til en konsentrasjonsleir i Sibir")
  quit()

def introScene():
  directions = ["Ja","nei"]
  print("Du har blitt spurt om å dra til militæret, har du lyst til dette?")
  userInput = ""
  while userInput not in directions:
    print("Options: Ja/Nei")
    userInput = input()
    if userInput == "Nei":
      ikkemilitær()
    elif userInput == "Ja":
      militærvalg()
    else: 
      print("Vennligst skriv inn et gyldig svar, Ja/Nei")

if __name__ == "__main__":
  while True:
    print("Velkommen til dette tekstbaserte spillet av Oda og Jostein!")
    print("La oss starte med navnet ditt: ")
    name = input()
    print("Lykke til, " +name+ ".")
    introScene()