def int_check():
    """Checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("what is a game goal? "))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine starts here
game_goal = int_check()
print(game_goal)
