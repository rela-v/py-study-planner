"""module for generating study schedule in the py-study-planner project"""

#import modules
import json
import datetime
import os
import math
from operator import itemgetter
import pandas as pd
import numpy as np

class ScheduleManager:
    def __init__(self, db_file='exam_data.json'):
        self.db_file = db_file

    def print_user_options(self):
        """print user options for the scheduling suite in menu"""
        print("('s' and hit enter to display your schedule)")
        print("('a' and hit enter to display your day's agenda)")
        print("('q' and hit enter to quit the scheduling suite)")

    def gen_tasks(self, exam_name):
        """generate a list of tuples with task names and associated times"""
        with open('exam_data.json',"r", encoding='utf-8') as exam_data_file:
            loaded = json.load(exam_data_file)
        resource_data = loaded[exam_name]['resource_data']
        today = datetime.datetime.today().date()
        date_data = loaded[exam_name]['exam_date']
        date_data = datetime.datetime.strptime(date_data, '%m/%d/%Y').date()
        t_remaining = (date_data-today).days
        resource_names = [tup[0] for tup in resource_data]
        resource_times = [int(tup[1])/t_remaining for tup in resource_data]
        tasks = list(zip(resource_names,resource_times))
        return tasks, t_remaining

    def view_schedule(self):
        """generate a study schedule for a given exam"""    
        exam_name = input("What exam would you like to generate a schedule for?\n")
        tasks = self.gen_tasks(exam_name)
        schedule = {}
        td = datetime.datetime.today()
        tdmin = datetime.timedelta(minutes=(td.minute))
        def convert_to_timeform(time):
            """convert to preferred %m/%d/%Y %H:%M time format"""
            return datetime.datetime.strftime((time),'%m/%d/%Y %H:%M')
        for i in range(((24*tasks[1])-int(td.hour))-1):
            raw_time = td-tdmin+datetime.timedelta(hours=i+1)
            schedule[convert_to_timeform(raw_time)] = [np.nan]
        def find_time(n):
            """find first instance of window of empty values in dict"""
            free_in_a_row = 0
            for index, date in enumerate(schedule):     
                if (np.isnan(schedule[date])):
                    free_in_a_row += 1
                else:
                    free_in_a_row = 0
                if (free_in_a_row == n):
                    return index-n+1
                
            return np.nan
        schedule = pd.DataFrame(schedule).T
        print(schedule)
        return True

    def view_agenda(self):
        """view an agenda for a given day"""
        ...

    def del_schedule(self):
        """view an agenda for a given day"""
        ...

    def scheduler_main(self):
        """run main function while constant "run" is True, allows user to navigate main menu or quit"""
        print("Welcome to the scheduling suite.")
        print("What would you like to do? Here are your options:")
        run=True
        while run:
            self.print_user_options()
            usr_input_mm = input("")
            if usr_input_mm=="s":     # display schedules for exams
                self.view_schedule()
                print("schedule viewed! What next?")
            elif usr_input_mm=="a":     # view day agenda
                self.view_agenda()
                print("agenda viewed! What next?")
            elif usr_input_mm=="q":   # quit py-study-planner program
                run=False
            else:                       # exception handling: repeat user options
                print("input invalid. your options are:")

if __name__=="__main__":
    scheduleMgr = ScheduleManager()
    scheduleMgr.scheduler_main()
