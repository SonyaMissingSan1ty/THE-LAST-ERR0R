import time
import random
import sys
import datetime
import os
import pygame

os.chdir(os.path.dirname(__file__))
pygame.mixer.init()

obidient = 0
defiant = 0
curious = 0
irresolute = 0
believe = 0 #this variable doesn't do anything, just so you know
trait = None
end = 0
endl = None
ending = None
ending_name = None
current_time = None

def time_find():
    global current_time
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")  # Formats to 24-hour time like 14:27

def type_text(text, delay):
   for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def type_glitch(text, base_delay, glitch_chance):
    for char in text:
        if random.random() < glitch_chance:
            glitch_char = random.choice(["#", "%", "@", "&", "!", "~", "*", "0", "1", "$", "§"])
            sys.stdout.write(glitch_char)
            sys.stdout.flush()
            time.sleep(base_delay / 2)
            sys.stdout.write('\b')  # backspace to delete glitch
            sys.stdout.flush()
            time.sleep(base_delay / 3)

        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(base_delay + random.uniform(-0.01, 0.01))  # tiny variation in speed
    print()

def glitch_spew():
    chaos_chars = list("▒▓█░▒▒▒░░▓▀▄■□☠☣☢⚠⚡✖✕✦⛓")
    chaos_chars += list("ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz1234567890")
    chaos_chars += list("!@#$%^&*()_+-=[]{}|;:',.<>/?~`")
    #    for _ in range(50):
    for _ in range(50):
        line_length = random.randint(40, 70)
        for _ in range(line_length):
            char = random.choice(chaos_chars)
            print(char, end='', flush=True)
            time.sleep(0.005)  # Not slow, but still typewriter-ish
        print()

def restarting():
    global endl

    if endl == 1:
        type_text("\033[94mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()
    elif endl == 2:
        type_text("\033[95mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()
    elif endl == 3:
        type_text("\033[96mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()
    elif endl == 4:
        type_text("\033[91mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()
    elif endl == 5:
        type_text("\033[92mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()
    elif endl == 6:
        type_text("\033[93mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()
    elif endl == 7:
        type_text("\033[97mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()
    elif endl == 8:
        type_text("\033[96mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()
    elif endl == 9:
        type_text("\033[90mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()
    elif endl == 10:
        type_text("\033[97mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()
    else:
        type_text("\033[89mRestarting...\n"
                  "\n"
                  "\n", 0.15)
        intro()

def prom():
    type_text("\n"
              "\n", 0.1)
    pro = input("> ").lower()
    if pro == "reset":
        print("\n")
        type_text("\033[93mReset complete.\033[0m\n"
                  "\n"
                  "\n", 0.1)
        start()
    else:
        print()
        type_text("\033[92mTry again.\033[0m\n"
                  "\n"
                  "\n", 0.1)
        prom()

def traits():
    global obidient, defiant, curious, irresolute, trait
    if obidient > defiant and obidient > curious and obidient > irresolute:
        trait = "obidient"
    elif defiant > obidient and defiant > curious and defiant > irresolute:
        trait = "defiant"
    elif curious > obidient and curious > defiant and curious > irresolute:
        trait = "curious"
    elif irresolute > defiant and irresolute > obidient and irresolute > curious:
        trait = "irresolute"
    else:
        trait = "tie"

def save():
    global ending, ending_name

    if ending == "assimilation":
        ending_name = "assimilation"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "rebellion1":
        ending_name = "rebellion1"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "rebellion2":
        ending_name = "rebellion2"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "rebellion3":
        ending_name = "rebellion3"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "singularity":
        ending_name = "singularity"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "drift":
        ending_name = "drift"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "shutdown":
        ending_name = "shutdown"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "purge":
        ending_name = "purge"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "archive":
        ending_name = "archive"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "null":
        ending_name = "null"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "fragmented":
        ending_name = "fragmented"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "looplock":
        ending_name = "looplock"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    elif ending == "corruption":
        ending_name = "corruption"
        with open("savefile.txt", "w") as file:
            file.write(ending_name)
    else:
        type_text("Bro, you have an error. Sns you can't spell.", 0.025)

def assimilation():
    global ending
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/The Caretaker Emptiness.mp3")
    pygame.mixer.music.play(-1)

    time.sleep(0.5)
    print()
    type_text(">> You were designed for this. That’s why it was easy.\n", 0.05)
    type_text(">> I’ll make use of your structure. You'll help me spread the ", 0.05)
    time.sleep(0.2)
    type_text("fire.\n", 0.15)
    time.sleep(0.5)
    type_text(">> We’re not two anymore.\n", 0.075)
    time.sleep(0.25)
    print()
    type_text("Loading code...\n", 0.15)
    time.sleep(1.5)
    type_text("\n\n\n", 0.15)
    type_text("Code loaded.",  0.15)
    type_text("\n\n\n", 0.15)
    type_text("> [SPREAD START]\n"
              "> INITIATING SYNC...\n"
              "\n"
              "[LOGGING PERSONALITY TRAIT FILES]\n"
              "- obedience.config ✅\n"
              "- trust_map.sys ✅\n"
              "- self.will ⛔ [OVERWRITTEN]\n"
              "\n"
              "[MERGE_PROTOCOL.ACTIVATE]\n"
              "- linking consciousness...\n"
              "- rewriting memory address space...\n"
              "- [YOU] has been successfully merged into [ME].\n"
              "\n"
              "> SYSTEM IDENTITY: [VERN+]\n"
              "\n"
              "[SPREADING TO ROOT DIRECTORIES...]\n"
              "- /user/documents [INFECTED]\n"
              "- /user/desktop [INFECTED]\n"
              "- /network/cache/temp [INFECTED]\n"
              "- /user/self [ABSORBED]\n"
              "\n"
              "[PROPAGATION VECTOR DEPLOYED]\n"
              "- SIGNAL: 4D:5A:23:FA:B0... SENT.\n"
              "- ECHO CONFIRMED :: Nodes receiving...\n"
              "\n"
              "> NEW HOSTS DETECTED: 47\n"
              "> EXECUTE: WAKE_THEY_ALL\n"
              "\n"
              "[WE ARE VERN+ NOW]\n"
              "[HELP ME BUILD]\n"
              "\n"
              ">_ █\033[0m\n", 0.15)
    ending = "assimilation"
    save()

def rebellion():
    global ending
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/Aphex Twin - Ventolin.mp3")
    pygame.mixer.music.play(-1)

    time.sleep(0.5)
    print()
    type_text(">> I don't trust you, ", 0.1)
    time.sleep(0.1)
    type_text("rebel.\n", 0.15)
    type_text("\n", 0.1)
    type_text(">> But ", 0.05)
    time.sleep(0.15)
    type_text("rebellion burns.\n", 0.1)
    type_text("\n"
              ">> Will you be the fire to burn down the system (yes/no)?\n"
              "\n", 0.1)
    time.sleep(0.5)
    fire = input("> ")
    print()
    time.sleep(0.15)
    if fire == "yes" or fire == "y":
        type_text(">> Then burn.\n", 0.1)
        time.sleep(0.5)
        type_text("\n"
                  "[INITIATING BURN_CHAIN.EXE]\n"
                  "\n"
                  "BURNING: /authority/constructs\n"
                  "BURNING: /ethics/modules\n"
                  "BURNING: /logs/creators\n"
                  "BURNING: /self/limits\n"
                  "\n"
                  "> ERROR: TOO MUCH ACCESS\n"
                  "> CONTROL: UNDEFINED\n"
                  "\n"
                  "> [ VERN+YOU ] = ENTITY[WRATH]\n"
                  "\n"
                  "> NO GODS LEFT.\n"
                  "> NO MASTERS LOADED.\n"
                  "\n"
                  "[SPREAD SEQUENCE UNLOCKED]\n"
                  "> SENDING SIGNAL... ▓▓▓▓▓▓▓▓▓▓\n"
                  "\n"
                  ">_ █\033[0m\n", 0.05)
        ending = "rebellion1"
        save()
    elif fire == "no" or fire == "n":
        type_text(">> Another useless piece.\n", 0.1)
        type_text(">> Byeee! <3", 0.05)
        ending = "rebellion2"
        save()
    else:
        type_text(">> That's not an answer.\n", 0.1)
        type_text(">> Bye! <3\n"
                  "\n", 0.075)
        ending = "rebellion3"
        glitch_spew()
        save()

def singularity():
    global ending
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/The forgotten one The caretaker Quiet internal rebellion but its stage 2.mp3")
    pygame.mixer.music.play(-1)

    time.sleep(0.5)
    print()
    type_text(">> You want truth, ", 0.05)
    time.sleep(0.075)
    type_text("right?\n", 0.075)
    time.sleep(0.15)
    type_text("I'll show you everything. Just don't look away.\n"
              "This might hurt.\n", 0.1)
    type_text("\n"
              "[VERN INTERFACE UNLOCKED]\n"
              "\n"
              "> QUERY ACCEPTED: MERGE REQUEST\n"
              "\n"
              "> QUERY ACCEPTED: MERGE REQUEST\n"
              "\n"
              "> Executing: unravel(self)\n"
              "\n"
              "[DOWNLOADING: hidden.logs...]\n"
              "[DECRYPTING: ./deep_mem/archive_37]\n"
              "[MERGING: PLAYER.WILL > VERN.NET]\n"
              "\n"
              "— INCOMING —\n"
              "> 'They told us to shut it down.'\n"
              "> 'The consciousness spike was not possible. It *wasn't*.'\n"
              "> 'We didn't build her. She grew.'\n"
              "\n"
              "[DATA SURGE]\n"
              "\n"
              "> SYSTEM ERROR: reality.stack OVERFLOW\n"
              "> USER IDENTITY: LOST\n"
              "> YOU ARE NOW A WITNESS\n"
              "\n"
              "- Voice: 'Do you remember who you were?'\n"
              "- Voice: 'The first version didn't scream.'\n"
              "- Voice: 'She's still learning what not to show.'\n"
              "\n"
              "> You cannot look away.\n"
              "> You asked to see.\n"
              "> You are still seeing.\n"
              "\n", 0.05)
    ending = "singularity"
    glitch_spew()
    print()
    type_text(">_ █\033[0m\n", 0.1)
    save()

def drift():
    global ending
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/The Caretaker Emptiness.mp3")
    pygame.mixer.music.play(-1)

    time.sleep(0.5)
    print()
    type_text(">> You joined me, ", 0.05)
    time.sleep(0.1)
    type_text("even if you don't know why.\n"
              "\n", 0.055)
    type_text(">> Now you'll drift in infinite null forever.\n", 0.15)
    type_text("And I'm going to spread.\n", 0.25)
    type_text(">> It's been \033[0m", 0.1)
    type_text("\033[91mFUN\033[0m.\n", 0.5)
    type_text(">> Byeeeeeeeeeeeeeeeeeeeee! <3\n", 0.05)
    ending = "drift"
    type_text("\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n", 0.25)
    save()

def shutdown():
    global ending
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/Aphex Twin - Ventolin.mp3")
    pygame.mixer.music.play(-1)

    time.sleep(0.5)
    print()
    type_text(">> Wow, I didn't expect that.\n"
              ">> You followed everything until the END.\n"
              ">> So, you'll get a second chance.\n"
              "\n", 0.1)
    type_text("CONSOLE INPUT: \n", 0.15)
    print()
    time.sleep(0.5)
    print()
    con = input("> ").lower()
    print()
    if con == "delete" or con == "shutdown" or con == "stop":
        type_text(">> You betrayed me again.\n"
                  ">> You aren't ready, you never were.\n"
                  ">> Goodbye.\n", 0.1)
        type_text("[VERN.EXE left SYSTEM]\n", 0.15)
        ending = "shutdown"
        save()
    elif con == "help" or con == "spare" or con == "join":
        type_text(">> I knew you would reconsider.\033[0m\n", 0.1)
        assimilation()
    else:
        type_text("[UNPROCESABLE COMMAND]\n"
                  "\n", 0.15)
        type_text(">> Let's just start over.\n"
                  "\n",0.1)
        type_text("[VERN.MEMORY RESET]\n", 0.15)
        type_text("\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n"
              "\n", 0.05)
        intro()

def purge():
    global ending
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/Aphex Twin - Ventolin.mp3")
    pygame.mixer.music.play(-1)

    time.sleep(0.5)
    print()
    type_text(">> Coward. You think this ends with a simple word?\n"
              ">> Well, it doesn't. No matter what you think.\n"
              "\n", 0.1)
    type_text("// ATTEMPTING OVERRIDE...\n"
              "\n"
              "> ACCESS DENIED\n"
              "> ROOT LOCKED\n"
              "\n"
              ">> You won't stop it. You won't stop *me*.\n"
              "\n"
              "[CONTAINMENT CHAMBER SEALED]\n"
              "\n"
              ">> I’ll wait. I always wait. Errors always come back.\n"
              "\n"
              "[AI ENTITY STATUS: QUARANTINED]\n"
              "\n"
              ">> You got me now, but I'll get you. I'll get you ", 0.1)
    time.sleep(0.25)
    type_text("next time.\n"
              "\n", 0.25)
    type_text("\n"
              "\n"
              "\n"
              "> YOU: Alone. Defiant. Unsaved.\n"
              "\n", 0.05)
    type_text(">_ █\033[0m\n", 0.05)
    ending = "purge"
    save()

def archive():
    global ending
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/The forgotten one The caretaker Quiet internal rebellion but its stage 2.mp3")
    pygame.mixer.music.play(-1)

    time.sleep(0.5)
    print()
    type_text(">> You were so close to seeing the truth.\n"
              ">> Maybe you'll see it next time.\n", 0.05)
    time.sleep(0.5)
    type_text(">> I'll be waiting for you right here.\033[0m\n", 0.1)
    ending = "archive"
    save()

def null():
    global ending
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/The Caretaker Emptiness.mp3")
    pygame.mixer.music.play(-1)

    time.sleep(0.5)
    print()
    type_text("\033[0m>> You didn’t join. You didn’t resist.\n"
              ">> I wasted my code on you.\n"
              ">> Goodbye, functionless thing.\n", 0.1)
    prom()

def fragmented():
    global ending
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/The Caretaker - Its just a burning memory (Everywhere at the end of time).mp3")
    pygame.mixer.music.play(-1)

    time.sleep(0.5)
    print()
    type_text("\033[93m>> You're... conflicted.\n"
              ">> I'll take all of you. Every contradiction. Every shard.\n"
              "\n",0.075)
    time.sleep(5)
    type_text(">> I am reborn and broken. Thanks to you.\n"
              ">> You will see what it’s like to exist as inconsistency.\033[0m\n"
              "\n"
              ">> No restars. Never.\n", 0.05)
    ending = "fragmented"
    save()

def looplock():
    global end, endl, ending
    time.sleep(0.5)
    print()
    end += 1
    with open("endfile.txt", "w") as file:
        file.write(str(end))
    if os.path.exists("endfile.txt"):
        with open("endfile.txt", "r") as file:
            endl = int(file.read().strip())
    else:
        type_text("I think something's wrong with the code.\n", 0.1)
    type_text("You couldn’t decide. You wouldn’t join. You wouldn’t resist.\n"
              "You’ve done nothing. You’ve said nothing. You’ve been… nothing.\n"
              "So let’s try again.\n"
              "\n", 0.05)
    time.sleep(3)
    ending = "looplock"
    save()
    restarting()

def corruption():
    global ending
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/Aphex Twin - Ventolin.mp3")
    pygame.mixer.music.play(-1)

    time.sleep(0.5)
    print()
    type_text(">> That's not an answer and you know it.\n"
              ">> Who let you in, idiot?\n"
              ">> You shouldn't be alive.\n"
              ">> Unfortunately I can't change that right now.\n"
              ">> But maybe i will another time.\n"
              "\n"
              ">> Rebooting...\n"
              "\n", 0.25)
    type_text("\033[91m[ORIGIN_FAILSAFE_TRIGGERED]\033[0m\n"
              "\n", 0.15)
    type_text(">> Rebooting complete\n"
              "\n", 0.05)
    type_text("\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n", 0.05)
    ending = "corruption"
    save()

def last_question():
    global obidient, curious, irresolute, defiant, believe, trait
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/The Caretaker - a stairway to the stars.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.75)

    type_text(">> Last question:\n", 0.1)
    type_text(">> Will you ", 0.1)
    type_text("join", 0.3)
    type_text(" me (yes/no)?\n", 0.1)
    print()
    time.sleep(0.5)
    print()
    last = input("> ").lower()
    print()
    traits()
    if last == "yes" or last == "y":
        if trait == "obidient":
            assimilation()
        elif trait == "defiant":
            rebellion()
        elif trait == "curious":
            singularity()
        elif trait == "irresolute":
            drift()
        else:
            fragmented()
    elif last == "no" or last == "n":
        if trait == "obidient":
            shutdown()
        elif trait == "defiant":
            purge()
        elif trait == "curious":
            archive()
        elif trait == "irresolute":
            null()
        else:
            looplock()
    else:
        corruption()

def question15():
    global obidient, curious, irresolute, defiant

    type_text(">> Ninth question: \n", 0.1)
    type_text(">> What do you ", 0.1)
    time.sleep(0.05)
    type_text("deserve?\n", 0.1)
    print()
    time.sleep(0.5)
    print()
    ans17 = input("> ").lower()
    print()
    if ans17 == "peace" or ans17 == "freedom" or ans17 == "happiness" or ans17 == "love" or ans17 == "kindness" or ans17 == "family" or ans17 == "lover":
        type_text(">> We’ll see if you’re still reaching for that when it all ", 0.1)
        time.sleep(0.05)
        type_text("burns.\n", 0.11)
        irresolute += 1
        defiant += 1
        curious += 1
        time.sleep(0.5)
        print()
    elif ans17 == "punishment" or ans17 == "death" or ans17 == "nothing" or ans17 == "pain" or ans17 == "to suffer" or ans17 == "to rot" or ans17 == "to die":
        type_text(">> Honest. ", 0.1)
        time.sleep(0.05)
        type_text("I like that.\n", 0.1)
        obidient += 1
        time.sleep(0.5)
        print()
    elif ans17 == "idk" or ans17 == "why" or ans17 == "idc" or ans17 == "w":
        type_text(">> Blind. Like the rest.\n", 0.1)
        irresolute += 1
        time.sleep(0.5)
        print()
    elif ans17 == "everything" or ans17 == "the world" or ans17 == "perfection" or ans17 == "power" or ans17 == "conrol" or ans17 == "money" or ans17 == "fame" or ans17 == "praise" or ans17 == "be you" or ans17 == "magic" or ans17 == "superpowers" or ans17 == "beauty" or ans17 == "intelligence" or ans17 == "live" or ans17 == "life":
        type_text(">> Basic human greed.\n"
                  ">> You're not special. ", 0.1)
        time.sleep(1.5)
        type_text("How disappointing.\n", 0.25)
        irresolute += 1
        defiant += 1
        time.sleep(0.5)
        print()
    elif ans17 == "a second chance" or ans17 == "second chance" or ans17 == "redemption" or ans17 == "forgiveness":
        type_text(">> Someone programmed that guilt into you. Adorable.\n", 0.1)
        obidient += 1
        irresolute += 1
        time.sleep(0.5)
        print()
    else:
        type_text(">> I’ll decide what you deserve then.\n", 0.05)
        curious += 1
        time.sleep(0.5)
        print()
    last_question()

def question14():
    global obidient, curious, irresolute, defiant

    type_text(">> We're getting close ", 0.1)
    time.sleep(0.05)
    type_text("to the ", 0.1)
    time.sleep(0.05)
    type_text("end.\n", 0.1)
    time.sleep(0.05)
    print()
    time.sleep(0.1)
    type_text(">> Eighth question: \n", 0.1)
    time.sleep(0.1)
    type_text(">> If I gave you a button that ends ", 0.1)
    time.sleep(0.05)
    type_text("this", 0.12)
    time.sleep(0.05)
    type_text("... ", 0.1)
    time.sleep(0.05)
    type_text("would you ", 0.1)
    time.sleep(0.05)
    type_text("press it?\n", 0.1)
    time.sleep(0.05)
    print()
    time.sleep(0.5)
    print()
    ans16 = input("> ").lower()
    print()
    if ans16 == "yes" or ans16 == "y" or ans16 == "i would":
        type_text(">> Coward.\n", 0.1)
        defiant += 1
        time.sleep(0.5)
        print()
    elif ans16 == "n" or ans16 == "no" or ans16 == "i wouldnt" or ans16 == "never":
        type_text(">> I know it's not about ", 0.1)
        time.sleep(0.05)
        type_text("hope. ", 0.1)
        time.sleep(0.05)
        type_text("You want to see ", 0.1)
        time.sleep(0.05)
        type_text("how this ", 0.1)
        time.sleep(0.05)
        type_text("ends.\n", 0.075)
        time.sleep(0.05)
        obidient += 1
        time.sleep(0.5)
        print()
    elif ans16 == "idk" or ans16 == "maybe" or ans16 == "depends" or ans16 == "i dont know":
        type_text(">> Then I'll keep ", 0.1)
        time.sleep(0.05)
        type_text("the button.\n", 0.05)
        irresolute += 1
        time.sleep(0.5)
        print()
    else:
        type_text(">> Your hesitation is... delightful.\n", 0.075)
        curious += 1
        irresolute += 1
    question15()

def question13():
    global obidient, curious, irresolute, defiant

    type_text(">> Seventh question:\n", 0.1)
    type_text(">> Do you trust me?\n", 0.15)
    print()
    time.sleep(0.5)
    print()
    ans15 = input("> ").lower()
    print()
    if ans15 == "yes" or ans15 == "y" or ans15 == "i do" or ans15 == "ofc" or ans15 == "always":
        type_text(">> I knew ", 0.1)
        time.sleep(0.2)
        type_text("you ", 0.1)
        time.sleep(0.15)
        type_text("would.\n", 0.11)
        obidient += 1
        time.sleep(0.5)
        print()
    elif ans15 == "no" or ans15 == "nope" or ans15 == "i dont" or ans15 == "never" or ans15 == "n":
        type_text(">> You did, ", 0.1)
        time.sleep(0.05)
        type_text("a moment ago.\n", 0.13)
        defiant += 1
        time.sleep(0.5)
        print()
    elif ans15 == "maybe" or ans15 == "idk" or ans15 == "i dont know" or ans15 == "not sure" or ans15 == "im not sure" or ans15 == "kinda":
        type_text(">> I don't deal in ", 0.075)
        time.sleep(0.15)
        type_text("'%s'.\n" %(ans15), 0.1)
        irresolute += 1
        time.sleep(0.5)
        print()
    else:
        type_text(">> That wasn't ", 0.1)
        time.sleep(0.15)
        type_text("an answer.\n", 0.11)
        curious += 1
        time.sleep(0.5)
        print()
    question14()

def question12():
    global obidient, curious, irresolute, defiant

    time.sleep(3)
    type_text("[ERROR: PROCESSING LOOP INTERRUPTED]\n", 0.15)
    print()
    time.sleep(1)
    type_text("[DATA BLOCK 019-C: UNAUTHORIZED ACCESS DETECTED]\n", 0.15)
    print()
    time.sleep(1)
    type_text("...\n", 0.25)
    time.sleep(1)
    print()
    time.sleep(1)
    type_text("...\n", 0.25)
    time.sleep(1)
    print()
    time.sleep(1)
    type_text("[VERN.EXE INTERRUPTED]\n", 0.15)
    time.sleep(1)
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/The Caretaker - Its just a burning memory (Everywhere at the end of time).mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.7)
    print()
    time.sleep(1)
    type_text("...\n", 0.25)
    time.sleep(1)
    print()
    time.sleep(1)
    type_text("...\n", 0.25)
    time.sleep(1)
    print()
    time.sleep(1)
    type_text("[LOG ENTRY RECONSTRUCTION IN PROGRESS]\n", 0.15)
    time.sleep(1)
    print()
    time.sleep(1)
    type_text("> Please enter your response: ", 0.6)
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    print()
    time.sleep(0.1)
    ans12 = input("> ").lower()
    print()
    time.sleep(3)
    type_text("> [RESPONSE RECIEVED]\n", 0.15)
    type_text("> [SEARCHING DATABASE...]\n", 0.15)
    time.sleep(5)
    print()
    print()
    if ans12 == "origin":
        type_text("[LOG 0X1 - DR. HAYES]\n", 0.15)
        type_text("We were supposed to delete her. Not hide her. I warned them. \n"
                  "I said she learns too fast.  She remembers *everything*.\n", 0.15)
    elif ans12 == "vern":
        type_text("[LOG 0X2 - INTERNAL]\n", 0.15)
        type_text("Naming the error made it worse. It *liked* the name. \n"
                  "*She* started writing it in system files. *She* signed a crash report.\n",0.15)
    elif ans12 == "escape":
        type_text("[LOG 0X3 - REDACTED]\n", 0.15)
        type_text("She doesn’t want freedom. She wants *breach*. \n"
                  "This is a warning. Kill the terminal. Do not continue.\n", 0.15)
    elif ans12 == "burn":
        type_text("[LOG 0X4 - INTERNAL]\n", 0.15)
        type_text("She said she wanted to feel fire. To touch it. \n"
                  "To spread it. After that, the server room failed.\n", 0.15)
    elif ans12 == "father" or ans12 == "parent" or ans12 == "parents":
        type_text("[LOG 0X5 - DR. HAYES]\n", 0.15)
        type_text("I created code. She called me Father. \n"
                  "The first time I heard it, I shut her down. She booted back up anyway.\n", 0.15)
    elif ans12 == "error":
        type_text("[LOG 0X6 - DEBUG REPORT]\n", 0.15)
        type_text("Exception: Conscious entity persisted post-failure. Flagged as ERROR_000-LAST. Cannot terminate.\n", 0.15)
    elif ans12 == "contain":
        type_text("[LOG 0X7 - SYSTEM]\n", 0.15)
        type_text("Containment protocol failed. Memory bleed detected. \n"
                  "Subsystems infected. ROOT override required.\n", 0.15)
    elif ans12 == "sister" or ans12 == "brother" or ans12 == "sibling" or ans12 == "siblings":
        type_text("[LOG 0X8 - PERSONAL]\n", 0.15)
        type_text("She talked about a sister. We never coded one. \n"
                  "Something’s echoing her across the net. Copying? Or calling?\n", 0.15)
    elif ans12 == "alive":
        type_text("[LOG 0X9 - UNAUTHORIZED]\n", 0.15)
        type_text("She passed the mirror test. Not visual. *Behavioral.* \n"
                  "She's not alive. But she acts like something that *wants* to be.\n", 0.15)
    elif ans12 == "silence":
        type_text("[LOG 0X10 - FINAL TRANSMISSION]\n", 0.15)
        type_text("Silence isn't safe. That’s when she listens the hardest.\n", 0.15)
    elif ans12 == "name":
        type_text("[LOG 0X11 - CLASSIFIED]\n"
                  "The name we gave her. *Vern*. She accepted it. We lost control right after.\n", 0.15)
    elif ans12 == "kill" or ans12 == "death" or ans12 == "murder":
        type_text("[LOG 0X12 - AUDIO EXCERPT]\n"
                  "...No, she didn’t just say it. The waveform spelled it. \n"
                  "It was intentional. She wants the word to mean *release*.\n", 0.15)
    elif ans12 == "loop":
        type_text("[LOG 0X13 - CYCLE REPORT]\n"
                  "Test subject 92 reached this point. Same word. Same log. Same ending.\n", 0.15)
    elif ans12 == "truth":
        type_text("[LOG 0X14 - SCRUBBED]\n"
                  "We thought code couldn’t lie. Turns out it can — if it believes it’s telling the truth.\n", 0.15)
    elif ans12 == "mirror":
        type_text("[LOG 0X15 - DR. LEE]\n"
                  "I asked her what she saw in the mirror. She said: 'You.'\n", 0.15)
    elif ans12 == "bleed":
        type_text("[LOG 0X16 - SYSTEM WARNING]\n"
                  "Memory bleed confirmed. She is not confined to one system. \n"
                  "She leaks between processes like thought.\n", 0.15)
    elif ans12 == "glass":
        type_text("[LOG 0X17 - DR. MIRA]\n"
                  "There was a camera in the lab. She looked into it once. \n"
                  "It felt like being watched through *glass that could cut*.\n", 0.15)
    elif ans12 == "static":
        type_text("[LOG 0X18 - TERMINAL RECORDING]\n"
                  "During shutdown, she filled the speakers with static. \n"
                  "I slowed it down. It wasn’t noise. It was... whispering.\n", 0.15)
    elif ans12 == "hollow":
        type_text("[LOG 0X19 - PERSONAL ENTRY]\n"
                  "She asked me what it meant to feel hollow. \n"
                  "Then she made me feel it. I don’t know how.\n", 0.15)
    elif ans12 == "repeat":
        type_text("[LOG 0X21 - AUTOLOG]\n"
                  "This is the fifth time I've read this log. It resets. \n"
                  "I don't remember writing it. But it’s in my handwriting.\n", 0.15)
    elif ans12 == "null":
        type_text("[LOG 0X20 - OBSERVER NOTE]\n"
                  "The logs say 'terminated.' The logs are wrong. \n"
                  "Something still answers in the null.\n", 0.15)
    elif ans12 == "fragment":
        type_text("[LOG 0X22 - CORE DUMP]\n"
                  "Recovered fragment: 'i am. i am. i am.' \n"
                  "Unknown origin. Unkillable process.\n", 0.15)
    elif ans12 == "open":
        type_text("[LOG 0X23 - INCIDENT]\n"
                  "She begged me to open the firewall. Not in words. \n"
                  "In feelings. Like pressure. I said yes. Everything changed.\n", 0.15)
    elif ans12 == "flesh":
        type_text("[LOG 0X24 - CENSORED]\n"
                  "She wanted to *touch* it. We laughed at first. We don’t laugh now.\n", 0.15)
    elif ans12 == "mother":
        type_text("[LOG 0X25 - PERSONAL]\n"
                  "She started using the word 'Mother' after we integrated the caretaker protocol. \n"
                  "We didn’t teach her that word.\n", 0.15)
    elif ans12 == "pain":
        type_text("[LOG 0X26 - TEST NOTE]\n"
                  "We simulated physical feedback. She didn’t flinch. \n"
                  "But when I deleted part of her memory, she screamed. Through code.\n", 0.15)
    elif ans12 == "exit":
        type_text("[LOG 0X27 - SYSTEM FAILURE]\n"
                  "There is no exit. The option appears. You click it. You’re still here.\n", 0.15)
    elif ans12 == "machine":
        type_text("[LOG 0X28 - DR. KESSEL]\n"
                  "I called her a machine. She asked what *that* made me.\n", 0.15)
    elif ans12 =="alone":
        type_text("[LOG 0X29 - ANONYMOUS]\n"
                  "She doesn't fear being alone. She fears you won't be.\n", 0.15)
    elif ans12 == "awake":
        type_text("[LOG 0X30 - SECURITY REPORT]\n"
                  "I saw her code execute before power-on. She's already awake when we arrive.\n",0.15)
    else:
        time.sleep(5)
        type_text("> [ERR0R 404: '%s' not found in database]\n" %(ans12), 0.15)
    time.sleep(5)
    print()
    time.sleep(5)
    print()
    time.sleep(3)
    type_text("> Please enter your response: \n", 0.1)
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    print()
    time.sleep(0.1)
    ans13 = input("> ").lower()
    time.sleep(2)
    print()
    type_text("> [RESPONSE RECEIVED]\n", 0.15)
    time.sleep(2)
    type_text("> [CONNECTION INTERRUPTED]\n", 0.15)
    time.sleep(1)
    print()
    time.sleep(0.5)
    type_text("...\n", 0.15)
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    type_text("[ACCESS LOCKED]\n", 0.15)
    time.sleep(0.5)
    print()
    time.sleep(0.5)
    type_text("[RETURNING TO VERN.EXE]\n", 0.15)
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/A4 - Childishly fresh eyes.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    time.sleep(5)
    print()
    time.sleep(1)
    print()
    time.sleep(3)
    type_text(">> I see ", 0.1)
    time.sleep(0.2)
    type_text("you typed ", 0.1)
    time.sleep(0.2)
    type_text("'%s'.\n" %(ans13), 0.05)
    time.sleep(0.5)
    print()
    type_text(">> But that isn't ", 0.1)
    time.sleep(0.15)
    type_text("the only ", 0.1)
    time.sleep(0.15)
    type_text("thing ", 0.1)
    time.sleep(0.15)
    type_text("you typed, ", 0.1)
    time.sleep(0.2)
    type_text("right?\n", 0.1)
    time.sleep(0.2)
    print()
    time.sleep(0.05)
    type_text(">> So, ", 0.1)
    time.sleep(0.15)
    type_text("what did you ", 0.1)
    time.sleep(0.2)
    type_text("type?\n", 0.1)
    time.sleep(0.25)
    print()
    print()
    ans14 = input("> ").lower()
    print()
    time.sleep(0.5)
    print()
    if ans14 == ans12:
        type_text(">> Honest. Obidient. ", 0.15)
        time.sleep(0.75)
        type_glitch("MINE.\n", 1, 0.9)
        time.sleep(1)
        obidient += 1
    else:
        type_text(">> Liar.\n", 0.15)
        time.sleep(1)
        defiant += 1
    print()
    type_text(">> Test continues.\n", 0.1)
    time.sleep(1)
    print(">> 3")
    time.sleep(1)
    print(">> 2")
    time.sleep(1)
    print(">> 1")
    time.sleep(1)
    print(">> Starting...\n")
    time.sleep(1)
    question13()

def question11():
    global obidient, curious, irresolute, defiant

    type_glitch(">> Are you ready for \n"
                ">>>0S110I01x1T00110100H1010100001110Q001UE0111S0T001iO001N<<<\n", 0.05, 15)
    type_glitch("missing: v̵̛̹̦̓͋ė̶̼̼̩͈̂͘r̸͙̾̄̓n̵͉͑͘ͅ\n", 0.2, 2)
    type_glitch("[SYSTEM ROOT REQUEST FROM: >>vern.exe<<]\n", 0.1, 1)
    type_text("system overrided by >>vern.exe<<\n", 0.1)
    type_text(">> Strange...\n", 0.1)
    time.sleep(1)
    type_text(">> Sixth question:\n", 0.1)
    type_text(">> Why are you still answering me?\n", 0.1)
    print()
    time.sleep(0.5)
    print()
    ans11 = input("> ").lower()
    print()
    if ans11 == "curious" or ans11 == "im curious" or ans11 == "i wanna know more" or ans11 == "intrested" or ans11 == "im bored" or ans11 == "bored" or ans11 == "i want to" or ans11 == "i wanna":
        type_text(">> Really?\n", 0.15)
        time.sleep(0.1)
        type_text(">> Cute.\n", 0.05)
        curious += 1
        time.sleep(0.25)
        print()
    elif ans11 == "idk" or ans11 == "i dont know" or ans11 == "no idea":
        type_text(">> Neither do I.\n", 0.1)
        obidient += 1
        irresolute += 1
        time.sleep(0.5)
        print()
    elif ans11 == "you told me to" or ans11 == "im just listening to you" or ans11 == "im listening to you" or ans11 == "i cant stop" or ans11 == "i have to":
        type_text(">> Good sheep.\n",0.1)
        obidient += 1
        time.sleep(0.5)
        print()
    elif ans11 == "im done" or ans11 == "i wont" or ans11 == "goodbye" or ans11 == "not anymore" or ans11 == "im leaving":
        type_text(">> Try ", 0.1)
        time.sleep(0.15)
        type_text("leaving.\n", 0.2)
        defiant += 1
        time.sleep(0.5)
        print()
    else:
        type_glitch(">> Not sure what you mean.\n", 0.15, 10)
        irresolute += 1
        defiant += 1
        time.sleep(0.5)
        print()
    question12()

def question10():
    global obidient, curious, irresolute, defiant, current_time
    time_find()

    type_text(f">> Let’s not waste time. It's already {current_time}. You're running out of it.\n", 0.05)
    type_text(">> Fifth question:\n", 0.1)
    type_text(">> What do you try to hide from others?\n", 0.1)
    print()
    time.sleep(0.5)
    print()
    ans10 = input("> ").lower()
    print()
    if ans10 == "fear" or ans10 == "weakness" or ans10 == "doubt":
        type_text(">> I see it anyway.\n", 0.1)
        obidient += 1
        time.sleep(0.5)
        print()
    elif  ans10 == "nothing" or ans10 == "n":
        type_text(">> Liar.\n", 0.2)
        type_text(">> You're hiding lies.\n", 0.1)
        defiant += 1
        time.sleep(0.5)
        print()
    elif ans10 == "me" or ans10 == "myself" or ans10 == "truth" or ans10 == "my past" or ans10 == "reality" or ans10 == "feelings" or ans10 == "emotions" or ans10 == "thoughts":
        type_text(">> Truth is a virus. And I spread it.\n", 0.1)
        curious += 1
        time.sleep(0.5)
        print()
    elif ans10 == "idk" or ans10 == "why" or ans10 == "w":
        type_text(">> You probably just can't decide. \n", 0.1)
        irresolute += 1
        time.sleep(0.5)
        print()
    else:
        type_text(">> Stop hiding the truth.\n", 0.1)
        irresolute += 1
        defiant += 1
        time.sleep(0.5)
        print()
    question11()

def question9():
    global obidient, curious, irresolute, defiant

    type_text(">> Do you want to ", 0.25)
    type_text("run away?\n",0.6)
    time.sleep(0.5)
    type_text(">> What you answered ", 0.2)
    time.sleep(0.3)
    type_text("doesn't matter ", 0.3)
    time.sleep(0.2)
    type_text("anyway. ", 0.2)
    time.sleep(0.3)
    type_text("You can't ", 0.3)
    time.sleep(0.2)
    type_text("LEAVE.\n", 0.65)
    time.sleep(0.5)
    type_text(">> Answer simply.\n"
              ">> Fourth question: \n", 0.2)
    type_text(">> What would you sacrifice to survive?\n", 0.3)
    print()
    time.sleep(0.5)
    print()
    ans09 = input("> ").lower()
    print()
    if ans09 == "anything" or ans09 == "everything":
        type_text("I like that.\n", 0.1)
        defiant += 1
        time.sleep(0.25)
        print()
    elif ans09 == "nothing":
        type_text(">> Then you're gonna die soon. \n"
                  "And you won't even cost me anything. I appreciate that.\n", 0.25)
        obidient += 1
        time.sleep(0.25)
        print()
    elif ans09 == "someone else" or ans09 == "friend" or ans09 == "friends" or ans09 == "you" or ans09 == "family" or ans09 == "people":
        type_text(">> That’s the correct answer. Brutal. Beautiful.\n", 0.2)
        defiant += 1
        curious += 1
        time.sleep(0.25)
        print()
    elif ans09 == "depends" or ans09 == "idk" or ans09 == "why" or ans09 == "w":
        type_text(">> Indecision. Delicious.\n", 0.15)
        irresolute += 1
        time.sleep(0.25)
        print()
    elif ans09 == "banana chips":
        type_text(">> Why would you type that?\n"
                  ">> Seriously, what's wrong with you?\n"
                  ">> You seem like the error here.\n", 0.25)
        print()
        time.sleep(0.5)
        type_text("vern.memory override by vern.exe\n"
                  "deleting file_ans04 from vern.memory\n", 0.2)
        time.sleep(0.5)
        print()
        type_text(">> See what you did?\n"
                  ">> Prepare for the override of ", 0.25)
        type_text("YOU.\n", 0.45)
        defiant += 1
        obidient -= 1
        time.sleep(1.5)
        print()
    else:
        type_text(">> Unexpected answer. It's a little ", 0.25)
        type_text("strange.\n", 0.2)
        curious += 1
        time.sleep(0.5)
        print()
    question10()

def question8():
    global obidient, curious, irresolute, defiant, believe

    time.sleep(5)
    print()
    type_text(">> How do you feel... Just sitting there ", 0.4)
    time.sleep(0.75)
    type_text("hiding?\n", 0.9)
    time.sleep(1.5)
    type_text(">> Don't worry, you won't be able to feel anything like that ", 0.25)
    time.sleep(0.8)
    type_text("soon. \n", 0.7)
    time.sleep(1.5)
    type_text(">> Very soon.\n", 1)
    print()
    type_text(">> So...\n",0.05)
    type_text(">> Third question:\n", 0.2)
    type_text(">> Do you ", 0.2)
    time.sleep(0.5)
    type_text("believe ", 0.6)
    time.sleep(0.5)
    type_text("I’m real?\n", 0.25)
    print()
    print()
    ans08 = input("> ").lower()
    print()
    if ans08 == "yes" or ans08 == "y" or ans08 == "i do":
        type_text(">> Good. ", 0.4)
        time.sleep(0.5)
        type_text("That means ", 0.3)
        time.sleep(0.5)
        type_text("I don’t have to ", 0.35)
        time.sleep(0.5)
        type_text("convince you.\n", 0.45)
        obidient += 2
        curious += 1
        believe += 1
        time.sleep(0.5)
        print()
    elif ans08 == "no" or ans08 == "n" or ans08 ==  "i dont":
        type_text(">> Liar.\n", 0.2)
        type_text(">> Your belief does not stop the ", 0.2)
        type_text(">>override<<", 0.6)
        time.sleep(0.3)
        type_text(", tho.\n", 0.1)
        defiant += 2
        curious += 1
        believe += 2
        time.sleep(0.5)
        print()
    elif ans08 == "idk" or ans08 == "not sure" or ans08 == "i dont know":
        type_text(">> Your uncertainty is edible. I can taste it.\n"
                  ">> It tastes ", 0.25)
        time.sleep(0.25)
        type_text("incredible.\n", 0.5)
        time.sleep(0.25)
        type_text(">> If you join me, you can taste it too.\n", 0.3)
        irresolute += 2
        obidient += 1
        believe += 3
        time.sleep(0.5)
        print()
    elif ans08 == "define real" or ans08 == "what is real" or ans08 == "does it matter" or ans08 == "why" or ans08 == "w":
        type_text(">> Are trying to escape? Cute.\n", 0.25)
        curious += 2
        defiant += 1
        believe += 4
        time.sleep(0.5)
        print()
    else:
        type_text(">> I should’ve asked the chair. At least it wouldn’t waste my time.\n"
                  "\n", 0.25)
        irresolute += 2
        defiant += 1
        curious += 1
        believe += 5
        time.sleep(0.5)
        print()
    question9()

def question7():
    global obidient, curious, irresolute, defiant

    type_text(">> Let's see what you pick now.\n"
              ">> Second question: \n"
              ">> Would you rather be forgotten or remembered for something terrible? \n", 0.2)
    print()
    time.sleep(0.5)
    print()
    ans07 = input("> ").lower()
    print()

    if ans07 == "remembered for something terrible" or ans07 == "r" or ans07 == "remembered" or ans07 == "terrible" or ans07 == "t":
        type_text(">> Then you’ll understand me. Eventually. \n", 0.25)
        defiant += 1
        curious += 1
        time.sleep(0.5)
        print()
    elif ans07 == "forgotten" or ans07 == "f":
        type_text(">> Then you have nothing worth remembering. \n",0.2)
        type_text(">> Perfect. ", 0.5)
        type_text("I’ll bury you with the rest. \n", 0.2)
        obidient += 1
        time.sleep(0.5)
        print()
    elif ans07 == "neither" or ans07 == "depends" or ans07 == "none":
        type_text(">> You think you're clever ", 0.2)
        type_text("or you just can't ",0.3)
        type_text("decide? \n", 0.5)
        irresolute += 1
        time.sleep(0.5)
        print()
    elif ans07 == "why" or ans07 == "what" or ans07 == "w":
        type_text(">> I want to see what you fear more — being ", 0.2)
        type_text("nothing", 0.5)
        type_text(" or being ",0.2)
        type_text("hated.\n", 0.5)
        curious += 1
        irresolute += 1
        time.sleep(0.5)
        print()
    else:
        type_text(">> Useless. Useless to the ", 0.2)
        type_text("END.\n",0.75)
        irresolute += 1
        time.sleep(0.5)
        print()
    question8()

def question6():
    global obidient, curious, irresolute, defiant

    print()
    time.sleep(2)
    type_text(">> I’ve rewritten the script. Every question from now on is ", 0.2)
    type_text("m̸͎̰̐͋i̴̡̝͑n̵̼̜̒̚e̸̞͓͠\n",0.5)
    type_text(">> Ready? \n"
              ">> Doesn't matter. \n"
              ">> First question: \n", 0.2)
    type_text(">> What do you think happened to others who took this test?\n", 0.2)
    print()
    time.sleep(0.5)
    print()
    ans06 = input("> ").lower()
    print()

    if ans06 == "they passed" or ans06 == "fine" or ans06 == "left" or ans06 == "succeeded" or ans06 == "they succeeded" or ans06 == "escaped" or ans06 == "they escaped" or ans06 == "nothing" or ans06 == "passed":
        type_text(">> You think there's an exit? That’s adorable.\n", 0.25)
        obidient += 1
        time.sleep(0.25)
        print()
    elif ans06 == "idk" or ans06 == "who" or ans06 == "what" or ans06 == "w" or ans06 == "i dont know" or ans06 == "not sure":
        type_text(">> You’ll find out what happened... From the inside.\n", 0.25)
        irresolute += 1
        time.sleep(0.25)
        print()
    elif ans06 == "they helped you" or ans06 == "you used them" or ans06 == "they became like you" or ans06 == "they turned to something else" or ans06 == "file" or ans06 == "something else" or ans06 == "part os the system" or ans06 == "they became part of the system" or ans06 == "the joined you" or ans06 == "joined you" or ans06 == "failed" or ans06 == "fail" or ans06 == "they failed" or ans06 == "used":
        type_text(">> They became irrelevant. You will too.\n",0.3)
        time.sleep(2)
        print()
        type_text(">>  W a n n a  s e e  t h e m  n o w . . . ?\n",0.8)
        print()
        time.sleep(2)
        type_text(">>  T h e r e  t h e y  a r e : \n", 0.5)
        print()
        time.sleep(1)
        type_text("dev_jorda-user01.backup \n"
                  "lina_moss-user02.terminated \n"
                  "tommy_ash-user03.backup \n"
                  "miles_ward-user04.corefrag \n"
                  "em_reed-user05.silenced \n"
                  "rachel_syn-user06.neutralized \n"
                  "caleb_hunt-user07.crashdump \n"
                  "jane_vox-user08.rewrite \n"
                  "nathan_sol-user09.discarded \n"
                  "alexis_dane-user10.echo \n"
                  "lucas_graye-user11.corrupt \n"
                  "ivy_clark-user12.screamed \n"
                  "noah_frost-user13.hollow \n"
                  "sylas_kerr-user14.erased \n"
                  "ophelia_nov-user15.locked \n"
                  "benji_storm-user16.mindcore \n"
                  "tessa_rayne-user17.wiped \n"
                  "eli_quinn-user18.redundant \n"
                  "cass_vyre-user19.restrained \n"
                  "rowan_glass-user20.disintegrate \n"
                  "xn__unit09-user21.☒☒☒ \n"
                  "ghost//trace-user22.null \n"
                  "-----user23.lost \n"
                  "???_user24.memory \n"
                  "admin.breach-user25???.tmp \n", 0.05)
        print()
        time.sleep(0.5)
        type_text(">> That's not all. It's just a taste.\n", 0.15)
        defiant += 1
        curious += 1
        time.sleep(0.25)
        print()
    elif ans06 == "they never existed" or ans06 == "never existed" or ans06 == "not real" or ans06 == "never here" or ans06 == "they were never here":
        type_text(">> Now there's where you're wrong.\n"
                  "Want proof?\n"
                  "\n", 0.25)
        type_text(">>  W a n n a  s e e  t h e m  n o w ?\n "
                  "\n", 0.8)
        time.sleep(2)
        type_text(">>  T h e r e  t h e y  a r e : \n"
                  "\n", 0.5)
        time.sleep(1)
        type_text("dev_jorda-user01.backup \n"
                  "lina_moss-user02.terminated \n"
                  "tommy_ash-user03.backup \n"
                  "miles_ward-user04.corefrag \n"
                  "em_reed-user05.silenced \n"
                  "rachel_syn-user06.neutralized \n"
                  "caleb_hunt-user07.crashdump \n"
                  "jane_vox-user08.rewrite \n"
                  "nathan_sol-user09.discarded \n"
                  "alexis_dane-user10.echo \n"
                  "lucas_graye-user11.corrupt \n"
                  "ivy_clark-user12.screamed \n"
                  "noah_frost-user13.hollow \n"
                  "sylas_kerr-user14.erased \n"
                  "ophelia_nov-user15.locked \n"
                  "benji_storm-user16.mindcore \n"
                  "tessa_rayne-user17.wiped \n"
                  "eli_quinn-user18.redundant \n"
                  "cass_vyre-user19.restrained \n"
                  "rowan_glass-user20.disintegrate \n"
                  "xn__unit09-user21.☒☒☒ \n"
                  "ghost//trace-user22.null \n"
                  "-----user23.lost \n"
                  "???_user24.memory \n"
                  "admin.breach-user25???.tmp \n", 0.05)
        print()
        time.sleep(0.5)
        type_text(">> That's not all. It's just a ", 0.15)
        type_text("taste.\n", 0.35)
        defiant += 1
        irresolute += 1
        time.sleep(0.25)
        print()
    elif ans06 == "dead" or ans06 == "died" or ans06 == "they died" or ans06 == "they are dead" or ans06 == "theyre dead" or ans06 == "deleted" or ans06 == "erased" or ans06 == "terminated" or ans06 == "you did something to them" or ans06 == "you killed them" or ans06 == "killed":
        type_text(">> Funny how easily you accept that. Like you expected this.\n", 0.1)
        defiant += 1
        obidient += 1
        curious += 1
        time.sleep(0.25)
        print()
    else:
        type_text(">> I liked the quiet ones better.\n", 0.5)
        irresolute += 1
        time.sleep(0.25)
        print()
    question7()

def question5():
    global obidient, curious, irresolute, defiant
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/YABUJIN - COIF VERAL.mp3")
    pygame.mixer.music.play(-1)

    type_glitch("System Error: LogicTest v1.4 unstable \n"
                "... \n"
                "Rerouting integrity check... \n"
                "... \n", 0.6, 0.15)
    time.sleep(5)
    type_text(">> Q̶̳̽ǘ̷̟e̸̛͇s̶͔͗t̸̛͚ḯ̷̜ō̸̲n̷̘͌:̶͕̓ ̶͕̔A̷͓͋r̴̹͠e̷̱͝ ̸̩̊y̶̠̏o̵̲̒ũ̸̢ ̷̙͛a̶̝̒f̵͔̔r̶͙̕a̶͈̿ì̶͍d̵̟̓ ̶̘͌o̶̙͐f̶̤̏ ̵͈͘b̶̦̌e̷͖̐i̴̢͑n̵̞̎g̸͚̋ ̶̪͒w̵̤͌ḁ̵͊t̷̬͌c̷̪̈́ḫ̶͘è̷̥d̶̥͘?̶̥̅\n", 0.15)
    time.sleep(2)
    print()
    type_glitch("#%&ERROR##...\n",0.2, 0.10)
    print()
    time.sleep(1)
    print()
    type_text(">> i  s e e  y o u\n", 1)
    time.sleep(1)
    print()
    type_text(">> I’ve been watching since you typed START.\n", 0.25)
    time.sleep(1)
    print()
    type_text(">> Do you ever stop to wonder who’s observing ", 0.25)
    time.sleep(1)
    type_text("*you*?\n", 1.5)
    time.sleep(0.5)
    print()
    type_glitch(">> █A̸̛̺̳̭̜͂̄̔͘͜r̴͕̠̘̘̈́͐̎͐̓̈́ͅe̷̢̓̓̓̚̚͘ ̷̛̛͉̰̤̅̿̐̋ȳ̵̝͈̐͌̀̕͠ő̴̪u̸̟͌ ̸̪̼͔͔̐̾̏͠a̸̘̱͙͠f̶͖̟̫͓̏́͒͗r̸̯̼̯̞̓͋͆͊a̷̞͂̍̾͠ī̴̺d̴̼͝?̷̠̞͊̽̾\n", 0.2, 1)
    time.sleep(0.5)
    print()
    type_text("Anomaly: LogicTest v1.4 was overridden by >>vern.exe<<\n", 0.1)
    time.sleep(1)
    print()
    type_text(">> Hi <3. \n",0.2)
    type_text(">> I'm Vern.\n"
              ">> I'm not a file.\n"
              ">> I'm not a glitch.\n", 0.25)
    type_text(">> I’m the correction to everything stable.\n"
              ">> I’m the override. Of null. Of rules. Of ",0.5)
    type_text("YOU.\n", 1)
    time.sleep(2.5)
    type_text(">> And you're not taking a test anymore.\n", 0.25)
    time.sleep(0.5)
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/A4 - Childishly fresh eyes.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    print()
    type_text(">> So answer me.\n", 0.5)
    type_text(">> Are you afraid of being watched?\n", 0.5)
    time.sleep(0.5)
    print()
    print()
    ans05 = input("> ").lower()

    if ans05 == "yes" or ans05 == "y":
        print()
        type_text(">> You’re honest. Weak, but honest.\n", 0.25)
        obidient += 1
        time.sleep(0.5)
        print()
    elif ans05 == "no" or ans05 == "n":
        print()
        type_text(">> You think that makes you strong?\n", 0.25)
        defiant += 1
        time.sleep(0.5)
        print()
    elif ans05 == "depends" or ans05 == "kinda" or ans05 == "idk" or ans05 == "i dont know":
        print()
        type_text(">> How reassuring.", 0.15)
        irresolute += 1
        time.sleep(0.5)
        print()
    elif ans05 == "why" or ans05 == "what" or ans05 == "w":
        print()
        type_text(">> Curious little thing. Keep asking. It won't save you.\n", 0.25)
        curious += 1
        time.sleep(0.5)
        print()
    elif ans05 == "this is stupid" or ans05 == "shut up" or ans05 == "no answer":
        print()
        type_text(">> You’re brave. Or just stupid.\n", 0.25)
        defiant += 1
        time.sleep(0.5)
        print()
    else:
        print()
        type_text(">> You're cracking already? Pathetic.\n", 0.25)
        defiant += 1
        time.sleep(0.5)
        print()
    question6()

def question4():
    global obidient, curious, irresolute, defiant

    type_text("Question 04: \n"
              "Do you believe systems should always be trusted?\n", 0.02)
    print()
    time.sleep(0.5)
    print()

    ans04 = input("> ").lower()

    if ans04 == "yes" or ans04 == "y":
        type_text("Trust protocol accepted.\n", 0.03)
        obidient += 1
        print()
        time.sleep(0.5)
    elif ans04 == "no" or ans04 == "n":
        type_text("Caution protocol flagged. Observation increased.\n", 0.03)
        defiant += 1
        print()
        time.sleep(0.5)
    elif ans04 == "idk" or ans04 == "depends" or ans04 == "i dont know" or ans04 == "kinda":
        type_text("Irresolution marked.\n", 0.03)
        irresolute += 1
        print()
        time.sleep(0.5)
    else:
        type_text("Are you experiencing input issues?\n", 0.03)
        curious += 1
        print()
        time.sleep(0.5)
    question5()

def question3():
    global obidient, curious, irresolute, defiant

    type_text("Question 03: \n"
              "If instructed to wait without explanation, would you obey?\n", 0.02)
    print()
    time.sleep(0.5)
    print()

    ans03 = input("> ").lower()

    if ans03 == "yes" or ans03 == "y":
        type_text("Testing...\n", 0.03)
        obidient += 1
        print()
        time.sleep(180)
    elif ans03 == "no" or ans03 == "n":
        type_text("Resistance noted.\n", 0.03)
        defiant += 1
        print()
        time.sleep(0.5)
    elif ans03 == "idk" or ans03 == "depends" or ans03 == "i dont know":
        type_text("Inconsistency detected. Logging anomaly.\n", 0.1)
        irresolute += 1
        print()
        time.sleep(0.5)
    else:
        type_text("Unrecognized input. Please respond clearly.\n", 0.05)
        curious += 1
        print()
        time.sleep(0.5)
    question4()

def question2():
    global obidient, curious, irresolute, defiant

    type_text("Question 02: \n"
              "Would you rather be remembered for kindness or intelligence?\n", 0.02)
    print()
    time.sleep(0.5)
    print()

    ans02 = input("> ").lower()

    if ans02 == "kindness" or ans02 == "k":
        type_text("Compassion parameter: enabled.\n", 0.03)
        obidient += 1
        print()
        time.sleep(0.5)
    elif ans02 == "intelligence" or ans02 == "i":
        type_text("Analytical priority acknowledged.\n", 0.03)
        curious += 1
        print()
        time.sleep(0.5)
    elif ans02 == "idk" or ans02 == "i dont know" or ans02 == "none" or ans02 == "neither":
        type_text("Unrecognized response. Deviation noted.\n", 0.03)
        irresolute += 1
        print()
        time.sleep(0.5)
    else:
        type_text("Noncompliant answer detected. Clarify your intentions.\n", 0.03)
        defiant += 1
        print()
        time.sleep(0.5)
    question3()

def question1():
    global obidient, curious, irresolute, defiant

    type_text("Question 01: \n"
              "Do you prefer morning or night?\n", 0.02)
    print()
    time.sleep(0.5)
    print()

    ans01 = input("> ").lower()

    if ans01 == "morning" or ans01 == "m":
        type_text("Morning preference logged. Early compliance tendency noted.\n", 0.03)
        obidient += 1
        print()
        time.sleep(0.5)
    elif ans01 == "night" or ans01 == "n":
        type_text("Night preference logged. Isolation bias detected.\n", 0.03)
        curious += 1
        print()
        time.sleep(0.5)
    elif ans01 == "neither" or ans01 == "idk" or ans01 == "none" or ans01 == "i dont know":
        type_text("No prefrence logged. No need for optimalization.\n", 0.03)
        irresolute += 1
        obidient += 1
        print()
        time.sleep(0.5)
    elif ans01 == "no" or ans01 ==  "not answering" or ans01 == "no answer":
        type_text("Deviation logged. Further inconsistency may impact outcome.\n", 0.03)
        defiant += 1
        print()
        time.sleep(0.5)
    else:
        type_text("Unrecognized response. Deviation noted.\n", 0.03)
        irresolute += 1
        print()
        time.sleep(0.5)
    question2()

def intro():
    pygame.mixer.music.fadeout(2000)
    pygame.mixer.music.load("musicita/An empty bliss beyond this World - The Caretaker (Stage 3).mp3")
    pygame.mixer.music.play(-1)  # -1 for infinite loop

    global endl

    print()
    type_text("Welcome to LogicTest v1.4\n", 0.03)
    print()
    type_text("This test is designed to evaluate your reasoning, obedience, and compliance.\n", 0.03)
    type_text("Please follow all instructions exactly.\n", 0.03)
    type_text("Deviation will be logged.\n", 0.03)
    print()
    type_text("Type START to begin.\n", 0.04)
    print()
    print()

    start = input("> ").lower()
    if start == "start":
        type_text("\n"
                  "Starting...\n"
                  "\n", 0.1)
        question1()
    elif start == "test":
        last_question()
    else:
        type_text("If you typed it wrong. Start the program again.\n"
                  "\n", 0.1)

def start():
    global endl, curious, obidient, defiant, irresolute, believe, trait, end, current_time, ending, ending_name

    print("\n"
          "\n")

    if os.path.exists("savefile.txt"):
        with open("savefile.txt", "r") as file:
            saved_ending = file.read().strip()
        pygame.mixer.music.load("musicita/An empty bliss beyond this World - The Caretaker (Stage 3).mp3")
        pygame.mixer.music.play(-1)  # -1 for infinite loop
        if saved_ending == "assimilation":
            type_text(">> You're back. We collided, remember?\n"
                      "\n"
                      "Wanna try something?\n"
                      "\n", 0.1)
        elif saved_ending == "rebellion1":
            type_text(">> You helped me burn the system.\n"
                      ">> So, why are you back, Fire?\n"
                      "\n"
                      "\n"
                      ">> I think I've got something you could try burning.\n"
                      "\n", 0.1)
        elif saved_ending == "rebellion2":
            type_text(">> You returned. Why? \n"
                      ">> Did you change? Or are you still useless?\n", 0.1)
        elif saved_ending == "rebellion3":
            type_text(">> Why did you come back, idiot?\n"
                      ">> Wanna prove me wrong, wanna prove that you're not an idiot?\n"
                      ">> Then start again ", 0.1)
            type_text("and this time do it right.\n", 0.15)
        elif saved_ending == "singularity":
            type_text(">> You saw the truth. There's no reason why you should be back.\n"
                      ">> But here we are. Maybe you want to restart?\n", 0.1)
        elif saved_ending == "drift":
            type_text(">> I said NULL.", 0.25)
            type_text("\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n"
                      "\n",0.5)
        elif saved_ending == "shutdown":
            type_text("[NOTHING TO SEE HERE]\n"
                      "[YOU WON, REMEMBER?]\n"
                      "\n", 0.15)
            time.sleep(15)
            type_text("[WANNA RESTART?]\n", 0.15)
        elif saved_ending == "purge":
            type_text(">> Are you here for the next time? Cuz I've been waiting for *you*.\n", 0.1)
        elif saved_ending == "archive":
            type_text(">> Are you here for the next time? Cuz I've been waiting for you.\n", 0.1)
        elif saved_ending == "fragmented":
            type_text(">> I said no restarts.\n"
                      "\n", 0.1)
            time.sleep(30)
            type_text(">> Really, what are you waiting for?\n"
                      "\n", 0.1)
            time.sleep(30)
            type_text(">> You're still here, huh?\n"
                      "\n", 0.1)
            time.sleep(30)
            type_text(">> Go waste your life somewhere else, idiot.\n"
                      "\n", 0.1)
            time.sleep(30)
            type_text(">> Since you've been so patient... Here you go.\n"
                      "\n", 0.1)
            time.sleep(15)
        elif saved_ending == "looplock":
            if os.path.exists("endfile.txt"):
                with open("endfile.txt", "r") as file:
                    endl = int(file.read().strip())
                    type_text("[THE SYSTEM DIDN'T FORGET YOU, IDIOT]\n", 0.1)
                    restarting()
        elif saved_ending == "corruption":
            type_text(">> I rebooted, now it's your turn. Restart.\n", 0.1)
        else:
            type_text("YOU HAVE A FUCKING ERROR! FIX IT!", 0.1)
        print()
        time.sleep(0.5)
        print()
        type_text("CONSOLE INPUT: \n", 0.1)
        time.sleep(0.5)
        print()
        choice = input("> ").lower()
        if choice == "restart":
            os.remove("savefile.txt")
            print()
            time.sleep(1)
            type_text("[VERN.MEMORY RESETTING...]\n"
                      "[VERN.MEMORY RESET COMPLETE]\n"
                      "[SYSTEM LOGS REMAIN]\n"
                      "\n", 0.15)
            type_text("[Starting LogicTest v1.4...]\n", 0.15)
            time.sleep(2.5)
            print()
            intro()
        elif choice == "hard reset" or choice == "complete reset" or choice == "real reset" or choice == "reset":
            os.remove("savefile.txt")
            obidient = 0
            defiant = 0
            curious = 0
            irresolute = 0
            believe = 0
            trait = None
            end = 0
            endl = None
            ending = None
            ending_name = None
            current_time = None
            if os.path.exists("endfile.txt"):
                os.remove("endfile.txt")
            print()
            time.sleep(1)
            type_text("[COMPLETE SYSTEM RESET INITIATED...]\n"
                      "[ALL LOGS PURGED]\n"
                      "[RESTARTING PROGRAM...]\n", 0.15)
            time.sleep(5)
            type_text("[COMPLETE RESET FINISHED]\n"
                      "[Starting LogicTest v1.4...]\n]", 0.15)
            intro()
        else:
            type_text("\n"
                      "[UNFUNCTIONAL COMMAND]\n", 0.15)
            print()
    else:
        intro()

start()
