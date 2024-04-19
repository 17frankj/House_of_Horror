import time
from Paths import leftPath
from Part_1 import Part1, Part2
from InputValidator import yes_no_Loop, one_two_three_loop
# Final Project for Wrinting Machines, 1130 
# Author: Joshua Frank in collaberation with Open AI Chatgpt 3.5
# All text will be created by Gpt 3.5 and edited by myself for clarity

# opening message to player
print("""Welcome to House of Horror! Prepare yourself for a spine-chilling adventure into the unknown depths of terror.
    As you step into the eerie corridors of this mysterious house, your bravery will be put to the ultimate test. 
    Will you unravel the dark secrets hidden within its walls, or will you become another victim of its malevolent presence? 
    The choice is yours, but beware, for every decision you make will shape your fate in this gripping tale of horror. 
      """)

choice = input("Are you ready to face the horrors that await you in the House of Horror? Y or N? ")
choice = yes_no_Loop(choice)
if choice == 0:
      choice = input("You sure? Y or N?")
      choice = yes_no_Loop(choice)
      if choice == 1:
            print("GG loser")
            exit()
      
print(""" You wake up from a deep sleep.... 
      the dim light filtering through dusty windows reveals a room shrouded in darkness. 
      The air is heavy with the scent of decay, and the floorboards creak ominously beneath their feet. 
      A single flickering candle casts eerie shadows on the peeling wallpaper, revealing the outlines of long-forgotten furniture covered in tattered sheets.
      """)
time.sleep(10)
print(""" Your vision slowly adjusts to the gloom,
      and they find themselves in what appears to be a dilapidated bedroom. 
      The bed they've just awoken on is draped in moth-eaten linens, 
      and the mattress sags uncomfortably beneath them. Across the room, 
      a cracked mirror reflects their disheveled appearance, distorted by age and neglect.
      """)
time.sleep(8)
print("""
      A chill runs down your spine as you notice strange markings etched into the walls, 
      resembling arcane symbols long forgotten by the world. 
      The only door out of the room looms ominously before them, its warped wood bearing the scars of years of neglect.
      """)
time.sleep(5)
print("""
      Outside, the wind howls mournfully, carrying with it whispers that seem to echo through the halls of the decrepit house. 
      With a sense of growing unease, the player realizes that they are not alone in this forsaken place. 
      Something sinister lurks in the shadows, waiting for its next victim to stumble blindly into its grasp.
      """)
time.sleep(5)

# loop to check which place in the story they're in
story_state = 0
while(story_state < 5):

      if(story_state == 0):
            choice = input("You see in the dime light ahead, two paths, do you choose the left path? Y or N? ")
            choice = yes_no_Loop(choice)
            story_state = Part1(choice)
      if(story_state == 1):
            choice = input("""
                  You now stand before three imposing doors, each one seemingly more ominous than the last. 
                           
                        Do you enter 1, 2, or 3? 
                              """)
            choice = one_two_three_loop(choice)
            story_state = Part2(choice)
            # bugg testing
            #story_state = 5
      if story_state == 5:
            print("Game over! ")
            choice = input("Try again?? Y or N? ")
            choice = yes_no_Loop(choice)
            if(choice == 1):
                  story_state = 0
            elif(choice == 0):
                  story_state = 8
if(story_state == 6):
      print("Thank you for playing my game! ")
      time.sleep(2)
      print("this was a parntership with myself and chat GPT 3.5")
      time.sleep(2)
      print("I hope to build on this in the future, but as of now I'm happy wiht this as my starting point!")