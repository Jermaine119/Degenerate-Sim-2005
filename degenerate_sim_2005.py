import random
import sys

morality_level = 1000
player_level = 0
player_health = 40

is_addicted = False
addiction_roll_interval = 3  # Roll for addiction every 3 moves
addiction_threshold = 2000  # Threshold for addiction survival roll

#This resets the player stats when the game is restarted from a fail state
def restart_game():
    global morality_level, player_level, player_health, is_addicted
    morality_level = 1000
    player_level = 0
    player_health = 40
    is_addicted = False

def addiction_func():
    global morality_level, player_level, player_health, addiction_threshold
    addiction_roll = random.randint(1, 5000) + (morality_level + (player_level * 100))
    if addiction_roll >= addiction_threshold:
            player_level += 2
            morality_level -= 50
            print("You feel a rush...")
            print(f"The substance increases your level to {player_level}, and your morality decreases to {morality_level}")
    
    else:
        player_health -= 10
        print("Your addiction causes complications!")
                # Handle consequence of addiction, e.g., lose health or die
        print(f"Player health reduced to {player_health}")
        if player_health <= 0:
            addict_death = input("You hath been blinded by your addictions. You die alone with soiled trousers and your system full of whatever it is you were taking. Restart? y/n: ")
            if addict_death.lower() == "y":
                restart_game()
                main()
            elif addict_death.lower() == "n":
                sys.exit()

def wrong_yes_no():
    print()
    print("Just choose one, alright?")

def main():
    global morality_level, player_level, player_health
    print()
    print()
    print()
    print()
    print("Welcome to Degenerate Sim 2005! Coded in Python by Jermaine Cunningham and Ben Griffiths.")
    print()
    print()
    print("The game begins with you as a lowly Office Worker in a city that is as immoral as it is metropolitan (who'd have thought?). Struggling day-to-day, trying to climb the corporate ladder")
    print("You have the choice to climb this ladder, and become rich, powerful, and influential!")
    print("Your actions have consequences, however, and there will be pitfalls. Each action has a consequence, and will subsequently impact your morality")
    print()
    print("Will you be a kind and caring leader, or a cruel and pragmatic businessman? The choice is yours!")
    print()
    print(f"Morality: {morality_level}, Player Level: {player_level}, Player Health: {player_health}")
    
    move_count = 0
    
    # Introduction section
    print()
    print()
    print("You are a Customer Service Assistant at a call centre. Your boss has asked you to work late.")
    while True:
        choice = input("What do you do? (1. Work late, 2. Go home, 3. Give up and admit that you can't handle life.): ")
        if choice == "1":
            work_late(is_addicted, addiction_roll_interval, addiction_threshold)
        elif choice == "2":
            straightedge_section_2()
        elif choice == "3":
            print()
            quit_fail = input("You cowardly coward! Restart? (y/n): ")
            if quit_fail.lower() == "y":
                restart_game()
                main()
            elif quit_fail.lower() == "n":
                sys.exit()
            break
        else:
            print()
            print("You really are a fool, aren't you?.")

def work_late(is_addicted, addiction_roll_interval, addiction_threshold):
    while True:
        global morality_level, player_level, player_health
        print()
        print()
        print()
        print()
        print("You work late and completely exhaust yourself for an extra few quid. During your shift, you hear some deadheads outside fighting and listening to hard house music. Certainly sounds more interesting than whatever you were doing all day.")
        print()
        work_choice = input("Outside your place of work in a nearby alley, you notice a policeman wrestling a hooded gentleman wearing a tracksuit into the back of (what you would assume to be) a police car. As they leave, you notice a parcel with a mysterious substance inside has been left behind. (1. Continue straight towards home, 2. Take substance, 3. Take the parcel to the police station): ")
        if work_choice == "1":
            # Continue to the next section of the game
            straightedge_section_2()
        elif work_choice == "2":
            player_level += 2
            morality_level -= 100
            is_addicted = True
            print()
            print()
            print()
            print()
            print("You take the mysterious substance and feel a rush of euphoria... and a cramp in your bowels.")
            print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
            addict_section_2(is_addicted, addiction_roll_interval, addiction_threshold)
        elif work_choice == "3":
            print()
            print()
            print()
            print()
            arrest_choice = input("You take the parcel to the police station. Upon arrival, you are immediately swarmed by several policemen who pin you to the ground, cuff you, and accuse you of drug trafficking. You are charged and sentenced to 69,873 years in a maximum security prison. Try again, do-gooder. Restart? (y/n): ")
            if arrest_choice.lower() == "y":
                restart_game()
                main()
            elif arrest_choice.lower() == "n":
                sys.exit()
            break
        else:
            print()
            print("Pay attention. Choose 1, 2, or 3.")

def addict_section_2(is_addicted, addiction_roll_interval, addiction_threshold):
    while True:
        global morality_level, player_level, player_health
        print()
        print()
        print()
        print()
        indust_choice_1 = input("High as a kite, you continue on your path towards home. You now find yourself at the industrial estate. There is an acrid smell in the air and in your peripheral vision you see a bearded gentleman with some missing teeth who appears to be the origin of the smell. He smiles at you, though it's hardly a warm smile. What will you do? (1. Tweak out and attack him, 2. Awkwardly walk away, 3. Offer to sell some of your mysterious wonder drug.): ")
        if indust_choice_1 == "1":
            print()
            print()
            print()
            print()
            indust_fail_1 = input("That didn't go well. You frantically flail your fists around and fall over, hitting your head on the pavement and killing yourself instantly. The bearded gentleman then robs you of your stash (and your dignity). Well done, druggie. Restart? (y/n): ")
            if indust_fail_1.lower() == "y":
                restart_game()
                main()
        elif indust_choice_1 == "2":
            print()
            addiction_func()
            walk_away_path(is_addicted, addiction_roll_interval, addiction_threshold)
        elif indust_choice_1 == "3":
            print()
            addiction_func()
            sell_path_1(is_addicted, addiction_roll_interval, addiction_threshold)
            break
        else:
            print()
            print("You really need to practice pressing buttons.")

def sell_path_1(is_addicted, addiction_roll_interval, addiction_threshold):
    while True:
        global morality_level, player_level, player_health
        print()
        print()
        print()
        print()
        sell_choice = input("The mans eyes widen with excitment as he snatches some of the substance from you, hands over some greasy, torn up money, and sprints into the night - barely holding up his trousers as he flees. Now what? (1. Die, 2. Keep walking home, 3. Go to ALDI and spend your hard earned cash): ")
        if sell_choice == "1":
            print()
            sell_fail = input("You begin shaking violently, the force of a thousand little elephants manifesting within you. Suddenly, your head explodes and leaves behind a very tough cleaning job. What did you think was going to happen? Restart? y/n: ")
            if sell_fail.lower() == "y":
                restart_game()
                main()
            elif sell_fail.lower() == "n":
                sys.exit()
        elif sell_choice == "2":
            print()
            addiction_func()
            sell_path_2(is_addicted, addiction_roll_interval, addiction_threshold)
        elif sell_choice == "3":
            print()
            addiction_func()
            aldi_path(is_addicted, addiction_roll_interval, addiction_threshold)
            break
        else:
            print()
            print("Is it really that hard to type 1, 2 or 3 into the terminal?")

def walk_away_path(is_addicted, addiction_roll_interval, addiction_threshold):
    while True:
        global morality_level, player_level, player_health
        print()
        print()
        print()
        print()
        walk_away_choice = input("You back away from the bearded gentleman and continue on towards home. You find yourself in the suburbs. The orange glow of the streetlights brings a comforting warmth that makes you feel slightly better about crackhead Brian Blessed giving you the eye. You have arrived at your flat, what will you do? (1. Go inside, 2. Go back and fight the hairy bikers, 3. Overdose on the substance.): ")
        if walk_away_choice == "1":
            print()
            print()
            print()
            print()
            home_end = input("You unlock the door and walk inside your flat. Exhausted, you lay your head down and drift away into unconsciousness, all the while dreaming about having a heart attack in your sleep so that you don't have to face another day at work. You have completed the game and acheived absolutely nothing. Restart? y/n: ")
            if home_end.lower() == "y":
                restart_game()
                main()
            elif home_end.lower() == "n":
                sys.exit()
        elif walk_away_choice == "2":
            print()
            print()
            print()
            print()
            fight_fail = input("You get a sudden burst of confidence and return to the industrial estate, where the two bearded gentlemen are conversing with one another. You walk straight up to them and land an epic suckerpunch on the biggest of the two. He goes down, and you feel a sense of triumph. In the same moment, the smaller of the two bearded gentlemen sneaks up behind you and knocks you out with a swift clout around the ear. As you are unconscious, the bearded gentleman robs your stash (and your dignity). Restart? y/n: ")
            if fight_fail.lower() == "y":
                restart_game()
                main()
            elif fight_fail.lower() == "n":
                sys.exit()
        elif walk_away_choice == "3":
            print()
            overdose_end = input("Seeing no other option, you take all of what is left of the substance and ingest it. You feel a rush of infinite euphoric bliss, and suddenly dissolve into a strange porridge-like gloop. You have completed the game and acheived death by drug. Well done! Restart? y/n: ")
            if overdose_end.lower() == "y":
                restart_game()
                main()
            elif overdose_end.lower() == "n":
                sys.exit()
            break
        else:
            print()
            print("Do me a favour, don't mess about sunshine.")

def sell_path_2(is_addicted, addiction_roll_interval, addiction_threshold):
    while True:
        global morality_level, player_level, player_health
        print()
        print()
        print()
        print()
        sell_choice_2 = input("You continue home and find yourself near the city centre, the giant glass eyesores pollute the dark skyline with a particular spitefulness. You seem to have forgotten where you live, your high risk lifestyle has left you confused and disoriented. What do you do? (1. Scream and run around frantically trying to find your way home, 2. Call a taxi, 3. Just go to ALDI after all.): ")
        if sell_choice_2 == "1":
            print()
            sell_fail_2 = input("You run around screaming trying to find your way home, and you end up falling off a nearby bridge to your death. You came so far, yet acheived so little. Restart? y/n: ")
            if sell_fail_2.lower() == "y":
                restart_game()
                main()
            elif sell_fail_2.lower() == "n":
                sys.exit()
        elif sell_choice_2 == "2":
            taxi_path(is_addicted, addiction_roll_interval, addiction_threshold)
        elif sell_choice_2 == "3":
            aldi_path(is_addicted, addiction_roll_interval, addiction_threshold)
            break
        else:
            print()
            print("You might think you're clever, but you need to choose a valid option.")

def taxi_path(is_addicted, addiction_roll_interval, addiction_threshold):
    while True:
        global morality_level, player_level, player_health
        print()
        print()
        print()
        print()
        taxi_choice = input("You manage to call a taxi from a nearby TARDIS. You wait around 45 minutes, and a black cab pulls up next to you. Inside the cab is a man in a suit who speaks to you with an Italian accent. He says that he and his associates have been watching you, and they like the way you do business. The man tells you that you should come with him if you want to start making some REAL cash. What will you do? (1. Lose control and attempt to murder the man, 2. Tell the man that you don't know what he's talking about and to take you home, 3. Go with him.): ")
        if taxi_choice == "1":
            print()
            taxi_fail = input("You suddenly lose control and become violent. You attack the man with extreme prejudice. Fully prepared for a fist fight to the death, the man has a trick up his sleeve - he pulls out a tommygun and riddles you with bullets. You have died and acheived nothing. Restart? y/n: ")
            if taxi_fail.lower() == "y":
                restart_game()
                main()
            elif taxi_fail.lower() == "n":
                sys.exit()
        elif taxi_choice == "2":
            addiction_func()
            taxi_home_path(is_addicted, addiction_roll_interval, addiction_threshold)
        elif taxi_choice == "3":
            addiction_func()
            mob_path_1()
            break
        else:
            print("This far into the game, you should know how to press 1, 2 or 3 by now.")

def taxi_home_path(is_addicted, addiction_roll_interval, addiction_threshold):
    while True:
        global morality_level, player_level, player_health
        print()
        print()
        print()
        print()
        taxi_home_choice = input("The man says nothing and drives you to the suburbs. As you get out and get ready to pay him, he simply speeds off. You can't help but wonder if you have missed something interesting. You find yourself at the suburbs. The orange glow of the streetlights brings a welcoming warmth that makes you feel slightly better about almost being murdered by Al Capone. You have arrived at your flat. What will you do? (1. Go inside, 2. Run after the taxi and call to the mysterious man, 3. Invade Paris): ")
        if taxi_home_choice == "1":
            print()
            print()
            print()
            print()
            home_end_2 = input("You unlock the door and walk inside your flat. Exhausted, you lay your head down and drift away into unconsciousness, all the while dreaming about having a heart attack in your sleep so that you don't have to face another day at work. You have completed the game and acheived absolutely nothing. Restart? y/n: ")
            if home_end_2.lower() == "y":
                restart_game()
                main()
            elif home_end_2.lower() == "n":
                sys.exit()
        elif taxi_home_choice == "2":
            mob_path_1()
        elif taxi_home_choice == "3":
            print()
            print()
            print()
            print()
            invade_end = input("You gather all your strength, and set about marching to Paris. After many gruelling miles, you reach the French border and are immediately gunned down by armed guards. You're certainly no Adolf Hitler. Restart? y/n: ")
            if invade_end.lower() == "y":
                restart_game()
                main()
            elif invade_end.lower() == "n":
                sys.exit()
            break
        else:
            print()
            print("Just press one of the buttons you've been told to press, smartarse.")

def aldi_path(is_addicted, addiction_roll_interval, addiction_threshold):
    while True:
        global morality_level, player_level, player_health
        print()
        print()
        print()
        print()
        aldi_choice = input("You walk to the nearby ALDI and find yourself and the checkout with 70cl of their cheapest whisky and a pack of scotch eggs. As you wait in line, you feel a tap on your shoulder. You turn to find a man in a suit who speaks to you with an Italian accent, he says that he likes how you do business and that you should go with him if you want to start seeing some REAL cash. What do you do? (1. Throw the scotch eggs at him, 2. Go with him, 3. Scream and run away): ")
        if aldi_choice == "1":
            print()
            print()
            print()
            print()
            eggs_end = input("You become enraged and throw your scotch eggs with full force directly at the man. He stares at you intensely, a wild fire in his eyes. Suddenly, the man bursts into tears and runs away into the night. You feel accomplished but can't help feel you have missed something potentially interesting. Restart? y/n: ")
            if eggs_end.lower() == "y":
                restart_game()
                main()
            elif eggs_end.lower() == "n":
                sys.exit()
        elif aldi_choice == "2":
            mob_path_1(is_addicted, addiction_roll_interval, addiction_threshold)
        elif aldi_choice == "3":
            print()
            print()
            print()
            print()
            scream_fail = input("You scream in terror and run away from the man in fear. As you run away, you trip over the Pepsi multipack display and explode into a thousand million pieces. That was probably not the thing to do. Restart? y/n: ")
            if scream_fail.lower() == "y":
                restart_game()
                main()
            elif scream_fail.lower() == "n":
                sys.exit()
            break
        else:
            print()
            print("Really?")


def straightedge_section_2():
    global morality_level, player_level, player_health
    print("Welcome to Degenerate Sim 2005! Coded in Python by Jermaine Cunningham and Ben Griffiths.")
    input("Continue ")
    print()
    print("The game begins with you as a lowly Office Worker in a city that is as immoral as it is metropolitan (who'd have thought?). Struggling day-to-day, trying to climb the corporate ladder")
    input("Continue ")
    print()
    print("You have the choice to climb this ladder, and become rich, powerful, and influential!")
    input("Continue ")
    print()
    print("Your actions have consequences, however, and there will be pitfalls. Each action has a consequence, and will subsequently impact your morality")
    input("Continue ")
    print()
    print("Will you be a kind and caring leader, or a cruel and pragmatic businessman? The choice is yours!")
    input("Continue ")
    print()
    print(f"Morality: {morality_level}, Player Level: {player_level}, Player Health: {player_health}")
    
    move_count = 0
    
    # Introduction section
    print()
    print("You are a Customer Service Assistant at a call centre. Your boss has asked you to work late.")
    input("Continue ")
    while True:
        choice = input("What do you do? (1. Work late, 2. Go home, 3. Give up and admit that you can't handle life.): ")
        if choice == "1":
            work_late(is_addicted, addiction_roll_interval, addiction_threshold)
        elif choice == "2":
            straightedge_section_2()
        elif choice == "3":
            quit_fail = input("You cowardly coward! Restart? (y/n): ")
            if quit_fail.lower() == "y":
                restart_game()
                main()
            elif quit_fail.lower() == "n":
                sys.exit()
            break
        else:
            print()
            print("You really are a fool, aren't you?.")

def work_late(is_addicted, addiction_roll_interval, addiction_threshold):
    while True:
        global morality_level, player_level, player_health
        print("You work late and completely exhaust yourself for an extra few quid. During your shift, you hear some deadheads outside fighting and listening to hard house music. Certainly sounds more interesting than whatever you were doing all day.")
        input("Continue ")
        print("Outside your place of work in a nearby alley, you notice a policeman wrestling a hooded gentleman wearing a tracksuit into the back of (what you would assume to be) a police car.")
        input("Continue ")
        work_choice = input("As they leave, you notice a parcel with a mysterious substance inside has been left behind. (1. Continue straight towards home, 2. Take substance, 3. Take the parcel to the police station): ")
        if work_choice == "1":
            # Continue to the next section of the game
            straightedge_section_2()
        elif work_choice == "2":
            player_level += 2
            morality_level -= 100
            is_addicted = True
            print("You take the mysterious substance and feel a rush of euphoria... and a cramp in your bowels.")
            input("Continue ")
            print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
            # Continue to the next section of the game
            addict_section_2(is_addicted, addiction_roll_interval, addiction_threshold)
        elif work_choice == "3":
            print()
            print("You take the parcel to the police station. Upon arrival, you are immediately swarmed by several policemen who pin you to the ground, cuff you, and accuse you of drug trafficking.")
            input("Continue ")
            arrest_choice = input("You are charged and sentenced to 69,420 years in a maximum security prison. Try again, do-gooder. Restart? (y/n): ")
            if arrest_choice.lower() == "y":
                restart_game()
                main()
            elif arrest_choice.lower() == "n":
                sys.exit()
            break
        else:
            print("Pay attention. Choose 1, 2, or 3.")

def walk_away_path(is_addicted, addiction_roll_interval, addiction_threshold):
    while True:
        global morality_level, player_level, player_health
        print()
        print("You walk away from the situation, trying not to soil yourself as you put some distance between you and the bearded gentleman")
        print()
        walk_away_choice = input("You now find yourself in the suburbs. The orange glow of the streetlights brings a welcoming warmth To restart, press 1, 2 or 3")
        input("Continue ")
        if walk_away_choice == "1":
            restart_game()
            main()
        elif walk_away_choice == "2":
            restart_game()
            main()
        elif walk_away_choice == "3":
            restart_game()
            main()
            break
        else:
            print()
            print("Do me a favour, don't mess about sunshine.")


def straightedge_section_2():
    global morality_level, player_level
    
    player_level += 2
    morality_level += 100
    print("You return to work following a long night")
    print()
    input("Continue ")
    print()
    print(f"Your boss is impressed with your work so far, and gives you a promotion! Your level has increased to {player_level}, and your morality has increased to {morality_level}")
    print()
    input("Continue ")
    print()
    print("Your colleague leaves work early and forgets to lock their computer. They have a presentation on their computer they are ready to present to better exploit the working class and create money for the company ")
    print()
    input("Continue ")
    while True:
        choice = input("What do you do? (1. Steal the presentation, or 2. lock the computer?: ")
        
        if choice == "1":
            player_level += 2
            morality_level -= 100
            print("Congratulations! Your manager loved the idea, and you gained a promotion!")
            input("Continue ")
            print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
            path_1_2() 
        elif choice == "2":
            player_level -= 1
            morality_level += 100
            print("Unfortunately, your Manager heard about your altruism, and believes you are not ready to become a leader")
            print(f"Your level decreased to {player_level} and your morality increased to {morality_level}")
            path_1_2()
        else:
            print("Invalid choice. Please choose 1 or 2")

def path_1_2():
    global morality_level, player_level
    print("You decide to go to a bar following the conversation with your manager, and overhear some sensitive information that could make your company money.")
    print()
    input("Continue ")
    print()
    print("Insider trading like this is illegal and risky. Do you use this to your advantage?")
    while True:
        choice = input("What do you do? (1. Yes I want every advantage I can get!, or 2. No, I don't really feel like climbing the ladder like this: ")
        if choice == "1":
            player_level += 1
            morality_level -= 100
            print("You use the Insider information, and get a promotion in the Company!")
            input("Continue ")
            print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
            path_1_3()
        elif choice == "2":
            player_level += 1
            morality_level += 100
            print("You report the breach to your manager who fires the person above you and gives you their job.")
            print(f"Your level decreased to {player_level} and your morality increased to {morality_level}")
            path_1_3()
        else:
            print("Invalid choice. Please choose 1 or 2")

def path_1_3():
    global morality_level, player_level
    print()
    print("Your manager calls you into an off the books meeting. He asks you to help him embezzle money from the sick childrens hospital your company works closely with.")
    print()
    input("Continue ")
    print()
    print("This is an opportunity to obtain a lot of money for your Company, however it does mean literally stealing money from sick children")
    while True:
        choice = input("Do you agree to do this? (1. Yes, if I make more money now, the children can get more later, right?, or 2. No. Stealing from children is pretty low, even for me: ")
        if choice == "1":
            player_level += 1
            morality_level -= 100
            print("You attempt to embezzle the money. I hope taking money from sick children is worth it.")
            input("Continue ")
            print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
            path_1_4a()
        elif choice == "2":
            morality_level += 200
            print("You go against your managers wishes and choose the morally correct choice.")
            print(f"Your morality increased to {morality_level}")
            path_1_4b()
        else:
            print("Invalid choice. Please choose 1 or 2")
    
def path_1_4a():
    global morality_level, player_level
    input("Roll a dice to see if the embezzlement is successful ")
    embez_threshold = 5000
    embez_roll = random.randint(1, 5000) + (morality_level + (player_level * 100))
    if embez_roll >= embez_threshold:
        
        player_level += 2
        morality_level -= 100
        print("The embezzlement was a success!")
        input("Continue ")
        print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
        print()
        path_1_5a()
    else:
        player_level -= 1
        morality_level -= 50
        print("The embezzlement was a failure!")
        input("Continue ")
        print(f"Your level decreased to {player_level} and your morality decreased to {morality_level}")
        print()
        path_1_5b()
        
def path_1_4b():
    global morality_level, player_level
    input("Roll a dice to see what happens next")
    fired_threshold = 4000
    fired_roll = random.randint(1, 4000) + morality_level
    if fired_roll <= fired_threshold:
        player_level -= 1
        print("Your manager is feeling kind, and decides to keep you at the company, despite your actions.")
        input("Continue ")
        print(f"Your level decreased to {player_level}")
        print()
        path_1_5c()
    else:
        player_level == 0
        print("Your manager is furious with you, and calls you into his office")
        input("Continue ")
        print("You're fired! clear out your desk, you have 2 minutes before security 'escort' you out of the building")
        input("Continue ")
        print(f"Now get out of my sight! {morality_level}")
        print()
        ending_1b()

def path_1_5a():
    global morality_level, player_level
    print("Following the embezzlement, you find out there is a larger scandal regarding the sick childrens hospital, who have been using the children as a source of free labour.")
    print()
    input("Continue ")
    print()
    choice = input("Do you 1. Choose to report them to the authorities, or 2. Get in on the scam yourself? ")
    if choice == "1":
        player_level -= 2
        morality_level += 200
        print("You reported the company to the authorities, resulting in a demotion")
        input("Continue ")
        print(f"Your level decreased to {player_level} and your morality increased to {morality_level}")
        print()
        ending_1()
    elif choice == "2":
        player_level += 2
        morality_level -= 200
        print("You choose to get in on the scam, which results in a hefty promotion for you")
        print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
        print()
        ending_1()
    else:
        print("Invalid choice. Please choose 1 or 2")
        
def path_1_5b():
    global morality_level, player_level
    print()
    print("The embezzlement is a failure, and you are summarily demoted. Your manager is still impressed with your ambition however, and has another opportunity you may be interested in joining.")
    print()
    input("Continue")
    print()
    print("They explain to you that there is a larger scandal regarding the sick childrens hospital, who have been using the children as a source of free labour.")
    print()
    input("Continue ")
    print()
    print("They offer you the opportunity to join them in this 'business venture', and continue your upward trajectory in the business")
    print()
    input("Continue ")
    print()
    choice = input("Do you 1. Choose to report them to the authorities, or 2. Get in on the scam yourself? ")
    if choice == "1":
        player_level -= 2
        morality_level += 200
        print("You reported the company to the authorities, resulting in a demotion")
        input("Continue ")
        print(f"Your level decreased to {player_level} and your morality increased to {morality_level}")
        ending_1()
    elif choice == "2":
        player_level += 2
        morality_level -= 200
        print("You choose to get in on the scam, which results in a hefty promotion for you")
        print()
        input("Continue ")
        print()
        print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
        ending_1()
    else:
        print("Invalid choice. Please choose 1 or 2")
def path_1_5c():
    global morality_level, player_level
    print("After your demotion, a shady character approaches you about a possible business venture")
    print()
    print("They are not specific, however this would definitely be illegal. ")
    print()
    input("Continue ")
    print()
    choice = input("Do you 1. Take them up on their offer, making more money than you could have dreamed of otherwise or 2. Turn them down, and put your fate in your own hands ")
    if choice == "1":
        player_level += 2
        morality_level -= 200
        print("You take the shady character up on their offer.")
        input("Continue ")
        print("Turns out that crime does pay after all, and you're now making a tidy amount of money")
        print()
        print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
        ending_1()
    elif choice == "2":
        player_level -= 1
        morality_level += 200
        print("Your morals appear to be incredibly important to you. It's just a shame that 'being a good person' doesn;t necessarily pay the bills now, does it?")
        print()
        print(f"Your level decreased to {player_level} and your morality increased to {morality_level}")
        ending_1()
    else:
        print("Invalid choice. Please choose 1 or 2 ")
def ending_1():
    global morality_level, player_level
    print("Congratulations you got to the end of the game!")
    print()
    input("Continue ")
    print()
    print("Below is a list of your stats, confirming how well you managed to climb this corporate ladder")
    print()
    input("Continue ")
    print()
    print("Did greed and ambition win out, or did you place morality first? Lets find out!")
    print()
    input("Continue ")
    print()
    if player_level >= 7 and morality_level <= 900:
        print("OLIGARCH")
        restart_or_quit()
    elif player_level >= 7 and morality_level >= 900:
        print("CEO")
        restart_or_quit()
    elif 3 <= player_level < 7 and morality_level >= 900:
        print("MIDDLE MANAGER")
        restart_or_quit()
    elif 3 <= player_level < 7 and morality_level < 900:
        print("PUPPET")
        restart_or_quit()
    else:
        print("PEASANT")
        restart_or_quit()

def ending_1b():
    global morality_level
    print("Congratulations you got to the end of the game!")
    print()
    input("Continue ")
    print()    
    print("Below is a list of your stats, confirming how well you managed to climb this corporate ladder")
    print()
    input("Continue ")
    print()
    print("Did greed and ambition win out, or did you place morality first? Lets find out!")
    input("Continue ")
    if morality_level >= 1700:
        print("JUSTICE WARRIOR")
        restart_or_quit()
    elif morality_level >= 1000:
        print("DUBIOUS CHARACTER")
        restart_or_quit()
    else:
        print("IMMORAL IDIOT")
        restart_or_quit()
        
def restart_or_quit():
    choice = input("Would you like to 1. Restart the game, and see what other ending you can achieve? or 2. Quit the game ")
    if choice == "1":
        restart_game()
        main()
    elif choice == "2":
        sys.exit()
    else:
        print("Invalid input. Choose 1. Restart the game or 2. Exit the game")

def mob_path_1():
    global morality_level, player_level, player_health
    print("The Italian man in the expensive suits lights a cigarette and takes a drag.")
    print()
    input("Continue ")
    print()
    print("I represent an organisation called 'The Firm'. You can call me Jimmy. We've had our eye on you for some time now, and we believe you could make an amazing addition to our, ahem, 'family'.")
    print()
    input("Continue ")
    print()
    print("Let's just say that this isn't an offer you can refuse.")
    print()
    input("Continue ")
    print()
    print("Or I guess you can refuse, but then we'd have to kill ya, and that would be a real shame")
    print()
    input("Continue ")
    print()
    while True:
        choice = input("So, whaddya say? You wanna join The Firm, or you fancy sucking lead instead? 1. Join the firm, 2. Refuse the offer ")
        print()
        if choice == "1":
            player_level += 2
            morality_level += 200
            print("You choose to join the firm. I wonder what this means for your future")
            print()
            print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
            mob_path_2()
        elif choice == "2":
            print("You refuse the gentlemans offer, and tell him to shove it where the sun don't shine")
            print()
            input("Continue ")
            print()
            print("You're gonna regret this, punk! Noone messes with The Firm and gets away with it!")
            print()
            assassination_path()
        else:
            print("Invalid choice. Please choose 1 or 2")
        
def mob_path_2():
    global morality_level, player_level, player_health
    print("It's been a few months in The Firm and you've been assigned guard duty, making sure no-one enters or leaves the property.")
    print()
    input("Continue ")
    print()
    print("It's boring work, and your mind begins to wander.")
    print()
    input("Continue ")
    print()
    print("'How long is it going to be before I get another big break?' you think to yourself.")
    print()
    input("Continue ")
    print()
    print("'It's time to go.' A new guard approaches you and tells you your shift is over, you can go home for the night.")
    print()
    input("Continue ")
    print()
    print("Making your way out of the property, you hear a voice in the darkness")
    print()
    input("Continue ")
    print()
    print("From a half-cracked window you can hear your boss, known to everyone simply as 'The Don's voice coming from inside.")
    print()
    input("Continue ")
    print()
    print("You can tell from his tone that this is something he doesn't want an outsider overhearing, so you lean in closer to get a better listen.")
    print()
    input("Continue ")
    print()
    print("The information you hear clearly implicates 'The Don' is double-dealing against The Firm, in his own interests. You might be able to use this information to your advantage later, but staying here is risky")
    print()
    input("Continue ")
    print()
    while True:
        choice = input("Stay and listen to entire conversation, or leave and go home 1. Stay and listen 2. Leave and go home ")
        print()
        if choice == "1":
            player_level += 2
            morality_level -= 100
            print("You stay and listen in on The Don's full conversation. The information you've found out might prove to be invaluable for you going forward.")
            print()
            input("Continue ")
            print()
            print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
            mob_path_3a()
        elif choice == "2":
            morality_level += 100
            print("You go home and wonder if you made the right choice.")
            print()
            input("Continue ")
            print()
            print()
            print(f"Your morality increased to {morality_level}")
            mob_path_3b()
        else:
            print("Invalid choice. Please choose 1 or 2")
    
def mob_path_3a():
    global morality_level, player_level, player_health
    addiction_func()
    print("You receive a message from The Don on a slip of paper: 'Jimmy's a rat. Get down to the docks at 9pm so we can take care of him.'")
    print()
    input("Continue ")
    print()
    print("You've never been asked to do something so drastic before, maybe it's time for you to move up the ranks!")
    print()
    input("Continue ")
    print()
    print("9pm comes and you show up at the docks, looking around it seems completely empty")
    print()
    input("Continue ")
    print()
    print("'I'm pretty sure it said 9pm' you say to yourself. 'Where are they?'")
    print()
    input("Continue ")
    print()
    print("Two shadowy figures detach themselves from the darkness, and begin walking towards you.")
    print()
    print()
    input("Continue ")
    print()
    print("As they enter the light you can see one of them is The Don, with a wicked grin on his face")
    print()
    input("Continue ")
    print()
    print("'Here he is, get him on his knees'")
    print()
    input("Continue ")
    print("Pain lances down your neck as you recoil from a blow to the head from behind")
    print()
    input("Continue ")
    print()
    print("Your assailant forces you to kneel on the ground. 'Any last word, before we pump you full of lead?' The Don asks with a smirk")
    print()
    while True:
        choice = input("You have two choices 1. Tell him you know The Dons' secret, or 2. Quietly accept your fate ")
        print()
        if choice == "1":
            print("'Ballsy play, I'll give you that. Maybe you should have kept that to yourself'")
            print()
            input("Continue ")
            print()
            print("'Now I know you definitely can't keep your mouth shut'")
            print()
            input("Continue ")
            print()
            print("A gunshot rings through the night. Harsh laughter in your ears is the final sound you hear before everything goes black, and you return to nothingness.")
            mob_ending_2a()
        elif choice == "2":
            player_level += 2
            morality_level += 100
            print("You stare down the barrel of the gun. Defiance and hatred shining in your eyes.")
            print()
            input("Continue ")
            print()
            print("You got stones, kid. Well done, you passed the test.")
            print()
            input("Continue ")
            print()
            print(f"Your level increased to {player_level} and your morality increased to {morality_level}")
            mob_path_4()
        else:
            print("Invalid choice. Please choose 1 or 2")

def mob_path_3b():
    global morality_level, player_level, player_health
    addiction_func()
    print("It's been a couple of days, and you're called in for guard duty again.")
    print()
    input("Continue ")
    print()
    print("'Oi, daydreamer, it's time to go. Or did you want to stand around here all day?'")
    print()
    input("Continue ")
    print()
    print("You make your way across the property, happy to finish your shift.")
    print()
    input("Continue ")
    print()
    print("Walking past, you come across that same window, however this time it's shut and bolted.")
    print()
    input("Continue ")
    print()
    print("Peering in to the window, you can see The Don, and it looks like he's on the phone")
    print()
    input("Continue ")
    print()
    print("'I'm not missing another opportunity to get ahead' you say to yourself, as you make your way into the building and listen in at the keyhole.")
    print()
    input("Continue ")
    print("You listen in on the conversation, The Don is indeed double-crossing the firm for his own benefit. This might prove invaluable information later on.")
    print()
    input("Continue ")
    print()
    print("You feel the kiss of cold steel against your neck, and bitter breath in your ear.")
    print("'Well lookie hear, seems someones listening in on The Don'")
    print()
    input("Continue ")
    print()
    print("It's Jimmy, and he has you dead to rights.")
    input("Continue ")
    print()
    while True:
        choice = input("You have two choices 1. Attempt to overpower him, or 2. Pull your own blade ")
        print()
        if choice == "1" and player_health >= 30:
            player_level += 1
            morality_level += 100
            print("'You go for the knife and plunge it deep into Jimmy's chest'")
            print()
            input("Continue ")
            print()
            print("Hearing the commotion outside, The Don bursts through the door")
            print()
            input("Continue ")
            print()
            print("'Caught the rat listening in on my way out. He pulled a blade on me, so I took care of him' you tell The Don.")
            print()
            input("Continue ")
            print()
            print("Good. He was a Junkie anyway. Can't have any no good rats in The Firm. You go home, I'll get this taken care of.")
            print(f"Your level increased to {player_level} and your morality increased to {morality_level}")
            mob_path_4()
        elif choice == "1" and player_health < 30:
            print("A struggle ensues. In a weakened state due to the crippling addiction wracking your body, you're in no state to win this fight.")
            print()
            input("Continue ")
            print()
            print("Hearing the commotion, The Don bursts through the door in time to see Jimmy bury the steel through your heart")
            print()
            input("Continue ")
            print()
            print("As the life fades before your eyes you see a wicked grin spread across The Don's face. 'No place for weaklings like you here, kid' he says, as the darkness consumes you.")
            mob_ending_2a()
        elif choice == "2" and player_health > 30:
            player_level -= 1
            morality_level -= 50
            print()
            print("You pull your blade and catch Jimmy unawares, giving him a quick slice on his arm")
            print()
            input("Continue ")
            print()
            print("He lets out a pained shriek and drops to the floor. Hearing the commotion outside, The Don bursts through the door")
            input("Continue ")
            print()
            print("'Caught the rat listening in on my way out. He pulled a blade on me' you tell The Don.")        
            print()
            print("Quick as a flash The Don pulls the sidearm on Jimmy and unloads a flurry of shots into his chest.")
            print()
            print("The Don turns towards you and smirks 'I never liked that Junkie rat. I'll get someone to dispose of the filth. Consider this a warning. And remember, I own you.'")
            print()
            input("Continue ")
            print()
            print("Still shaking with a mix of adrenaline and fear, you exit the property")
            print(f"Your level decreased to {player_level} and your morality decreased to {morality_level}")
            mob_path_4()
        elif choice == "2" and player_health < 30:
            print()
            print("You go to pull your blade but your crippling addiction has left you weak. Jimmy is easily able to disarm you and throw you to the ground.")
            print()
            input("Continue ")
            print()
            print("'I wasn't listening, I swear!' you plead with Jimmy, as the door to the The Don's office opens.")
            print()
            input("Continue ")
            print()
            print("'What's going on here then?' The Don, suave as ever, saunters out of his Office")
            print()
            input("Continue ")
            print()
            print("'I found this one listening in on you, Boss' says Jimmy. Gleaming hatred and ambition in his eyes.")
            print()
            input("Continue ")
            print()
            print("'Is that so? Guess I'll have to take care of him myself' exclaims The Don. Pulling a piece from his pocket.")
            print()
            input("Continue ")
            print("Calm as ever, The Don turns the gun on you and with three quick trigger pulls puts you down")
            print()
            input("Continue ")
            print("'Ain't no room in The Firm for weaklings like you' he says, as he walks over your body and tells Jimmy to get on disposal duty.")
            mob_ending_2a()   
        else:
            print("Invalid choice. Please choose 1 or 2")

def mob_path_4():
    global morality_level, player_level, player_health
    addiction_func()
    print("A few more days go by without incident, and you find yourself settling into a routine.")
    print()
    input("Continue ")
    print()
    print("It feels good to have a purpose, a sense of security and belonging being part of The Firm.")
    print()
    input("Continue ")
    print()
    print("All this, however, is about to come crashing down.")
    print()
    input("Continue ")
    print()
    print("It's late, and once again you find yourself guarding one of The Firms many properties.")
    print()
    input("Three unmarked cars come flying down the street, stopping on the other side of the road")
    print()
    print("Two heavily armed goons spring out from each car, taking cover and opening fire at you.")
    print()
    input("Continue ")
    print()
    print("In the hail of bullets three of the goons are laid out, and the other guard on duty takes one to the chest.")
    print()
    input("Continue ")
    print("Panic sets in, and the remaining goons stops shooting.")
    print()
    input("Continue ")
    print()
    print("'Were not here for you, kid, we only want what you're guarding. Throw your gun down and we'll let you go, all quiet like.'")
    print()
    input("Continue ")
    print()
    while True:
        choice = input("You can 1. Continue firing, or 2. Run away like a coward ")
        print()
        if choice == "1":
            player_level += 2
            morality_level -= 100
            print("'Yeah nah. I'll take on all of you SOB's!' You cry")
            print()
            input("Continue ")
            print()
            print("You grab the fallen guards pistol, and continue firing off shots into the night")
            print()
            input("Continue ")
            print()
            print("You get lucky, and two of the goons go down one oafter the other.")
            print()
            input("Continue ")
            print()
            print("Seeing there's only one left, you round the car and finish the job. Pumping 2 into the chest, and a final one into the dome.")
            print()
            input("Continue ")
            print()
            print(f"Your level increased to {player_level} and your morality decreased to {morality_level}")
            mob_path_5()
        elif choice == "2":
            player_level -= 1
            morality_level += 50
            print("Warm liquid runs down your leg, and your whole body starts to shake.")
            print()
            input("Continue ")
            print()
            print("You throw your gun on the ground and run for your life, the goons taunting ringing in your ears.")
            print()
            input("Continue ")
            print()
            print(f"Your morality increased to {morality_level}")
            assassination_path()
        else:
            print("Invalid choice. Please choose 1 or 2")

def mob_path_5():
    global morality_level, player_level, player_health
    addiction_func()
    print("You've been a member of The Firm for some time now, gaining the trust and respect of your peers and The Don both.")
    print()
    input("Continue ")
    print()
    print("Tasks that would have seemed insurmountable beforehand, are now routine. The ability to lie and keep secrets is second nature to you.")
    print()
    input("Continue ")
    print()
    print("You have wholly commited yourself to this path. To this type of life, the good and the bad. Especially the ugly.")
    print()
    input("Continue ")
    print()
    print("One thing has remained constant throughout this whole ordeal however. Every choice and circumstance.")
    print()
    input("Continue ")
    print()
    print("'I'm always acting on someone elses orders' you think to yourself.")
    print()
    input("Continue ")
    print()
    print("Maybe it's time to make that next step, to become my own boss, but how?")
    print()
    input("Continue ")
    print("You think back to that one, fated night, where you overheard The Don")
    print()
    input("Continue ")
    print()
    print("'If I tell the others what I've heard, we can overthrow him, and cause a power vacuum in The Firm. Then I can swoop in and become the next Don'")
    print()
    input("Continue ")
    print()
    print("It's a risky move, and there's no guarnatee that the rest of The Firm either won't turn on you, or will choose someone else to lead them.")
    input("Continue ")
    print()
    while True:
        choice = input("You have two choices 1. Tell the rest of The Firm about The Don's double dealing, 2. Confront The Don yourself")
        print()
        if choice == "1" and player_health >= 20:
            player_level += 2
            morality_level += 100
            print("You spread rumours of The Don's crimes to rest of The Firm, sowing discord.")
            print()
            input("Continue ")
            print()
            print("Fighting erupts between Members, and battlelines start being drawn up.")
            print()
            input("Continue ")
            print()
            print(f"Your level increased to {player_level} and your morality increased to {morality_level}")
            mob_path_6()
        elif choice == "1" and player_health < 20:
            print()
            print("Your attempts to bad mouth The Don either aren't heard, or aren't taken seriously by the other members of The Firm.")
            print()
            input("Continue ")
            print()
            print("It seems that due to your crippling addiction, they won't take you seriously.")
            print()
            input("Continue ")
            print()
            assassination_path()
        elif choice == "2" and player_health >= 20:
            player_level += 2
            morality_level += 100
            print("You confront the Don in his office, telling him that you know all about his double dealings, cutting out The Firm in his own interests.")
            print()
            input("Continue ")
            print()
            print("'Well, I guess we got two choices then, don't we. I can cut you in and make you a Partner, or I can get you taken care of, if you catch my drift'")
            print()
            input("Continue ")
            print()
            print("Weighing up the options in your mind, you know that it's already set.")
            print()
            input("Continue ")
            print()
            print("'Fine, I'll take you up on your offer' you let him know. Heading out the door you both know that there can be only one true boss in this business.")
            print()
            input("Continue ")
            print()
            print("Two factions rise to power. The Loyalists on one side, led by The Don. And on the other side, are the Insurrectionists with you at the helm. It's time to go to war.")
            print()
            input("Continue ")
            print()
            print(f"Your level increased to {player_level} and your morality increased to {morality_level}")
            mob_path_6()
        elif choice == "2" and player_health <= 20:
            player_level += 2
            morality_level -= 100
            print("You find the Don in his office, an intimidating presence in their full glory. You tell him that you know all about his double dealings, cutting out The Firm in his own interests.")
            print()
            input("Continue ")
            print()
            print("The Don pours two glasses and hands you one. 'Now this is what's gonna happen. I'm gonna promote you to Capo, and you only answer to me from now on. But anyone gets any idea about what you just said to me, then it's lights out for you. Capische?'")
            print()
            input("Continue ")
            print()
            print("You take a long gulp of the bourbon, stifling a cough at the bitter taste. 'Looks like it'll take a little longer to get to the top' you tell yourslef as you head home. For now though, it may be time to enjoy your new-found power.")
            print()
            input("Continue ")
            print()
            print("'Fine, I'll take you up on your offer' you let him know. Heading out the door you both know that there can be only one true boss in this business.")
            print()
            input("Continue ")
            print(f"Your level increased to {player_level} and your morality increased to {morality_level}")
            assassination_path()
        else:
            print("Invalid choice. Please choose 1 or 2")   

def mob_path_6():
    global morality_level, player_level, player_health
    addiction_func()
    print()
    print("Two factions rise to power. The Loyalists on one side, led by The Don. And on the other side, are the Insurrectionists with you at the helm. It's time to go to war.")
    print()
    input("Continue ")
    print()
    print("It proves to be a long and bitter ordeal. Lives are lost on both sides, and there doesn't seem to be a clear winner in sight.")
    print()
    input("Continue ")
    print()
    print("A courier arrives with a signed letter, asking for a temporary ceasefire and a sit-down between you and The Don, to come to terms.")
    print()
    input("Continue ")
    print()
    print("'Surely this has got to be a setup?' You say to yourself. An obvious ploy to get you alone and finish you off. But this could also be just the opportunity you've been waiting for to end this once and for all.")
    print()
    input("Continue ")
    print()
    while True:
        choice = input("You have two choices 1. Go to the meet unarmed, as requested, or 2. Conceal a firearm")
        print()
        if choice == "1" and player_health >= 20:
            player_level += 10
            morality_level += 1000
            print()
            print("You rock up to the meeting alone, and unarmed. Whatever's coming you're going to face it as you always have, with your wits and brute strength.")
            print()
            input("Continue ")
            print()
            print("As expected, The Don is already there with his usual Lackies. A few faces less than previous, you have your own Insurrectionists to thank for that.")
            print()
            input("Continue ")
            print()
            print("Seeing you The Don sneers, 'Didn't think to bring anyone I see? Think you can take me all on your own, do ya? You've certainly grown a pair of brass ones, I'll give you that.'")
            print()
            input("Continue ")
            print()
            print("Motioning to a decanter of bourbon on the table next to you, The Don pours you both a few fingers, and you raise the glass to your lips.")
            print()
            input("Continue ")
            print()
            print("You drain the glass in one, smacking your lips in appreciation for the dark drink.")
            print()
            input("Continue ")
            print()
            print("Suddenly your vision starts swimming and the room becomes a blur of sound and smells. You recognise this sensation, it's the same as the Substance you've been taking all this time, except that the effects have been multiplied threefold.")
            print()
            input("Continue ")
            print()
            print("The Don throws back his shoulders and lets out a roucous laugh. 'I always knew you were a Junkie, and now your gonna die like the rat filth you are.'")
            print()
            input("Continue ")
            print()
            print("As casual as you like the Don pulls his piece from under his coat, inspecting and admiring the handiwork. All while the Substances effects slowly appear to overwhelm you.")
            print()
            input("Continue ")
            print()
            print("The Don's eyes widen with surprise as you lunge for the gun, overpowering him and turning the weapon on it's owner")
            print()
            input("Continue ")
            print()
            print("'Seems like I'm not as much of a Junkie as you thought I was' you say. Repeated exposure to the substance without taking too much has given you a natural immunity against the effects of a lethal dosage, allowing you to stay in control of your faculties.")
            print()
            input("Continue ")
            print()
            print("'It's time for a new ruler' you say to him, as you let off one singular shot to his heart, and put The Don down for good.")
            mob_ending_2b()
        elif choice == "1" and player_health < 20:
            player_level -= 1
            morality_level += 1000
            print("You come to the meeting flanked by some of your most trusted men, unarmed. You want to get this over and done with, your mind full of treachery and a hunger for a certain Substance once you get back.")
            print()
            input("Continue ")
            print()
            print("The Don welcomes you with his usual Lackies. A few faces less than previous, you have your own Insurrectionists to thank for that.")
            print()
            input("Continue ")
            print()
            print("Seeing you visibly agitated The Don asks you to sit at the other end of the table. A lone seat positioned opposite him, outside of arms reach from each other.")
            print()
            input("Continue ")
            print()
            print("Motioning to a decanter of bourbon on the table next to you, The Don pours you both a few fingers, and you raise the glass to your lips.")
            print()
            input("Continue ")
            print()
            print("You struggle to maintain a straight face and sink the liquid, the taste of the brown drink burning the back of your throat as it goes down.")
            print()
            input("Continue ")
            print()
            print("Suddenly your vision starts swimming and the room becomes a blur of sound and smells. You recognise this sensation, it's the same as the Substance you've been taking all this time, except that the effects have been multiplied threefold.")
            print()
            input("Continue ")
            print()
            print("The Don throws back his shoulders and lets out a roucous laugh. 'I always knew you were a Junkie, and now your gonna die like the rat filth you are.'")
            print()
            input("Continue ")
            print()
            print("As casual as you like the Don pulls his piece from under his coat, inspecting and admiring the handiwork. All while the Substances effects bring you to your knees.")
            print()
            input("Continue ")
            print()
            print("'I can't believe a Junkie like you though he could outsmart me. You're nothing. You've always been nothing, and you'll always be remembered as nothing.'")
            print()
            input("Continue ")
            print()
            print("The Don squeezes the trigger, finally putting an end to your pained existence. As the light fades from your eyes, his laughter is the last sound you hear.")
            mob_ending_2a()
        elif choice == "2" and player_health >= 20:
            player_level += 10
            morality_level -= 100
            print("You come to the meeting alone, concealing a gun. Life's never played you fair before, and you know that it's not going to continue now.")
            print()
            input("Continue ")
            print()
            print("As expected, The Don is already there with his usual Lackies. A few faces less than previous, you have your own Insurrectionists to thank for that.")
            print()
            input("Continue ")
            print()
            print("Seeing you The Don sneers, 'Didn't think to bring anyone I see? Think you can take me all on your own, do ya? You've certainly grown a pair of brass ones, I'll give you that.'")
            print()
            input("Continue ")
            print()
            print("Motioning to a decanter of bourbon on the table next to you, The Don pours you both a few fingers, and you raise the glass to your lips.")
            print()
            input("Continue ")
            print()
            print("You lock eyes with The Don and notice that he's started lowering his glass. Suspicions raised you throw your drink in his face and pull your piece")
            print()
            input("Continue ")
            print()
            print("'Rule Number One in this life, never come unprepared'. You squeeze the trigger and let him have it, finally putting down The Don for good.")
            print()
            input("Continue ")
            print()
            print("You turn to The Don's goons who bow their head in deference. If they can't respect you, they may as well fear you instead. 'Looks like I'm in charge now'")
            mob_ending_2b()
        elif choice == "2" and player_health < 20:
            player_level -= 1
            morality_level -= 500
            ("You come to the meeting flanked by some of your most trusted men, concealing a gun. You want to get this over and done with, your mind full of treachery and a hunger for a certain Substance once you get back.")
            print()
            input("Continue ")
            print()
            print("The Don welcomes you with his usual Lackies. A few faces less than previous, you have your own Insurrectionists to thank for that.")
            print()
            input("Continue ")
            print()
            print("Seeing you visibly agitated The Don asks you to sit at the other end of the table. A lone seat positioned opposite him, outside of arms reach from each other.")
            print()
            input("Continue ")
            print()
            print("Motioning to a decanter of bourbon on the table next to you, The Don pours you both a few fingers, and you raise the glass to your lips.")
            print()
            input("Continue ")
            print()
            print("You lock eyes with The Don and notice that he's started lowering his glass. Suspicions raised you attempt to throw your drink and pull your piece. However all of the Substance abuse you've put your body through has left you sluggish and slow.")
            print()
            input("Continue ")
            print()
            print("The Don is quicker on the draw and lets rip with his own, ornate iron, planting one straight in your chest.")
            print()
            input("Continue ")
            print()
            print("'I can't believe a Junkie like you though he could outsmart me. You're nothing. You've always been nothing, and you'll always be remembered as nothing.'")
            print()
            input("Continue ")
            print()
            print("The Dons' word echo in your brain as you fall to your knees. Thoughts swirling in your brain about what could have been.")
            mob_ending_2a()
        else:
            print("Invalid choice. Please choose 1 or 2") 

def assassination_path():
    while True:
        print()
        print("It's a cold dark night, and you find yourself walking home alone.")
        print()
        input("Continue ")
        print()
        print("These backstreets aren't safe, but you know you'll be fine. Besides, who'd be stupid enough to mess with you?")
        print()
        input("Continue ")
        print()
        print("Walking down the final alley before you get home, a shot rings out into the night")
        print()
        input("Continue ")
        print()
        print("You spin around to meeet your assailant head on, but it's too late.")
        print()
        input("Continue ")
        print()
        print("'Thought you could get away from us?'. The light coalesces on your assassins face, and you recognise them as the man in the grey suit, Jimmy.")
        print()
        input("Continue ")
        print()
        print("Your knees buckle as three shots ring out into the night. BANG. BANG. BANG.")
        print()
        input("Continue ")
        print()
        print("'No-one messes with the firm'. Footsteps recede into the darkness, leaving you cold and alone.")
        input("Continue ")
        print()
        while True:
            choice = input("Would you like to 1. Restart the game, and see what other ending you can achieve? or 2. Quit the game ")
            if choice == "1":
                restart_game()
                main()
            elif choice == "2":
                sys.exit()
            else:
                print("Invalid input. Choose 1. Restart the game or 2. Exit the game")   

def mob_ending_2a():
    global morality_level, player_level
    print("Congratulations you got to the end of the game!")
    print()
    input("Continue ")
    print()
    print("You may not have reached the lofty heights you aimed for, but how well did you manage to do?")
    print()
    input("Continue ")
    print()
    while True:
        if player_level >= 7 and morality_level <= 900:
            print("OLIGARCH - You prove that the best way to the top is by being a ruthless Corporate Dictator. Well done on seeing through your shady choices to the bitter end.")
            restart_or_quit()
        elif player_level >= 7 and morality_level >= 900:
            print("CEO - Sometimes the path to the top isn't just black and white. You operate in that moral grey area, doing just enough to ensure that the job gets done, and everyone profits.")
            restart_or_quit()
        elif 3 <= player_level < 7 and morality_level >= 900:
            print("MIDDLE MANAGER - You're never going to get far in life if you don't make a few hard choices, break a few eggs. You're rather averse to stepping on toes, that's obviouc. I hope you enjoy the 2.4 kids and the mortgage.")
            restart_or_quit()
        elif 3 <= player_level < 7 and morality_level < 900:
            print("PUPPET - How does it feel to always be the bridesmaid, and never the bride? Maybe next time it'll be worth taking a few risks and starting to live life in the fast lane, playing by your own rules rather than staying in somebody elses shadow.")
            restart_or_quit()
        else:
            print("PEASANT - I'm actually amazed you managed to mess up this badly. It's honestly quite impressive how much you must lack a spine.")
            restart_or_quit()

def mob_ending_2b():
    global morality_level
    print("Congratulations you got to the end of the game!")
    print()
    input("Continue ")
    print()
    print("You managed to overthrow The Don, and become the leader of The Firm. Lets see how well you did.")
    print()
    input("Continue ")
    print()
    while True:
        if morality_level >= 1500:
            print("KINGPIN - You take what you want with brute force. Everyone respects you, and wouldn't think twice about betraying that trust. They know that even if they did, you'll always be that one step ahead.")
            print()
            restart_or_quit()
        else:
            print("GANG LORD - You believe that respect is overrated, force and brutality are much more effective tools in your arsenal if you actually want to see things get done, and get done right. The people may fear you now, but what of the future? Enjoy this while you can.")
            print()
            restart_or_quit()

if __name__ == "__main__":
    main()