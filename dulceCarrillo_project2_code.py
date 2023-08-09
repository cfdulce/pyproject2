#create a game introduction
#create game rules
#create a coundown which will print before starting the game
#create different functions based on difficulty level and genre so to make it easier to put it all together on the final part of the code
#final code all together should include all the defined functions!

def gameIntro():
    print('Hello!!! Welcome to "Guess the song by the Lyric" quiz game! Please read the Game Rules before proceeding to play.')
def gameRules():
    print("""
    --- G A M E  R U L E S ---
    >>>Type all answers in CAPITAL letters!
    >>>Please make sure that you type all responses correctly. Any mispelling of words will affect your playing experience!
    >>>Do not look up answers! Give it your best shot! :)(HINT:Some answers are within the lyrics)
    >>>Have Fun!!! :D
    """)

def countdown():
    print("""
    READY???

    STARTING IN...

        3...
        2...
        1...

    START!""")
 

def easy_rock():
    #question 1
    print("""Q.1 ``TWO HUNDRED DEGREES, THAT'S WHY THEY CALL ME MISTER FAHRENHEIT, I'M TRAVELLING AT THE SPEED OF LIGHT``""")
    eRq1=input("What song is this?")
    while True:
        if eRq1=="DON'T STOP ME NOW":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... DON'T STOP ME NOW")
            break
    print()
    #question 2
    print("""Q.2 ``IT'S OKAY TO EAT FISH, CAUSE THEY DON'T HAVE ANY FEELINGS``""")
    eRq2=input("What song is this?")
    while True:
        if eRq2=="SOMETHING IN THE WAY":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is...SOMETHING IN THE WAY")
            break
    print()
    #question 3
    print("""Q.3 ``LITTLE DARLING, IT'S BEEN A LONG, COLD, LONELY WINTER``""")
    eRq3=input("What song is this?")
    while True:
        if eRq3=="HERE COMES THE SUN":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... HERE COMES THE SUN")
            break
    print()
    #question 4
    print("""Q.4 ``BACK IN THE BACK OF A CADILLAC, NUMBER ONE WITH A BULLET, i'M POWER PACK``""")
    eRq4=input("What song is this?")
    while True:
        if eRq4=="BACK IN BLACK":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... BACK IN BLACK")
            break
    print()
    #question 5
    print("""Q.5 ``I LOVE ROCK 'N ROLL... SO PUT ANOTHER DIME IN THE JUKEBOX, BABY``""")
    eRq5=input("What song is this?")
    while True:
        if eRq5=="I LOVE ROCK 'N ROLL":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... I LOVE ROCK 'N ROLL")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED EASY: ROCK!!!")
#easy_rock()
#----------------------------------------------section break---------------------------------------------------------------------------
def easy_Pop():
    #question 1
    print("""Q.1 ``TALKIN' IN MY SLEEP AT NIGHT, MAKIN' MYSELF CRAZY``""")
    ePq1=input("What song is this?")
    while True:
        if ePq1=="NEW RULES":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... NEW RULES")
            break
    print()
    #question 2
    print("""Q.2 ``CAN YOU KISS ME MORE? WE'RE SO YOUNG,  BOY, WE AIN'T GOT NOTHING TO LOSE..UH OH``""")
    ePq2=input("What song is this?")
    while True:
        if ePq2=="KISS ME MORE":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... KISS ME MORE")
            break
    print()
    #question3
    print("""Q.3 ``BEIN' SO BAD GOT ME FEELIN' SO GOOD, SHOWIN' YOU UP LIKE I KNEW THAT I WOULD``""")
    ePq3=input("What song is this?")
    while True:
        if ePq3=="SORRY NOT SORRY":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... SORRY NOT SORRY")
            break
    print()
    #question 4
    print("""Q.3 ``ONE TAUGHT ME LOVE, ONE TAUGHT ME PATIENCE, AND ONE TAUGHT ME PAIN. NOW I'M SO AMAZING``""")
    ePq4=input("What song is this?")
    while True:
        if ePq4=="THANK U NEXT":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... THANK U NEXT")
            break
    print()
    #question 5
    print("""Q.4 ``I DON'T WANT NO SCRUB. A SCRUB IS A GUY THAT CAN'T GET NO LOVE FROM ME``""")
    ePq5=input("What song is this?")
    while True:
        if ePq5=="NO SCRUBS":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... NO SCRUBS")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED EASY: POP!!!")

#easy_Pop()
#-----------------------------------------section break--------------------------------------------------------------------------
def easy_latin():
    #question 1
    print("""Q.1 ``MARIPOSA TRAICIONERA, TODO SE LO LLEVA EL VIENTO. MARIPOSA NO REGRESO``""")
    eLq1=input("What song is this?")
    while True:
        if eLq1=="MARIPOSA TRAICIONERA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... MARIPOSA TRAICIONERA")
            break
    print()
    #question 2
    print("""Q.2 ``MAL PARECE QUE SOLO ME QUEDE, Y FUE PURA TODITA TU MENTIRA, QUE MALDITA, MALA SUERTe LA MIA QUE AQUEL DIA TE ENCONTRE``""")
    eLq2=input("What song is this?")
    while True:
        if eLq2=="LA CAMISA NEGRA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... LA CAMISA NEGRA")
            break
    print()
    #question 3
    print("""Q.3 ``A ELLA LE GUSTA LA GASOLINA (DAME MAS GASOLINA), COMO LE ENCANTA LA GASOLINA (DAME MAS GASOLINA)``""")
    eLq3=input("What song is this?")
    while True:
        if eLq3=="GASOLINA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... GASOLINA")
            break
    print()
    #question 4
    print("""Q.4 ``SON LAS CINCO DE LA MANANA, Y YO NO HE DORMIDO NADA, PENSANDO EN TU BELLEZA LOCO VOY A PARAR``""")
    eLq4=input("What song is this?")
    while True:
        if eLq4=="OBSESION":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... OBSESION")
            break
    print()
    #question 5
    print("""Q.5 ``MACARENA TIENE UN NOVIO QUE SE LLAMA, QUE SE LLAMA DE APELLIDO VITORINO``""")
    eLq5=input("What song is this?")
    while True:
        if eLq5=="MACARENA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... MACARENA")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED EASY: LATIN!!!")

#easy_latin()
#-------------------------------------section break----------------------------------------------------------------------------
def easy_hiphop():
    #question 1
    print(""""Q.1 ``IF YOU HAVIN' GIRL PROBLEMS, I FEEL BAD FOR YOU, SON. I GOT 99 PROBLEMS BUT A [CENSORED] AIN'T ONE``""")
    eHq1=input("What song is this?")
    while True:
        if eHq1=="99 PROBLEMS":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... 99 PROBLEMS")
            break
    print()
        #question 2
    print(""""Q.1 ``NEVER MEANT TO MAKE YOUR DAUGHTER CRY, I APOLOGIZED A TRILLION TIMES``""")
    eHq2=input("What song is this?")
    while True:
        if eHq2=="I'M SORRY MS. JACKSON":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... I'M SORRY MS. jACKSON")
            break
    print()
    #question 3
    print(""""Q.3 ``WITH RICK ROCK BEATS, YEAH FELLA, I;LL ROCK YA``""")
    eHq3=input("What song is this?")
    while True:
        if eHq3=="HYPHY":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... HYPHY")
            break
    #question 4
    print("""Q.4 ``LEMME SEE YOU SHAKE IT, SHAKE IT. NOW WON'T YOU DROP IT, OOH TAKE IT, TAKE IT``""")
    eHq4=input("What song is this?")
    while True:
        if eHq4=="WOBBLE, WOBBLE":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... WOBBLE, WOBBLE")
            break
    print()
    #question 5
    print("""Q.5 ``THEY SHOULD CALL YOU SUGAR, YOU'RE SO SWEET...WELL, THEY SHOULD CALLL YOU SUGAR 'CAUSE YOU'RE SO SWEET TO ME``""")
    eHq5=input("what song is this?")
    while True:
        if eHq5=="SWEET/ I THOUGHT YOU WANTED TO DANCE":
            print("Correct!")
            break
        else:
            print("Sorry! the answer is... SWEET/ I THOUGHT YOU WANTED TO DANCE")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED EASY: HIPHOP!!!")
#easy_hiphop()
#-----------------------------------------------------------------------------------------------------
def easy_popESP():
    print("""Q.1 ``Y YO qUE TE DESO A MORIR... QUE IMPORTA? ESTA ES LA ULTIMA VEZ...``""")
    ePEq1=input("What song is this?")
    while True:
        if ePEq1=="QUE BELLO":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... QUE BELLO")
            break
    print()
    print("""Q.2 ``VEN Y CUENTAME LA VERDAD...TEN PIEDAD...Y DIME PORQUE? NO, NO, NO, OHH...``""")
    ePEq2=input("What song is this?")
    while True:
        if ePEq2=="TU FALTA DE QUERER":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... TU FALTA DE QUERER")
            break
    print("""Q.3 ``QUIERO EN TUS MANOS BUSCAR MI CAMINO....Y QUE TE SIENTAS MUJER SOLAMENTE CONMIGO...``""")
    ePEq3=input("What song is this?")
    while True:
        if ePEq3=="TENGO GANAS DE TI":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is...TENGO GANAS DE TI")
            break
    print("""Q.4 ``TRAICIONERA, EN MI VIDA FUISTE PASAJERA. ME, NO ME IMPORTA QUE DE AMOR TE MUERAS``""")
    ePEq4=input("What song is this?")
    while True:
        if ePEq4=="TRAICIONERA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is...TRAICIONERA")
            break
    print()
    print("""Q.5 ``YA, YA ME ESTA GUSTANDO MAS DE LO NORMAL. TODOS MIS SENTIDOS VAN PIDIENDO MAS, ESTO HAY QUE TOMARLO SIN NINGUN APURO...``""")
    ePEq5=input("What song is this?")
    while True:
        if ePEq5=="DESPACITO":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is...DESPACITO")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED EASY: POP (ESP)!!!")
#------------------------------section break--------------------------------------------
def medium_rock():
    #question 1
    print("""Q.1 ``SLIPPIN' ON THE SECRETS YOU KEEP, YEAH THAT [CENSORED] GIVES ME THE CREEPS ``""")
    mRq1=input("What song is this?")
    while True:
        if mRq1=="CREEPS":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... CREEPS")
            break
    print()
        #question 2
    print("""Q.2 ``I'M YOUR SOURCE OF SELF-DESTRUCTION, VEINS THAT PUMP WITH FEAR``""")
    mRq2=input("What song is this?")
    while True:
        if mRq2=="MASTER OF PUPPETS":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... MASTER OF PUPPETS")
            break
    print()
        #question 3
    print("""Q.3 ``OH HONEY BEAR, YOU CAUGHT MEUNAWARE, I'LL LET IT SLIDE, OH LET IT DROP ``""")
    mRq3=input("What song is this?")
    while True:
        if mRq3=="THE DROP":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... THE DROP")
            break
    print()
        #question 4
    print("""Q.4 ``TO EVERY STRANGER ON THE STREETS THAT WALKS ON BY. SO I CAN MOVE ALONG``""")
    mRq4=input("What song is this?")
    while True:
        if mRq4=="PAGES":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... PAGES")
            break
    print()
        #question 5
    print("""Q.5 ``WHY DOES MY WALL INSIST I HAVE MY BACCK AGAINS IT?? ``""")
    mRq5=input("What song is this?")
    while True:
        if mRq5=="GROWING/DYING":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... GROWING/DYING")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED MEDIUM: ROCK!!!")
#-------------------------------section break-----------------------------------------
def medium_pop():
    #question 1
    print("""Q.1 ``IN THE WHIP ON A TUESDAY NIGHT, GO TTHE MUSIC HIGH, AND YOU BY MY SIDE, SIDE ``""")
    mPq1=input("What song is this?")
    while True:
        if mPq1=="POTION":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... POTION")
            break
    print()
        #question 2
    print("""Q.2 ``THE FIRST TIME IN SIX MONTHS, IDON'THATE YOU AS MUCH. YOU WEREN'T THERE IN MY DREAMS, I COULD FINALLY SLEEP``""")
    mPq2=input("What song is this?")
    while True:
        if mPq2=="TOO WELL":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... TOO WELL")
            break
    print()
        #question 3
    print("""Q.3 ``WALKIN' RIGHT OUTSIDE THE VENUE, WE USED TO GO WITH SOMEBODY I USED TO KNOW ``""")
    mPq3=input("What song is this?")
    while True:
        if mPq3=="WHAT HAPPENED TO RYAN":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... WHAT HAPPENED TO RYAN")
            break
    print()
        #question 4
    print("""Q.4 ``YOU'RE LEADING ME OUT OF THE DARK LIKE A SAVIOU SHINING IN MY SOUL, OH WOAH, OH WOAH ``""")
    mPq4=input("What song is this?")
    while True:
        if mPq4=="LIKE A SAVIOUR":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... LIKE A SAVIOUR")
            break
    print()
        #question 5
    print("""Q.5 ``CAN WE GO BACK TO HOW IT WAS? BEFORE MY PRIDE GOT IN BETWEEN US ``""")
    mPq5=input("What song is this?")
    while True:
        if mPq5=="LOVE AGAIN":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... LOVE AGAIN")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED MEDIUM: POP!!!")

#------------------------------section break---------------------------------------
def medium_Latin():
    #question 1
    print("""Q.1 ``ESO PARECE SINCERO PERO TE CONOZCO BIEN Y SE QUE MIENTES, TE FELICITO, QUE BIEN ACTUAS ``""")
    mLq1=input("What song is this?")
    while True:
        if mLq1=="TE FELICITO":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... TE FELICITO")
            break
    print()
        #question 2
    print("""Q.2 `ANTES NO CREIA QUE DEBE DE EXISTIR ALGUIEN, ASI COMO TU ``""")
    mLq2=input("What song is this?")
    while True:
        if mLq2=="PERFECTA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... PERFECTA")
            break
    print()
        #question 3
    print("""Q.3 ``PERO COMO EL AJEDREZ, LA REINACAE ALGUNA VEZ``""")
    mLq3=input("What song is this?")
    while True:
        if mLq3=="SWING":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... SWING")
            break
    print()
        #question 4
    print("""Q.4 ``ME DIJERON UN SECRETO TUYO, LO PIENSO TODO EL TIEMPO QUE CONMIGO QUIERES VER ELMUNDO ``""")
    mLq4=input("What song is this?")
    while True:
        if mLq4=="PARIS":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... PARIS")
            break
    print()
        #question 5
    print("""Q.5 ``Y SI NO VALE, PUES LE DIGO NO. Y SI SE VA QUE VUELVA A MI MY BOY ``""")
    mLq5=input("What song is this?")
    while True:
        if mLq5=="FORMENTERA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... FORMENTERA")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED MEDIUM: LATIN!!!")

#------------------------------section break------------------------------------------
def medium_hiphop():
    #question 1
    print("""Q.1 ``I NEED A GIRL TO MAKE MY WIFE, I NEED A GIRL WHO'S MINE, ALL MINE ``""")
    mHq1=input("What song is this?")
    while True:
        if mHq1=="I NEED A GIRL":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... I NEED A GIRL")
            break
    print()
        #question 2
    print("""Q.2 ``STANDING ON CORNERS, SERVING ON FATHER'S DAY, THE CLOSEST I HAD TO A DAD ``""")
    mHq2=input("What song is this?")
    while True:
        if mHq2=="BURGLARS AND MURDERERS":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... BURGLARS AND MURDERERS")
            break
    print()
        #question 3
    print("""Q.3 ``I SEEN SHORTY,SHE WAS CHECKIN' UP ON ME ``""")
    mHq3=input("What song is this?")
    while True:
        if mHq3=="YEAH!":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... YEAH!")
            break
    print()
        #question 4
    print("""Q.4 ``YOU KNOW ME WELL FROM NIGHTMARES OF A LONELY CELL ``""")
    mHq4=input("What song is this?")
    while True:
        if mHq4=="HARD KNOCK LIFE":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... HARD KNOCK LIFE")
            break
    print()
        #question 5
    print("""Q.5 ``I HAD TO FIND A PLAY LIKE ANDALE``""")
    mHq5=input("What song is this?")
    while True:
        if mHq5=="ANDALE":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... ANDALE")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED MEDIUM:HIP-HOP!!!")
#---------------------------------section break-----------------------------------------
def medium_popESP():
    #question 1
    print("""Q.1 ``ACORDATE MORALITO DE AQUEL DIA QUE ESTUVISTE EN URUMITA Y NO QUISISTE HACER PARRANDA ``""")
    mPEq1=input("What song is this?")
    while True:
        if mPEq1=="LA GOTA FRIA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... LA GOTA FRIA")
            break
    print()
        #question 2
    print("""Q.2 ``SI LO QUE QUIERES ES BAILAR, SI LO QUE QUIERES ES GOZAR, SI TU QUIERES BAILAR, SOPA DE CARACOL ``""")
    mPEq2=input("What song is this?")
    while True:
        if mPEq2=="SOPA DE CARACOL":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... SOPA DE CARACOL")
            break
    print()
        #question 3
    print("""Q.3 ``VUELA VUELA CON TU IMAGINACION, SI NO PUEDES SER FELIZ ``""")
    mPEq3=input("What song is this?")
    while True:
        if mPEq3=="VUELA VUELA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... VUELA VUELA")
            break
    print()
        #question 4
    print("""Q.4 ``ENTRE ESTAS LAGRIMAS QUE AHORA VAN CAYENDO... NO CABE DUDA, TE ESTOY QUERIENDO COMO NUNCA QUISE ASI ``""")
    mPEq4=input("What song is this?")
    while True:
        if mPEq4=="MIMAYOR NECESIDAD":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... MI MAYOR NECESIDAD")
            break
    print()
        #question 5
    print("""Q.5 ``EN MIS TIEMPOS TODO ERA ELEGANTE, SIN GRENUDOS Y SIN ROCK (HEY PA) ``""")
    mPEq5=input("What song is this?")
    while True:
        if mPEq5=="PACHUCO":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... PACHUCO")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED MEDIUM: POP(ESP)!!!")
#------------------------------------------section break------------------------------------------------
def hard_rock():
    #question 1
    print("""Q.1 ``FEELIN' LIKE A HAND INRUSTED SHAME, SO DOYOU LAUGH OR DOES IT CRY? REPLY ``""")
    hRq1=input("What song is this?")
    while True:
        if hRq1=="INTERSTATE LOVE SONG":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... INTERSTATE LOVE SONG")
            break
    print()
        #question 2
    print("""Q.2 ``AND AT YOUR WORST, YOU'RE STILL THE BEST...BUT AT MY BEST, I AM THE WORST ``""")
    hRq2=input("What song is this?")
    while True:
        if hRq2=="LYDIA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... LYDIA")
            break
    print()
        #question 3
    print("""Q.3 ``WITH ALL THE CHATTER, WHERE'S THE TRUTH ? I FIND IT HARD TO LISTEN``""")
    hRq3=input("What song is this?")
    while True:
        if hRq3=="KID":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... KID")
            break
    print()
        #question 4
    print("""Q.4 ``DO YOU LOVE YOUR NEIGHBOR? IS IT IN YOUR NATURE? DO YOU LOVE A SUNSET? AREN'T YOU FED UP YET? ``""")
    hRq4=input("What song is this?")
    while True:
        if hRq4=="DIRTY":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... DIRTY")
            break
    print()
        #question 5
    print("""Q.5 ``WHAT IF I SAY I'M NOT LIKE THE OTHERS? WHAT IF I SAY I'MNOT JUST ANOTHER ONE OF YOUR PLAYS?``""")
    hRq5=input("What song is this?")
    while True:
        if hRq5=="THE PRETENDER":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... THE PRETENDER")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED HARD: ROCK!!!")
#-------------------------------- section break----------------------------------------
def hard_pop():
    #question 1
    print("""Q.1 ``AND EVERY TIME ITS LIKE A ROCKET THROUGH MY CHEST, THE TV MAKE YOU THINK THE WHOLEWORLD'S ABOUT TO END ``""")
    hPq1=input("What song is this?")
    while True:
        if hPq1=="10:35":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... 10:35")
            break
    print()
        #question 2
    print("""Q.2 ``DARLING, I DON'T UNDERSTAND YOU IF YOU STAY AWAKE AT NIGHT WAITING FOR SOMEBODY RIGHT ``""")
    hPq2=input("What song is this?")
    while True:
        if hPq2=="IF WE EVER BROKE UP":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... IF WE EVER BROKE UP")
            break
    print()
        #question 3
    print("""Q.3 ``OH EVERY DAY,SHE FOUNDA WAY OUT OF THE WINDOW TO SNEAK OUT LATE ``""")
    hPq3=input("What song is this?")
    while True:
        if hPq3=="EASTSIDE":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... EASTSIDE")
            break
    print()
        #question 4
    print("""Q.4 ``OH I'VE BEEN TRIPPIN' ABOUT YOU DAILY, I'VE BEEN OUT OF MY MIND LOOKING ALL KIND OF CRAZY ``""")
    hPq4=input("What song is this?")
    while True:
        if hPq4=="SATURDAY/SUNDAY":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... SATURDAY/SUNDAY")
            break
    print()
        #question 5
    print("""Q.5 ``YOU'RE KINDA CUTE BUT IT'S RAINING HARDER, MY SHOES ARE NOW FULL OF WATER ``""")
    hPq5=input("What song is this?")
    while True:
        if hPq5=="CEILINGS":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... CEILINGS")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED HARD: POP!!!")
#----------------------------------section break-----------------------------------
def hard_Latin():
    #question 1
    print("""Q.1 ``CREES, ME IBA, QUEDAR POR TI LLORANDO? ESA NO SOY YO ``""")
    hLq1=input("What song is this?")
    while True:
        if hLq1=="MARTE":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... MARTE")
            break
    print()
        #question 2
    print("""Q.2 `` MIRA SI LA VIDA FUERA FACIL YO TUVIERA MIL AMORES MAS``""")
    hLq2=input("What song is this?")
    while True:
        if hLq2=="ADIOS":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... ADIOS")
            break
    print()
        #question 3
    print("""Q.3 ``SIGUES CON EL POR EL TIEMPO QUE YA TIENEN PERO SE PUEDE ACABR EN UN SEGUNDO ``""")
    hLq3=input("What song is this?")
    while True:
        if hLq3=="SIGUES CON EL":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... SIGUES CON EL")
            break
    print()
        #question 4
    print("""Q.4 ``SE QUE NUNCA ME VA A LLAMER, MIS MENSAJES LOS VA ABORRAR, ESTOY CANSADO DE LLORAR POR ELLA ``""")
    hLq4=input("What song is this?")
    while True:
        if hLq4=="MENTE":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... ")
            break
    print()
        #question 5
    print("""Q.5 ``DE LA VEZ QUE NOS PERDIMOS EN SEPTIEMBRE QUE FUIMOS A MALGASTAR LA SUERTE ``""")
    hLq5=input("What song is this?")
    while True:
        if hLq5=="MONACO":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... MONACO")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED HARD: LATIN!!!")
#-----------------------------------section break-------------------------------------
def hard_hiphop():
    #question 1
    print("""Q.1 ``NOT BEING ABLE TO GIVE YOU WHAT YOU WANT SINCE I WAS A TODDLER, SHOUT OUT TO MY POPS FOR ALL THE FREE GAME ``""")
    hHq1=input("What song is this?")
    while True:
        if hHq1=="PAINTING PICTURES":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... PAINTING PICTURES")
            break
    print()
        #question 2
    print("""Q.2 ``A OVERNIGHT CELEBRITY, KNOW WHAT I'M SAYING? COME ON ``""")
    hHq2=input("What song is this?")
    while True:
        if hHq2=="OVERNIGHT CELEBRITY":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... OVERNIGHT CELEBRITY")
            break
    print()
        #question 3
    print("""Q.3 ``YOU CAN'T KEEP PATCHINGUP YOUR PAIN TAKING SHOTS AT THE BAR. KNOW EXACTLY HOW YOU FEEL, I KNOW WHAT'S IN YOUR HEART``""")
    hHq3=input("What song is this?")
    while True:
        if hHq3=="FIGHT THE FEELING":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... FIGHT THE FEELING")
            break
    print()
        #question 4
    print("""Q.4 ``IF YOU LIKE TO GET MONEY, WE SIMILAR... ``""")
    hHq4=input("What song is this?")
    while True:
        if hHq4=="SIMILAR":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... SIMILAR")
            break
    print()
        #question 5
    print("""Q.5 ``ALL MY BRAGS TURNTO FACTS, ALL MY HUNDREDS TURN TO RACKS ``""")
    hHq5=input("What song is this?")
    while True:
        if hHq5=="SUVS":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... SUVS")
            break
    print()
    print("CONGRATS! YOU'VE COMPLETED HARD: HIP-HOP!!!")
#-------------------------------Section break-------------------------------------------
def hard_popESP():
    #question 1
    print("""Q.1 ``EL BLANCO MAS PERFECTO DE MI PERDICION, Y COMO UN RAYO TU PIEL CAYO EN MI``""")
    hPEq1=input("What song is this?")
    while True:
        if hPEq1=="EL CENTRO DE MI CORAZON":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... EL CENTRO DE MI CORAZON")
            break
    print()
        #question 2
    print("""Q.2 ``HOY TE VAS PERO SEQUE VOLVERAS PORQUE LO QUE YO TE DI NO LO ENCONTRARAS JAMAS ``""")
    hPEq2=input("What song is this?")
    while True:
        if hPEq2=="LA DOSIS PERFECTA":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... LA DOSIS PERFECTA")
            break
    print()
        #question 3
    print("""Q.3 ``SIETE DE LA MANANA, MI ASIENTO TOCA LA VENTANA. ESTACION CENTRAL, SEGUNDO CARRO ``""")
    hPEq3=input("What song is this?")
    while True:
        if hPEq3=="TREN AL SUR":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... TREN AL SUR")
            break
    print()
        #question 4
    print("""Q.4 ``DEJAME SEGUIR YA NO ME DETENGAS, DEJA ME QUE YA NO TENGO FUERZAS ``""")
    hPEq4=input("What song is this?")
    while True:
        if hPEq4=="ABRAZAME FUERTE":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... ABRAZAME FUERTE")
            break
    print()
        #question 5
    print("""Q.5 ``TENGO UN CORAZON, MUTILADO DE ESPERANZAY DE RAZON``""")
    hPEq5=input("What song is this?")
    while True:
        if hPEq5=="BURBUJAS DE AMOR":
            print("Correct!")
            break
        else:
            print("Sorry! The answer is... BURBUJAS DE AMOR")
            break
    print()
    ("CONGRATS! YOU'VE COMPLETED HARD: POP(ESP)!!!")
#================================================section break to final code=================================================================
gameIntro()
gameRules()
print()
print("Please select a game mode \n \n >>EASY \n >>MEDIUM \n >>HARD")
print()
gameModeselection=input("Mode:")
print()
print("Please select a music genre: \n >>ROCK \n >>POP \n >>LATIN \n >>HIP-HOP \n >>POP(ESP)")
print()
modeGenreselection=input("Genre:")

while True:
    #EASY GAME MODE
    if gameModeselection=="EASY" and modeGenreselection=="ROCK":
        print()
        print("You've selected EASY (ROCK)")
        countdown()
        print()
        easy_rock()
        break
    elif gameModeselection=="EASY" and modeGenreselection=="POP":
        print()
        print("You've selected EASY (POP)")
        countdown()
        print()
        easy_Pop()
        break
    elif gameModeselection=="EASY" and modeGenreselection=="LATIN":
        print()
        print("You've selected EASY (LATIN)")
        countdown()
        print()
        easy_latin()
        break
    elif gameModeselection=="EASY" and modeGenreselection=="HIP-HOP":
        print()
        print("You've selected EASY (HIP-HOP)")
        countdown()
        print()
        easy_hiphop()
        break
    elif gameModeselection=="EASY" and modeGenreselection=="POP(ESP)":
        print()
        print("You've selected EASY (POP(ESP))")
        countdown()
        print()
        easy_popESP()
        break
    #MEDIUM GAME MODE
    elif gameModeselection=="MEDIUM" and modeGenreselection=="ROCK":
        print()
        print("You've selected MEDIUM (ROCK)")
        countdown()
        print()
        medium_rock()
        break
    elif gameModeselection=="MEDIUM" and modeGenreselection=="POP":
        print()
        print("You've selected MEDIUM (POP)")
        countdown()
        print()
        medium_pop()
        break
    elif gameModeselection=="MEDIUM" and modeGenreselection=="LATIN":
        print()
        print("You've selected MEDIUM (LATIN)")
        countdown()
        print()
        medium_Latin()
        break
    elif gameModeselection=="MEDIUM" and modeGenreselection=="HIP-HOP":
        print()
        print("You've selected MEDIUM (HIP-HOP)")
        countdown()
        print()
        medium_hiphop()
        break
    elif gameModeselection=="MEDIUM" and modeGenreselection=="POP(ESP)":
        print()
        print("You've selected MEDIUM (POP(ESP))")
        countdown()
        print()
        medium_popESP()
        break
    #HARD GAME MODE
    elif gameModeselection=="HARD" and modeGenreselection=="ROCK":
        print()
        print("You've selected HARD (ROCK)")
        countdown()
        print()
        hard_rock()
        break
    elif gameModeselection=="HARD" and modeGenreselection=="POP":
        print()
        print("You've selected HARD (POP)")
        countdown()
        print()
        hard_pop()
        break
    elif gameModeselection=="HARD" and modeGenreselection=="LATIN":
        print()
        print("You've selected HARD (LATIN)")
        countdown()
        print()
        hard_Latin()
        break
    elif gameModeselection=="HARD" and modeGenreselection=="HIP-HOP":
        print()
        print("You've selected HARD (HIP-HOP)")
        countdown()
        print()
        hard_hiphop()
        break
    elif gameModeselection=="HARD" and modeGenreselection=="POP(ESP)":
        print()
        print("You've selected HARD (POP(ESP))")
        countdown()
        print()
        hard_popESP()
        break
    else:
        print("Please make sure you've selected one of the listed game modes/genres and typed it correctly. \n Run Program again to play.")
        break