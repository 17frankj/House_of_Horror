import time
from InputValidator import yes_no_Loop

def leftPath():
    
    print("""
    Your footsteps echo hollowly as they venture down the narrow hallway, 
          the dim light casting long, 
          twisting shadows that seem to dance malevolently along the cracked walls. 
          The air grows colder with each step, sending shivers down their spine.
          """)
    time.sleep(5)
    print("""
    As you approach a corner, 
          a faint scratching sound echoes from the darkness ahead, 
          accompanied by the soft rustle of movement. Their heart pounds in their chest as they hesitate, 
          gripped by a sudden sense of dread. 

          """)
    time.sleep(5)
    choice = input("Do you continue forward, risking what may lie beyond, or retreat back to the relative safety of the room they woke in? Y or N ")
    choice = yes_no_Loop(choice)
    if(choice == 0):
        # take player back to origanl choice
        print("you cower away, back to the room you came from...")
        return -1
    
    #continue with path

    print("""
    With a shaky breath, the player inches closer to the corner, 
          straining their senses for any sign of what awaits them. 
          Shadows seem to coalesce into sinister shapes, and the scratching grows louder, more insistent. 
          Their pulse quickens as they steel themselves to peer around the corner, bracing for whatever horrors may lurk just out of sight...
          """)
    
    time.sleep(5)
    print("""
      As you cautiously rounds the corner, 
          you are met with a sudden gust of icy wind that extinguishes their only source of light, 
          plunging you into utter darkness. Panic grips your chest as you fumble blindly for a way out, 
          but before you can react, something cold and clammy wraps around your ankle, pulling you down with a force you cannot resist...
          """)
    
    time.sleep(5)
    print("""
      With a gasp, 
          you finds yourself falling into a hidden pit concealed beneath the floorboards, 
          landing with a bone-jarring thud at the bottom. As you struggle to regain their bearings, 
          you realize with growing horror that the pit is filled with sharp, jagged spikes, glinting ominously in the dim light.
          """)
    
    time.sleep(5)
    print("""
      Despite your desperate attempts to climb out, 
          you're impaled by the cruel spikes, 
          your vision fading as the darkness claims you. 
          Yourr last thoughts are of the sinister presence that lurked in the shadows, 
          waiting patiently to claim its next victim in the House of Horror...
          """)
    return 5

def rightPath():
      print("""
      As You cautiously proceeds down the hallway, 
            you come to a weathered wooden door slightly ajar. 
            Pushing it open, you step into a room bathed in an eerie blue glow, 
            emanating from a series of flickering candles scattered around the perimeter.")
            """)
      time.sleep(5)
      print("""
      The air is thick with the scent of incense, 
            mingling with the musty odor of old books stacked haphazardly on shelves lining the walls. 
            Strange symbols and arcane sigils adorn the floor, drawn in chalk and pulsating softly with an otherworldly energy.
            """)
      time.sleep(5)
      print("""
      In the center of the room stands a pedestal, 
            upon which rests a worn tome bound in cracked leather. 
            Its pages seem to shimmer with hidden knowledge, beckoning you closer with an irresistible allure.
            """)
      time.sleep(5)
      print("""
      As you approach, you feel a tingle of anticipation run down your spine, 
            sensing that you have stumbled upon something of great importance within the House of Horror. 
            With trembling hands, you reach out to grasp the tome, ready to uncover the secrets that lie within...
            """)
      choice = input("Do you grab it? Y or N ")
      choice = yes_no_Loop(choice)
      if(choice == 0):
            # take player back to origanl choice
            print("You drop it, and run back, coward!...")
            return -1
      
      time.sleep(5)
      print("""
      As your fingers close around the weathered tome, 
            a surge of energy courses through your veins, sending sparks dancing along your skin. 
            The room suddenly grows still, the very air vibrating with an ancient power.
            """)
      time.sleep(5)
      print("""
      With a whispered incantation, the tome springs to life in your hands, 
            its pages flipping open of your own accord to reveal cryptic symbols and 
            forbidden knowledge written in a language long forgotten by mortals. 
            As your eyes scan the arcane text, 
            you feel a profound sense of understanding wash over you, 
            as if the secrets of the universe are laid bare before your very eyes.
            """)
      time.sleep(5)
      print("""
      But with understanding comes a price. 
            Your senses a presence stirring in the shadows, 
            drawn forth by the unlocking of the tome's secrets. 
            Eyes blazing with malevolent intent, a dark figure materializes before you, its form shifting and twisting like smoke.      
            """)
      time.sleep(5)
      print("""
      With a voice that echoes with the weight of centuries, 
            the figure issues a chilling warning: 
            "You have delved too deep into that which was not meant to be known. Prepare yourself, for the true horrors of this house await."
            """)
      time.sleep(5)
      print("""
      And with that ominous proclamation, the figure fades back into the darkness, 
            leaving you alone to face the terrifying challenges that lie ahead...
            """)
      return 1