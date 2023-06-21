"""module for editing exams in the py-study-planner project"""

# import libraries
import json
import os


def print_user_options():
    """presents options for user in menu"""
    print("('a' and hit enter to add an exam that you are studying for)")
    print("('l' and hit enter to list exams that you are currently studying for)")
    print("('e' and hit enter to edit an exam that you are currently studying for)")
    print("('d' and hit enter to delete an exam that you are currently studying for)")
    print("('q' and hit enter to quit the exam editing suite)")


def get_resource_data():
    """get data for resources according to user input"""
    resources = input(
        "List resources, separated by a space "
        "(e.g. 'textbook website flashcards' inputs 3 separate resources).\n"
    )
    resources = resources.split(" ")
    resources_times = []
    for i, resource in enumerate(resources):
        resource_time = input(
            "How much time would you like to dedicate "
            f"to the '{resource}' resource? Enter how many total "
            "minutes you want to spend on this resource from now "
            "until the exam.\n"
        )
        resources_times.append(resource_time)
    resource_data = list(zip(resources, resources_times))
    return resource_data


def add_exam():
    """routine for adding user input on exam data to json"""
    exam_name = input("What is the name of the exam you'd like to add?\n")
    with open("exam_data.json", "r", encoding="utf-8") as exam_data_file:
        loaded = json.load(exam_data_file)
    if (exam_name in loaded.keys()): # If the new name is already in use then do nothing
        return "Exam name is already in use"
    exam_date = input("What date is your exam? (use mm/dd/yyyy format)\n")
    resource_data = get_resource_data()

    exam_info = {
        "exam_date": exam_date,
        "resource_data": resource_data,
    }  
    exam_data = {f"{exam_name}": exam_info}
    print(exam_data)
    loaded.update(exam_data)
    print(loaded)
    with open("exam_data.json", "w", encoding="utf-8") as exam_data_file:
        json.dump(loaded, exam_data_file)
    return exam_data


def list_exam():
    """routine for listing all added exams"""
    with open("exam_data.json", "r", encoding="utf-8") as exam_data_file:
        loaded = json.load(exam_data_file)
        for key, v in loaded.items():
            print("exam_name: " + key)
            for k, value in v.items():
                print(f"{k}: {value}")


def edit_exam(exam_name):
    """routine for editing user input on exam data to json"""
    with open("exam_data.json", "r", encoding="utf-8") as exam_data_file:
        loaded = json.load(exam_data_file)
    if exam_name in loaded.keys():
        change_flags = input(
            f"Type the things you wanted to change about your {exam_name} "
            "exam separated by a space: type...\n"
            "('n' to edit the name of the exam)\n"
            "('d' to edit the date of the exam)\n"
            "('r' to edit the resources of the exam)\n"
        )
        change_flags = change_flags.split(" ")
        if "n" in change_flags:
            
            exam_name_new = input(
                f"Please input the new name for your {exam_name} " "exam\n"
            )
            loaded[exam_name_new] = loaded.pop(exam_name)
            exam_name = exam_name_new
        if "d" in change_flags:
            loaded[exam_name]["exam_date"] = input(
                f"Please input the new date for your {exam_name} "
                "exam in 'mm/dd/yyyy' format\n"
            )
        if "r" in change_flags:
            loaded[exam_name]["resource_data"] = get_resource_data()
        with open("exam_data.json", "w", encoding="utf-8") as exam_data_file:
            json.dump(loaded, exam_data_file)
        return True
    return False


def del_exam():
    """routine for editing user input on exam data to json"""
    list_exam()
    exam_name = input("Listed exams! Type the name of the one you'd like to delete.\n")
    with open("exam_data.json", "r", encoding="utf-8") as exam_data_file:
        loaded = json.load(exam_data_file)
    print(f"Removing the {exam_name} from the database...")
    del loaded[exam_name]
    with open("exam_data.json", "w", encoding="utf-8") as exam_data_file:
        json.dump(loaded, exam_data_file)
    print("Done! What next?")
    print_user_options()


def exam_main():
    """run main function while constant "run" is True, allows user to navigate main menu or quit"""
    print("Welcome to the exam-editing suite.")
    print("What would you like to do? Here are your options:")
    print_user_options()
    run = True
    while run is True:
        usr_input_mm = input("")
        if usr_input_mm == "a":  # add exam into json database
            exam_data = add_exam()
            new_name = list(exam_data.keys())[-1]
            print(
                f"{new_name} was added to the database "
                "(you can find the database under 'exam_data.json')! "
                "What would you like to do next?"
            )
            print_user_options()
        elif usr_input_mm == "l":  # list all exams in json database
            list_exam()
            print("Exam data printed! What next?")
            print_user_options()
        elif usr_input_mm == "e":  # edit exam in json json database
            exam_to_edit = input("What exam would you like to edit?\n")
            exam_found = edit_exam(exam_to_edit)
            if exam_found:
                print(
                    f"{exam_to_edit} was changed in the database! "
                    "(you can find the database under 'exam_data.json')! "
                    "What would you like to do next?"
                )
                print_user_options()
            else:
                print(
                    f"{exam_to_edit} was not found. " "What would you like to do next?"
                )
                print_user_options()
        elif usr_input_mm == "d":  # delete exam in json database
            del_exam()
        elif usr_input_mm == "q":  # quit py-study-planner program
            run = False
        else:  # exception handling: repeat user options
            print("input invalid. your options are:")
            print_user_options()
    return run


if __name__ == "__main__":
    exam_main()
