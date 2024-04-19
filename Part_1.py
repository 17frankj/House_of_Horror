from Paths import leftPath, rightPath
from InputValidator import yes_no_Loop
from Doors import door1, door2, door3

def Part1(choice):
        if choice == 1:
                # go to method for left path
                result = leftPath()
        elif choice == 0:
                choice = input("Do you choose the right path? Y or N? ")
                choice = yes_no_Loop(choice)
                if(choice == 0):
                        # take player back to origanl choice
                        return 0
                # go to method for right path
                result = rightPath()
        if result == -1:
                return 0

        return result

def Part2(choice):
        if choice == 1:
                # go to method for first door
                result = door1(choice)
        if choice == 2:
                # go to method for second door
                result = door2(choice)
        if choice == 3:
                # go to method for third door
                result = door3(choice)
        
        return result