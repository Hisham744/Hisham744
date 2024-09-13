import random , time
name = input("Herzlich wilkommen zum Spiel Tieriel. Wie lautet dein Name? ")
hunger = 0
sleep = 0
Happiness = 0
ahunger = 0
asleep = 0
aHappiness = 0
money = 100
Level = 1
Levelpunkte = 0
getfreeshop = 0
saloonname = "Mein Saloon"
Gesamtkosten = 20
accept = 1
sg = 0
def stop() :
    print("...")
def startGame() :
    global petname,name,Level
    print(f"Hallo {name}")
    print("")
    time.sleep(2)
    print("in diesem Spiel hast du ein Tier , dass du trainieren musst.")
    time.sleep(2.5)
    petname = input("Hezlichen Glückwunsch. Du hast dein erstes Tier bekommen es ist eine Katze. Wie willst du sie nennen? ")
    time.sleep(3)
    print("Dein Tier heißt " + str(petname) + ". Sie ist auf Level eins. Um ein höheres Level zu erreichen musst du sie füttern , sie zum Schlafen bringen oder sie mit ihr spielen.")
    time.sleep(3)
    home()
def Levelcheck() :
    global Level, Levelpunkte, money, name
    Levelpunkte += 1
    if name == "Hishamistcool" :
        Level += 3
    if Levelpunkte >= 5 :
        Levelpunkte -= 5
        Level += 1
        print(f"Herzlichen Glückwunsch. Du bist Level {Level}")
        print("Belohnungen : 10€ ")
        money = money + 10
        if Level == 3 :
            print("Du kannst nun arbeiten.")
            time.sleep(1)
            makesaloon()    
        home()
    else :
        print(f"Du hast {Levelpunkte} Levelpunkte du brauchst 5.")
        home()

def eat() :
    global hunger, money , ahunger
    if hunger > 0 :
         if money >= 20 :
            option1 = int(input(f"{petname} hat Hunger.Hunger : {hunger}. Willst du {petname} füttern. Ja (1) Nein(2) "))
            if option1 == 1:
                option2 = int(input(f"Essen kostet 20€ du hast {money}€.Willst du trozdem bezahlen? Ja(1) Nein(2) "))
                if option2 == 1 :
                    hunger = 0
                    money -= 20
                    ahunger = 1
                    Levelcheck()
                else :
                    home()
            else :
                home()
         else : 
             print(f"Du hast nicht genug Geld. Du hast nur {money}€")
             home()
    else :
        print("Dein Haustier hat gerade keinen Hunger")
        home()
def gosleep() :
     global sleep, money, asleep
     if sleep > 0 :
         if money >= 10 :
            option1 = int(input(f"{petname} ist müde. Müdigkeit : {sleep}. Willst du {petname} ins bett bringen. Ja (1) Nein (2) "))
            if option1 == 1:
                option2 = int(input(f"Schlafen  kostet 10€. Du hast {money}€. Willst du trozdem schlafen? Ja(1) Nein(2) "))
                if option2 == 1 :
                    print("Dein Haustier schläft. ZZzzzz...")
                    print("Warte 5 Sekunden.")
                    time.sleep(5)
                    money -= 10
                    sleep = 0
                    asleep = 1
                    print("Dein Haustier ist wach")
                    Levelcheck()
                else :
                    home()
            else :
                home()
         else : 
             print(f"Du hast nicht genug Geld. Du hast nur {money}€")
             home()
     else :
        print("Dein Haustier ist gerade nicht müde.")
        home()
def play() :
    import random
    abc = random.randint(1, 4)
    if abc == 1 or abc == 2 :
        def initGame() :
            print("Herzlich willkommen zum Spiel rate was ich denke.")
            Regel = "Ich denke mir eine Zahl zwischen 1 und 1000"
            print(Regel)
        def playminigame(Versuche, Eingabe) :
            Zufall = random.randint(1,1000)
            while Eingabe != Zufall :
                print("Rate mal :" , end= "")
                Eingabe = int(input())
                Versuche += 1
                if Eingabe == 0 :
                    print("Spiel abgebrochen")
                    home()
                if Eingabe < Zufall :
                    print("zu klein!")
                if Eingabe > Zufall :
                    print("zu groß!")
                if Eingabe == Zufall :
                    print("Richtig!")
                    return Versuche
        def endminigame(Versuche) :
            global money, Happiness, aHappiness
            print("Du hast " + str(Versuche) + " Versuche gebraucht!")
            if int(Versuche) <= 10 :
                print("Du hast 5€ gewonnen!")
                time.sleep(3)
                money += 5
                Happiness = 0
                aHappiness = 1
                Levelcheck()
        
            else :
                print("Du hast 2€ gewonnen!")
                Happiness = 0
                aHappiness = 0
                money += 2
                Levelcheck()
        initGame()
        Spiel = playminigame(0, 0)
        endminigame(Spiel)
    elif abc == 3 :
        def würfel() :
            import random, time
            global money , Happiness, aHappiness
            print("Lass uns würfeln!")
            Versuche = 0 
            DeinWert = 0
            MeinWert = 0
            print("Wie viel Geld setzt du? " , end="")
            ggeld = int(input())
            if ggeld > money :
                print("Du hast zu wenig Geld du hast nur" + str(money))
                würfel()
            money -= ggeld
            print("Wer denkst du wird gewinnen? Du(1) oder Ich(2) " , end="")
            gamestimme = int(input())
            gewinn = ggeld * 2
            for Nr in range(1,6) :
                print(str(Nr) + ". Runde")
                print("Du bist dran: " , end=" ")
                Wurf1 = random.randint(1,6) 
                time.sleep(0.5)  
                print(Wurf1)
                print("Ich bin dran: " , end=" ")
                Wurf2 = random.randint(1,6) 
                time.sleep(0.5)   
                print(Wurf2)
                if Wurf1 < Wurf2 :
                    DeinWert = DeinWert + 1
                if Wurf1 > Wurf2 :
                    MeinWert = MeinWert + 1
                print(str(DeinWert) + " zu " + str(MeinWert))
                time.sleep(1)
                print()
            if DeinWert > MeinWert :
                if gamestimme == 2 :
                   print("Prima richtig geraten. Du hast " + str(gewinn) + "€ gewonnen.")
                   money += gewinn
                   time.sleep(1)
                   Happiness = 0
                   aHappiness = 1
                   Levelcheck()
                else : 
                    print("Du hast Falsch geraten. Du hast gewonnen , nicht ich.")
                    Happiness = 0
                    aHappiness = 1
                    home()
            elif DeinWert < MeinWert :
                if gamestimme == 1 :
                    print("Prima richtig geraten. Du hast " + str(gewinn) + "€ gewonnen.")
                    money += gewinn
                    time.sleep(1)
                    Happiness = 0
                    aHappiness = 1
                    Levelcheck()
                else :
                     print("Du hast Falsch geraten. Ich habe gewonnen , nicht du.")
                     Happiness = 0
                     aHappiness = 1
                     home()
            else :
                print("Unentschieden! Du bekommst dein Geld zurück.")
                money += ggeld
                Happiness = 0
                aHappiness = 1
                home()
        würfel()
    else :
        import random
        global money, aHappiness, Happiness
        Zahl1 = random.randint(10,21)
        Zahl2 = random.randint(1,10)
        Operator = random.randint(1,4)
        Aufgabe = 0
        if Operator == 1 :
            print(Zahl1 , end="")
            print(" + " , end="")
            print(Zahl2)
            Aufgabe = Zahl1 + Zahl2
        if Operator == 2 :
            print(Zahl1 , end="")
            print(" - " , end="")
            print(Zahl2)
            Aufgabe = Zahl1 - Zahl2
        if Operator == 3 :
            print(Zahl1 , end="")
            print(" * " , end="")
            print(Zahl2)
            Aufgabe = Zahl1 * Zahl2
        if Operator == 4 :
            print(Zahl1 , end="")
            print(" / " , end="")
            print(Zahl2)
            Aufgabe = Zahl1 / Zahl2
        avs = int(input("Rechne: "))
        Ergebnis = Aufgabe
        if Ergebnis == avs :
            print("Richtig! du Verdienst 1€")
            money += 1
            time.sleep(1)
            Happiness = 0
            aHappiness = 1
            Levelcheck()
        else :
            print("Leider Falsch. Das Ergebnis ist: " , end="")
            print(Ergebnis) 
            Happiness = 0
            aHappiness = 1
            home()
def makesaloon() :
    import random, time
    global money, name, saloonname, sg
    if sg == 0 :
        print("Hallo " + name)
        print("Du musst arbeiten. In einem Tiersaloon")
        print("Das Tiersaloon kostet 150€. Willst du trozdem bezahlen? Ja(1) Nein(2) " , end="")
        option = int(input())
        if option != 1 :
            print("Kauf abgebrochen")
            home()
        if money >= 150 :
            money -= 150
            saloonname = str(input("Wie willst du dein Saloon nennen(z.B Mein Salooon): "))
            sg = 1
        else :
            print("Du hast nicht genügend geld")
            sg = 0
            home()
def work() :
    import random, time
    global money, saloonname , Gesamtkosten, Levelpunkte , accept
    plus = 0
    if not money >= 16 :
        accept = 1
        print("Du hast nich genug Geld für die anderen Kosten.")
        home()
    print("Du fährst zur Arbeit...")
    time.sleep(3)
    print("Herzlich wilkommen in deinem Tiersaloon : " + saloonname)
    print("Kosten pro Tier : ")
    print("Wasserkosten : 5€")
    print("Stromkosten : 10€")
    print("Materialkosten : 1€")
    print("Hauskosten : 4€")
    print("Gesamtkosten : 20€")
    Gesamtkosten = 20

    while accept == 1 :
        Gast = random.randint(100,1000)
        Bezahlung = random.randint(21,35)
        plus = Bezahlung - Gesamtkosten
        print("Gast Nr." + str(Gast) + " bietet dir " + str(Bezahlung) + "€")
        print("Damit wirst du " + str(plus) + "€ verdienen")
        print("Willst du den Gast annehmen? Ja(1) Nein(2) " , end="")
        option = int(input())
        if option == 1 :
            print("Gast wurde angenommen")
            print("Gast wird gewaschen"  , end="")
            time.sleep(0.3)
            print("." , end="")
            time.sleep(0.3)
            print("." , end="")
            time.sleep(0.3)
            print(".")
            print("Haare werden geföhnt" , end="")
            time.sleep(0.5)
            print("." , end="")
            time.sleep(0.5)
            print("." , end="")
            time.sleep(0.5)
            print("." )
            print("Haare werden Geschnitten"  , end="")
            time.sleep(0.5)
            print("." , end="")
            time.sleep(0.5)
            print("." , end="")
            time.sleep(0.5)
            print(".")
            print("Gast Nr." + str(Gast) + " dankt dir")
            money += plus
            Levelpunkte += 1
            time.sleep(1)
            option1 = int(input("Weiter? Ja(1) Nein(2) "))
            if option1 == 1 :
                work()
            
            else :
                Levelcheck()
        else :
            print("Auftrag abgeleht")
            time.sleep(1)
            home()
def shop() :
    global money , petname , Levelpunkte , getfreeshop
    getfreeshop = random.randint(1,10)
    if getfreeshop == 1 :
       print("(1)GRATIS! 3 Levelpunkte")
    print("(2)100€ Haustiernamen ändern. Aktuell: " + petname)  
    if petname != petname + "🐱" :
       print(f"(3)50€ dieses Emoji nach den Namen machen. so sieht es aus : {petname}🐱" ) 
    option1 = input("Was willst du? ")
    if option1 == "1" and getfreeshop == 0 :
        Levelpunkte += 3
        getfreeshop = 1
        Levelcheck()
    elif option1 == "2" :
        petname = input("Wie soll dein Haustier heißen: ")
        print("Herzlichen Glückwunsch. Dein Haustier heißt nun : " + petname)
        money -= 100
        time.sleep(2)
        if petname == "mmm" :
            print("Herlichen Glückwunsch Geheimcode eraten. Du erhälst 200€🙂")
            money += 200
            time.sleep(2)
            Levelcheck()
        home()
    elif option1 == 3 :
        petname = petname + "🐱"
        print("Herzlichen Glückwunsch. Dein Haustier heißt nun " + petname)
        time.sleep(1.5)
        home()
    else :
        print("Nicht verfügbar.")
        home()
def home() :
    global sleep, hunger, Happiness, asleep, ahunger, aHappiness, sg
    time.sleep(2)
    minus = random.randint(1,3)
    if minus == 1 :
        sleep += random.randint(1,3)
    elif minus == 2 : 
        hunger += random.randint(1,3)
    else :
        Happiness += random.randint(1,3)
    if asleep == 1 :
        sleep = 0
    elif ahunger == 1 :
        hunger = 0
    elif aHappiness == 1 :
        Happiness = 0
    print("Du bist nun zuhause")
    print()
    print("Geld: " + str(money) + "€")
    print("(1)Schlafen Müdeigkeit : " + str(sleep))
    print("(2)Essen Hunger : " + str(hunger))
    print("(3)Spielen  Langweile : " + str(Happiness))
    print("(4)Shop")
    if  Level >= 3 :
        print("(5)Arbeiten")
    print("Haustierlevel : " + str(Level) )
    asleep = 0
    ahunger = 0
    aHappiness = 0
    option = int(input("Wähle aus: "))
    if option == 1 : 
        gosleep()
    elif option == 2 :
        eat()
    elif option == 3 :
        play()
    elif option == 4 :
        shop()
    elif option == 5 and Level >= 3 :
        if sg == 1 :
            work()
        else :
            makesaloon()

    else :
        print("Spiel beenden? Ja(1) Nein(2) " , end="")
        beenden = int(input())
        if beenden == 1 :
            print("Spiel beendet")
            stop()
        else :
            home()


startGame()
