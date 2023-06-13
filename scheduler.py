"""module for generating study schedule in the py-study-planner project"""

def print_user_options():
    """print user options for the scheduling suite in menu"""
    print("('g' and hit enter to generate a schedule)")
    print("('s' and hit enter to display your schedule)")
    print("('a' and hit enter to display your day's agenda)")
    print("('d' and hit enter to delete an exam study schedule)")
    print("('q' and hit enter to quit the scheduling suite)")

def scheduler_main():
    """run main function while constant "run" is True, allows user to navigate main menu or quit"""
    print("Welcome to the scheduling suite.")
    print("What would you like to do? Here are your options:")
    print_user_options()
    run=True
    while run is True:
        usr_input_mm = input("")
        if usr_input_mm=="g":     # add exam into json database
            ...
        elif usr_input_mm=="s":     # add exam into json database
            ...
        elif usr_input_mm=="a":     # add exam into json database
            ...
        elif usr_input_mm=="d":     # add exam into json database
            ...
        elif usr_input_mm=="q":   # quit py-study-planner program
            run=False
        else:                       # exception handling: repeat user options
            print("input invalid. your options are:")
            print_user_options()
    return run