"""main codebase for the py-study-planner project"""

#import libraries
import json
import os
import random

def random_number_gen(n):
    """generate a random number with a certain number of digits"""
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def print_user_options():
    """presents options for user in menu"""
    print("('a' and hit enter to add an exam that you are studying for)")
    print("('l' and hit enter to list exams that you are currently studying for)")
    print("('e' and hit enter to edit an exam that you are currently studying for)")
    print("('d' and hit enter to delete an exam that you are currently studying for)")
    print("('q' and hit enter to quit py-study-planner)")

def add_exam():
    """routine for adding user input on exam data to json"""
    exam_name = input("What is the name of the exam you'd like to add?\n")
    exam_date = input("What date is your exam? (use mm/dd/yyyy format)\n")
    resources = input("List any resources that you have available, separated by a space (e.g. 'textbook website flashcards' inputs 3 separate resources).\n")
    resources = resources.split(' ')
    resources_times = []
    for i, resource in enumerate(resources):
        if i>len(resources):
            break
        resource_time = input(f"How much time would you like to dedicate to the '{resource}' resource? Enter how many total minutes you want to spend on this resource from now until the exam.\n")
        resources_times.append(resource_time)
    resource_data = list(zip(resources, resources_times))
    exam_info = {'exam_name': exam_name, 'exam_date': exam_date, 'resource_data': resource_data}
    if os.path.exists('exam_data.json'): #if the json database exists then update
    # search ids in order to produce a new, unique id
        with open('exam_data.json',"r", encoding='utf-8') as exam_data_file:
            loaded = json.load(exam_data_file)
        while True:
            unique = True
            exam_id = random_number_gen(9)
            current_ids = []
            for key,value in loaded.items():
                if key=="exam_id":
                    current_ids.append(value)
                else:
                    pass
            for current_id in current_ids:
                if int(current_id)==int(exam_id):
                    unique=False
                else:
                    pass
            if unique is False:
                exam_id = random_number_gen(9)
            elif unique:
                exam_data = {f'{exam_id}':exam_info}
                print(exam_data)
                loaded.update(exam_data)
                print(loaded)
                with open('exam_data.json',"w", encoding='utf-8') as exam_data_file:
                    json.dump(loaded, exam_data_file)
                break
            else:
                print("There was a problem.")
    else: #if the json database doesn't exist then create it
        with open('exam_data.json',"w", encoding='utf-8') as exam_data_file:
            exam_id = random_number_gen(9)
            exam_data = {f'{exam_id}':exam_info}
            json.dump(exam_data, exam_data_file)

    return exam_data

def main():
    """run main function while constant "run" is True, allows user to navigate main menu or quit"""
    print("Welcome to the py-study-planner program.")
    print("What would you like to do? Here are your options:")
    print_user_options()
    run=True
    while run is True:
        usr_input_mm = input("")
        if usr_input_mm=="a":     # add exam into json database
            exam_data = add_exam()
            names = []
            for d in exam_data.values():
                names.append(d['exam_name'])
            print(f"{names[-1]} was added to the database (you can find the database under 'exam_data.json')! What would you like to do next?")
            print_user_options()
        elif usr_input_mm=="l":   # list all exams in json database
            print(usr_input_mm)
        elif usr_input_mm=="e":   # edit exam in json json database
            print(usr_input_mm)
        elif usr_input_mm=="d":   # delete exam in json database
            print(usr_input_mm)
        elif usr_input_mm=="q":   # quit py-study-planner program
            run=False
        else:                       # exception handling: repeat user options
            print("input invalid. your options are:")
            print_user_options()
    return run

if __name__=="__main__":
    main()
    