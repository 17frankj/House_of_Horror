import time
from InputValidator import yes_no_Loop, one_two_three_loop

def door1(choice):
    # only displays this message the first time you enter this room
    if(choice == 1):
        print("""
        Summoning your courage, you push open the door and step into the darkness beyond. 
            As the door creaks shut behind you, you find yourself in a narrow corridor, 
            its walls lined with faded portraits of grim-faced individuals whose eyes seem to follow your every move.
            """)
        time.sleep(5)
        choice = input("""
        The air grows colder as you venture deeper into the corridor, 
            the silence broken only by the sound of your own footsteps echoing off the walls. 
            You come to a fork in the corridor, faced with a choice: 
            continue straight ahead, or turn left into an even darker passageway. 
            Straight: Y or left: N?
            """)
    # choice will be 0 if they have entered before
    elif(choice == 0):
        choice = input("Wanna go straight now? Y or N ")
    elif(choice == 5):
        print("-----------------------------------------------")
        return choice
    choice = yes_no_Loop(choice)
    # using recurition to repeat doors
    if(choice == 0):
        choice = left()
        return door1(choice)
    result = straight(choice)
    return result

def door2(choice):  
    print("Your gaze falls upon the second door, its surface adorned with intricate carvings that seem to writhe and twist in the dim light.")
    time.sleep(5)
    print("""
    Taking a deep breath, you grasp the handle and push open the door, 
            revealing a room bathed in an eerie green glow. 
            The air is heavy with the scent of decay, and a thick mist hangs in the air, obscuring your vision and sending a chill down your spine.
            """)
    time.sleep(5)
    print("""
    As you step into the room, you are greeted by the sight of a twisted, 
            gnarled tree growing from the center of the floor. Its branches stretch outwards like skeletal fingers, casting long shadows that dance across the walls.
            """)
    time.sleep(5)
    print("""
    In the dim light, you can just make out the shapes of strange, pulsating pods hanging from the branches, 
            their surfaces slick with a sickly sheen. A sense of unease washes over you as you realize that you are not alone in this strange, otherworldly chamber.
            """)
    time.sleep(5)
    print("""
    Before you can react, the pods begin to quiver and shake, and with a sickening squelch, 
            they burst open, unleashing a swarm of writhing, 
            insect-like creatures that skitter across the floor towards you, hungry for blood...
            """)
    choice = input("Do you run (1), Hide(2), or Attack!(3)")
    choice = one_two_three_loop(choice)
    if(choice == 1):
        return choice
    elif(choice == 2):
        print("""
        Panicked, you dive behind the nearest piece of furniture, 
                your heart pounding in your chest as the horde of insect-like creatures swarms into the room. 
                Desperation grips you as you huddle in the darkness, praying that they won't find you.
                """)
        time.sleep(4)
        print("""
        The creatures overwhelm you, their chittering cries echoing in your ears as they tear into your flesh with merciless efficiency. 
                Darkness closes in around you as your vision blurs, and with one final, agonized gasp, 
                you succumb to the swarm, your fate sealed within the House of Horror...
                """)
        return 5
    elif(choice == 3):
        print("""
        With a primal scream, you charge at the oncoming swarm of insect-like creatures, 
                swinging wildly in a desperate attempt to fend them off. Your blows land true, 
                crushing several of the creatures beneath your makeshift weapon, but still they keep coming, their numbers seemingly endless.
                """)
        time.sleep(4)
        print("""
        In your final moments, you catch a fleeting glimpse of the twisted tree at the center of the room, 
                its branches writhing with malevolent intent. And then, darkness claims you, 
                your screams lost amidst the chittering of the creatures as you meet your gruesome end within the House of Horror...
                """)
        return 5
def door3(choice):
       print("""
        With a trembling hand, you reach out and grasp the handle, pushing it open to reveal a narrow passageway bathed in a soft, golden light.
             """)
       time.sleep(5)
       print("""
        A sense of relief washes over you as you step into the warmth of the illuminated corridor, 
             the oppressive darkness of the house receding behind you. The air is filled with the faint scent of fresh flowers, 
             and a gentle breeze carries the sound of distant birdsong.
             """)
       time.sleep(5)
       print("""
        In the distance, you catch sight of a flickering light, beckoning you forward like a beacon in the night. 
             With newfound hope in your heart, you quicken your pace, eager to leave the horrors of the House of Horror behind you.
             """)
       time.sleep(5)
       print("""
        As you draw closer to the light, you realize that it emanates from a doorway at the end of the corridor, 
             its threshold bathed in a soft, inviting glow. With each step, the warmth of the light envelops you, 
             filling you with a sense of peace and tranquility.
             """)
       choice = input("Do you enter? Y or N ")
       choice = yes_no_Loop(choice)
       if(choice == 1):
           return choice
       elif(choice == 0):
           print("""
            Your cowardess angers the house...
                 Thunderous noises arrize all around you, the walls begin to shake,
                 Everything hits you at once, flashes of a nightmare consume then...
                 """)
           time.sleep(5)
           print("""
            Your eyes squint open as you look up to a familiar ceiling.. 
                 You hear blaring through your door "School Time Kiddo!"
                 """)
           return 6
           

def straight(choice):
    if(choice == 1):
        print("""
        Taking a deep breath to steady your nerves, you choose to continue straight ahead, 
            forging deeper into the heart of the house. The corridor stretches out before you, 
            seemingly endless, its walls adorned with ancient tapestries depicting scenes of unspeakable horror.
            """)
        time.sleep(5)
        print("""
        With each step, the air grows heavier, weighed down by the oppressive atmosphere of the House of Horror. 
            Shadows dance and flicker along the walls, playing tricks on your senses as you navigate the labyrinthine passageways.
            """)
        time.sleep(5)
        print("""
        Suddenly, you come to a branching path, where the corridor splits off in two directions. 
            To your left, a staircase ascends into darkness, while to your right, a doorway beckons, its threshold shrouded in shadow.
            """)
    choice = input("Left: Y or Right: N")
    choice = yes_no_Loop(choice)
    if(choice == 0):
        choice = 1
        return door1(choice)
    elif(choice == 1):
        return int(choice)
    

def left():
    print("""
    You opt to turn left, your footsteps echoing ominously in the narrow passageway as you follow its winding path deeper into the darkness. 
          The air grows thick with a sense of foreboding, and a chill creeps down your spine as you press on, driven by a mixture of curiosity and fear.
          """)
    time.sleep(5)
    print("""
    After what feels like an eternity of twisting corridors and dead ends, 
          you come to a sudden stop as you reach a solid wall blocking your path. 
          Confusion clouds your mind as you realize you've stumbled into a dead end, the darkness pressing in around you like a suffocating shroud.
          """)
    time.sleep(5)
    print("""
    Panic begins to rise within you as you frantically search for a way out, your hands groping blindly at the cold, 
          unforgiving stone of the walls. But no matter how hard you try, there is no escape from this nightmarish maze, 
          and the realization sinks in that you are trapped in this forsaken corner of the House of Horror...
        """)
    choice = input("Turn back? Y or N ")
    choice = yes_no_Loop(choice)
    if(choice == 1):
        return 0
    elif(choice == 0):
        print("""
        Darkness consumes your being, You hear the whispery voice shout,
            A feast awaits!
            """)
        return int(5)
