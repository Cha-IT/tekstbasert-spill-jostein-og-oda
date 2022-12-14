def jægerHistorie():
  directions = ["Dreper han", "Dreper han ikke"]
  print()
  print("Du får et oppdrag om å følge en spesialtrent russisk soldat som befinner seg på norsk territorium, når du ser soldaten finner du ut at det er en du har hatt førstegangstjeneste med. Hva gjør du?")
  userInput = ""
  while userInput not in directions:
    print("Valg: Dreper han/Dreper han ikke")
    userInput = input()
    if userInput.lower() == "Dreper han".lower():
      print("Du velger å drepe han og deretter fullføre oppdraget, dette var en sentral person for den russiske siden og du får æresmedalje for din tjeneste.")
      jægerhistorieEtterliv()
    elif userInput.lower() == "Dreper han ikke".lower():
      print("Du velger å la han gå, han klarer å skaffe viktig informasjon om Norge sin plan fremover i krigen, din øverste kommandant finner ut av at du lot han gå og du får dødsstraff. ")
      quit()
    else:
      print("Venligst skriv inn et svar, Dreper han/Dreper han ikke.")

def jægerhistorieEtterliv():
    directions = ["tar kontakt med folk","holder deg for deg selv"]
    print("Det er 5 år siden den kalde dagen. Du har vunnet krigen og fått æresmedalje og er en nasjonal helt. Men du er alene og uten familie det føles ikke ut som du har vunnet noe av krigen. Du har mange dårlige tanker om framtiden av livet ditt, du går på piller for posttraumatisk stresslidelse. Hva er det neste du gjør?")
    userInput = ""
    while userInput not in directions:
      print("Valg: tar kontakt med folk/holder deg for deg selv")
      userInput = input()
      if userInput.lower() == "tar kontakt med folk".lower():
        print("Du finner noen venner som er veldig interest i frisbeegolf, du blir veldig god etter noen år og deltar i norgesmesterskapet og vinner gull. Du går proffesjonel og lever resten av livet som en krigshelt og frisbeegolf proff.")
        quit()
      elif userInput.lower() == "holder deg for deg selv".lower():
        print("Du holder deg hjemme og har vært deprimert i flere måneder og har kjent på at det ikke fantes noen vei ut av den uendelige mørket. Du ombestemmer deg å prøver å søke hjelp, men det har ikke hjulpet. Etter mye grubling kommer du frem til at det eneste som kan løse problemet ditt, var å ta sitt eget liv. En dag bestemte du deg for å gjøre det. Du forberedte deg, og tar avskjed med familien din uten å si hva du skal. Du henger deg selv i kjelleren, og i det du dør, begynte din lange reise til den andre siden.")
        quit()
      else:
        print("Vennligst skriv inn et gyldig svar, La de gå/Ikke la de gå")

def hærensValg():
  actions = ["Jægersoldat","Artillerist"]
  print("De er altid fint å ha flere i hæren hvilken stilling ønsker du å ha?")
  userInput = ""
  while userInput not in actions:
    print("Options: Jægersoldat/Artillerist")
    userInput = input()
    if userInput.lower() == "Jægersoldat".lower():
      jægerHistorie()
    elif userInput.lower() == "Artillerist".lower():
      artilleristHistorie()
    else:
      print("Vennligst skriv inn et gyldig svar, Jægersoldat/Artillerist.")

def luftforsvaretValg():
  directions = ["Fallskjermjeger","Pilot"]
  print("Hva ønsker du å bli?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Fallskjermjeger/Pilot")
    userInput = input()
    if userInput.lower() == "Fallskjermjeger".lower():
      Fallskjermjeger()
    elif userInput.lower() == "Pilot".lower():
      Pilot()
    else:
      print("Vennligst skriv inn et gyldig svar, Fallskjermjeger/Pilot")

def Pilot():
  directions = ["Skyter","Skyter ikke"]
  print("Du får beskjed om å skyte opp en russisk leir, men du vet at det er sivile der inne, hva gjør du?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Skyter/Skyter ikke")
    userInput = input()
    if userInput.lower() == "Skyter".lower():
      PilotSkyter()
    elif userInput.lower() == "Skyter ikke".lower():
      PilotSkyterIkke()
    else:
      print("Vennligst skriv inn et gyldig svar, Skyter/Skyter ikke")

def PilotSkyterIkke():
  directions = ["Aksepter straff","Nekt straff"]
  print("Du skyter leiren og treffer de sivile også.Du blir bedt om å rapportere din side om oppdraget, forteller du dem om de sivile i sonen?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Aksepter straff/Nekt straff")
    userInput = input()
    if userInput.lower() == "Aksepter straff".lower():
      print("Du mener du gjorde det riktige, men innser du brøyt reglene så du får 1 år i fengsel og ingen bot.")
      quit()
    elif userInput.lower() == "Nekt straff".lower():
      Print("Du mener gjorde det rette men har ingen bevis, du går i rettsak men taper å får bot og 10 år i fengsel.")
      quit()
    else:
      print("Vennligst skriv inn et gyldig svar, Aksepter straff/Nekt straff")

def PilotSkyter():
  directions = ["Ja","Nei"]
  print("Du skyter leiren og treffer de sivile også.Du blir bedt om å rapportere din side om oppdraget, forteller du dem om de sivile i sonen?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Ja/Nei")
    userInput = input()
    if userInput.lower() == "Ja".lower():
      print("Du rapporterer drapene du har gjort på de sivile og blir fratatt rollen som pilot.")
      quit()
    elif userInput.lower() == "Nei".lower():
      print("Du rapporterer alt utenom de sivile og svekker den russiske frontlinjen ")
      quit()
    else:
      print("Vennligst skriv inn et gyldig svar, Ja/Nei")

def Fallskjermjeger():
  directions = ["Gi til piloten","Ta den selv"]
  print("Flyet du sitter på i blir skutt av russiske krigsfly og 1 fallskjerm detter ut. Resten av bataljonen din hopper ut og det er kun deg og piloten igjen. Det er bare en fallskjerm igjen, hva gjør du?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Gi til piloten/Ta den selv")
    userInput = input()
    if userInput.lower() == "Gi til piloten".lower():
      print(" Du gir fallskjermen til piloten og prøver å lande flyet trygt men overlever ikke. Du blir en helt.")
      quit()
    elif userInput.lower() == "Ta den selv".lower():
      TaDenSelv()
    else:
      print("Vennligst skriv inn et gyldig svar, Gi til piloten/Ta den selv")
      
def TaDenSelv():
  directions = ["Skyt russisk soldat","Snik unna"]
  print("Du tar fallskjermen selv og klarer å hoppe ut av flyet. Du lander i en russisk sone. Du ser en russisk soldat som har fanget en sivil. Hva gjør du?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Skyt russisk soldat/Snik unna")
    userInput = input()
    if userInput.lower() == "Skyt russisk soldat".lower():
      print("Du skyter den russiske soldaten, men de finner deg med en gang, du blir skutt på stedet.")
      quit()
    elif userInput.lower() == "Snik unna".lower():
      prin("Du ser den sivile blir skutt og løper unna, en snikskyter ser deg løpe unna og du blir skutt.")
      quit()
    else:
      print("Vennligst skriv inn et gyldig svar, Skyt russisk soldat/Snik unna")

Militærvalg={
  "Luftforsvaret":"luftforsvaret",
  "Hæren":"hæren",
  "Sjøforsvaret":"sjøforsvaret"
}

def militærvalg():
  directions = ["Luftforsvaret","Hæren","Sjøforsvaret"]
  print("Så bra du vil ble med i militæret, her finns det masse muligheter hva ønsker du å gjøre?")
  userInput = ""
  while userInput not in directions:
    print(f"Du kan velge mellom (1){Militærvalg['Luftforsvaret']}, (2){Militærvalg['Hæren']}, (3){Militærvalg['Sjøforsvaret']}.")
    userInput = input()
    if userInput.lower() == Militærvalg["Luftforsvaret"].lower() or 1:
        luftforsvaretValg()
    elif userInput.lower() == Militærvalg["Hæren"].lower():
        hærensValg()
    elif userInput.lower() == Militærvalg["Sjøforsvaret"].lower():
        sjøforsvaretValg()
    else:
      print("Vennligst skriv inn et gyldig svar, Luftforsvaret/Hæren/sjøforsvaret")
      

def sjøforsvaretValg():
  directions = ["Kystvakt","Båtoperatør"]
  print("Hva ønsker du å bli?")
  userInput = ""
  while userInput not in directions:
    print("Valgmuligheter: Kystvakt/Båtoperatør")
    userInput = input()
    if userInput.lower() == "Kystvakt".lower():
      Kystvakt()
    elif userInput.lower() == "Båtoperatør".lower():
      Båtoperatør()
    else:
      print("Vennligst skriv inn et gyldig svar, Kystvakt/Båtoperatør")

def Kystvakt():
    directions = ["La de gå","Undersøker nærmere"]
    print("Krigen har vart i 3 år nå, det er ekstrem sult og fattigdom i nord russiske hjem. Du er på vakt å tar noen i å snikfiske i norske vann. Hva gjør du?")
    userInput = ""
    while userInput not in directions:
      print("Valg: La de gå/Undersøker nærmere")
      userInput = input()
      if userInput.lower() == "La de gå".lower():
        print("De viser seg at det var ikke fiskere men en russisk militærbåt med misiler. De fyrer torpedoer på båten din. ")
        quit()
      elif userInput.lower() == "Undersøker nærmere".lower():
        undersøke()
      else:
        print("Vennligst skriv inn et gyldig svar, La de gå/Undersøker nærmere")

def undersøke():
    directions = ["Sniker seg innpå","Gjør deg synlig"]
    print("Ved en nærmere kikk ser du at det viser seg at de ikke fisker men gjør noe annet, De har ikke sett deg enda. Du har valget mellom å gjøre deg synlig eller snike deg innpå Hva gjør du?")
    userInput = ""
    while userInput not in directions:
      print("Valg: Sniker seg innpå/Gjør deg synlig")
      userInput = input()
      if userInput.lower() == "Gjør deg synlig".lower():
        print("Du gjør deg synlig, undersøker båten og klarer å synke båten imens den prøver å kjøre unna, dette var en svært sentral båt i det russiske forsvaret og Norge får en stor fordel i krigen.")
        quit()
      elif userInput.lower() == "Sniker seg innpå".lower():
        Snike()
      else:
        print("Vennligst skriv inn et gyldig svar, Sniker seg innpå/Gjør deg synlig")


def Snike():
    directions = ["Rapporter det","Ikke rapporter"]
    print("Du og båten din klarer å snike deg innpå den russiske båten, dere klarer og komme dere på båten deres og ser at det er en russisk soldat med sin familie som henter opp krabbeteiner. Ønsker du å rapportere det til din øverste kommandant? ")
    userInput = ""
    while userInput not in directions:
      print("Valg: Rapporter det/Ikke rapporter")
      userInput = input()
      if userInput.lower() == "Rapporter det.lower()":
        print("Ved å rapportere det får du tilliten til din øverste kommandant og du får en høyere rolle i kystvakten")
        quit()
      elif userInput.lower() == "Ikke rapporter".lower():
        print("Du velger å ikke rapportere funnet av den russiske soldaten og hans familie og det viser seg at det russiske spioner som har gjemt seg på båten, de kaprer båten og klarer å snike seg inn i den norske kystvakten")
        quit()
      else:
        print("Vennligst skriv inn et gyldig svar, Rapporter det/Ikke rapporter")


def Båtoperatør():
  directions = ["Varsle","Ikke varsle"]
  print("Du får vite at båten du styrer er et mål for russerne, du får også beskjed om å ikke varsle de andre om bord siden dette kan skape panikk. Hva gjør du?")
  userInput = ""
  while userInput not in directions:
    print("Valg: Varsle/Ikke varsle")
    userInput = input()
    if userInput.lower() == "Varsle".lower():
      print("Du varsler de andre på båten og dere klarer å legge en plan sammen som får russerne til å styre unna, båten er reddet.")
      quit()
    elif userInput.lower() == "Ikke varsle".lower():
      print("Du velger å ikke varsle de andre, dette fører til at når russerne angriper båten din blir det full panikk om bord og båten ender opp med å synke.")
      quit()
    else:
      print("Vennligst skriv inn et gyldig svar, Varsle/Ikke varsle")
      
def ikkemilitær():
  print("Norge hadde for lite soldater til krigen, Russland har tatt over landet og du har blitt sendt til en konsentrasjonsleir i Sibir")
  quit()

def artilleristHistorie():
  directions = ["planter ikke bomben","planter bomben"]
  print("Du fikk høre om denne krigen når du hadde en tur til Moskva for 5 år siden, da fikk du et eget oppdrag om å bli med i det norske forsvaret, du får oppdrag om å plante en bombe i en norsk leir. Hva gjør du?")
  userInput = ""
  while userInput not in directions:
    print("planter ikke bomben/planter bomben")
    userInput = input()
    if userInput.lower() == "planter ikke bomben".lower():
      print("Du velger å ikke plante bomben og de russiske soldatene finner ut av det og dreper deg")
      quit()
    elif userInput.lower() == "planter bomben".lower():
      print("Du planter bomben og det norske forsvaret finner ut at det var deg og dreper deg på stedet")
      quit()
    else:
      print("Vennligst skriv inn et gyldig svar, planter ikke bomben/planter bomben")
def introScene():
  directions = ["Ja","nei"]
  print("Du har blitt spurt om å dra til militæret, har du lyst til dette?")
  userInput = ""
  while userInput not in directions:
    print("Valg: Ja/Nei")
    userInput = input()
    if userInput.lower() == "Nei".lower():
      ikkemilitær()
    elif userInput.lower() == "Ja".lower():
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