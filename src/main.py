"""code execution main menu file"""

#import modules
from scheduler import scheduler_main
from exam import exam_main
from exam import random_number_gen
import os
def print_user_options():
    """presents options for user in menu"""
    print("('e' and hit enter to enter the exam editing menu)")
    print("('s' and hit enter to enter the schedule editing menu)")
    print("('q' and hit enter to quit py-study-planner)")

def mm_main():
    """run main function while constant "run" is True, allows user to navigate main menu or quit"""
    print("Welcome to py-study-planner.")
    print("What would you like to do? Here are your options:")
    print_user_options()
    run=True
    
    if not os.path.exists('exam_data.json'): #If JSON database doesn't exist then add the database
        open('exam_data.json',"w", encoding='utf-8')

    while run is True:
        usr_input_mm = input("")
        if usr_input_mm=="e":     # generate schedule for exam
            exam_main()
            print("Welcome back from exam editing! What next?")
            print_user_options()
        elif usr_input_mm=="s":     # display schedules for exams
            scheduler_main()
            print("Welcome back from schedule editing! What next?")
            print_user_options()
        elif usr_input_mm=="q":   # quit py-study-planner program
            run=False
        else:                       # exception handling: repeat user options
            print("input invalid. your options are:")
            print_user_options()
    return run

if __name__=="__main__":
    mm_main()
