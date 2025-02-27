error = "Please enter an integer more than / equal to 13."

while True:
    try:
        game_goal = int(input("what is a game goal? "))

        if game_goal < 13:
            print(error)
        else:
            break


    except ValueError:
        print(error)
