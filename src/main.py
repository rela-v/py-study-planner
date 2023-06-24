"""code execution main menu file"""

#import modules
from scheduler import ScheduleManager
from exam import ExamManager
import os
import json

class MainProgram:
    def __init__(self):
        self.examMgr = ExamManager()
        self.scheduleMgr = ScheduleManager()

    def print_user_options(self):
        """presents options for user in menu"""
        print("('e' and hit enter to enter the exam editing menu)")
        print("('s' and hit enter to enter the schedule editing menu)")
        print("('q' and hit enter to quit py-study-planner)")

    def check_database_file(self, file_name='exam_data.json'):
        if not os.path.exists(file_name): #If JSON database doesn't exist then add the database
            with open(file_name,"w", encoding='utf-8') as exam_data_file:
                json.dump({}, exam_data_file)


    def mm_main(self):
        """run main function while constant "run" is True, allows user to navigate main menu or quit"""
        print("Welcome to py-study-planner.")
        print("What would you like to do? Here are your options:")
        run=True
        
        self.check_database_file('exam_data.json')
        
        while run:
            self.print_user_options()
            usr_input_mm = input("")
            if usr_input_mm=="e":     # generate schedule for exam
                self.examMgr.exam_main()
                print("Welcome back from exam editing! What next?")
            elif usr_input_mm=="s":     # display schedules for exams
                self.scheduleMgr.scheduler_main()
                print("Welcome back from schedule editing! What next?")
            elif usr_input_mm=="q":   # quit py-study-planner program
                run=False
            else:                       # exception handling: repeat user options
                print("input invalid. your options are:")
                

if __name__=="__main__":
    mainloop = MainProgram()
    mainloop.mm_main()
