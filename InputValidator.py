
def validation(response):
        # check if response is yes or no
        if response.strip().casefold() == "Y".casefold():
            return 1
        elif response.strip().casefold() == "N".casefold():
            return 0
        else:
            return -1

# validation for any while loops for yes or no
def yes_no_Loop(string):
    val = -1
    while val == -1:
        val = validation(string)
        if val == 1:
            choice = val
            return choice
        elif val == 0:
            choice = val
            return choice
        else:
            string = input("Please enter 'Y' or 'N': ")  # Ask for input again if it's not valid

def one_two_three_loop(choice):
    try:
        choice = int(choice)
        if choice not in [1, 2, 3]:
            choice = int(input("Please enter 1, 2, or 3: "))
            return one_two_three_loop(choice)
        else:
            return choice
    except ValueError:
        choice = int(input("Please enter a valid integer: "))
        return one_two_three_loop(choice)
    

