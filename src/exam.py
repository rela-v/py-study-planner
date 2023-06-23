"""module for editing exams in the py-study-planner project"""

# import libraries
import json

class ExamManager:
    def __init__(self, db_file='exam_data.json'):
        self.db_file = db_file

    def print_user_options(self):
        """presents options for user in menu"""
        print("('a' and hit enter to add an exam that you are studying for)")
        print("('l' and hit enter to list exams that you are currently studying for)")
        print("('e' and hit enter to edit an exam that you are currently studying for)")
        print("('d' and hit enter to delete an exam that you are currently studying for)")
        print("('q' and hit enter to quit the exam editing suite)")


    def get_resource_data(self):
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

    def add_exam_input(self):
        """routine for adding user input on exam data to json"""
        exam_name = input("What is the name of the exam you'd like to add?\n")
        exam_date = input("What date is your exam? (use mm/dd/yyyy format)\n")
        resource_data = self.get_resource_data()

        exam_info = {
            "exam_date": exam_date,
            "resource_data": resource_data,
        }  

        exam_data = {f"{exam_name}": exam_info}
        
        return exam_data


    def add_exam(self, data):
        """routine for adding user input on exam data to json"""
        exam_data = data

        with open(self.db_file, "r", encoding="utf-8") as exam_data_file:
            loaded = json.load(exam_data_file)
        if (list(data.keys())[0] in loaded): # If the new name is already in use then do nothing
            return "Exam name is already in use"
        print(exam_data)
        loaded.update(exam_data)
        print(loaded)
        with open(self.db_file, "w", encoding="utf-8") as exam_data_file:
            json.dump(loaded, exam_data_file)
        return 


    def list_exam(self):
        """routine for listing all added exams"""
        with open(self.db_file, "r", encoding="utf-8") as exam_data_file:
            loaded = json.load(exam_data_file)
            for key, v in loaded.items():
                print("exam_name: " + key)
                for k, value in v.items():
                    print(f"{k}: {value}")


    def edit_exam(self, exam_name, command, new_data):
        """routine for editing user input on exam data to json"""
        with open(self.db_file, "r", encoding="utf-8") as exam_data_file:
            loaded = json.load(exam_data_file)
        if exam_name in loaded:
            change_flags = command
            if "n" in change_flags:        
                loaded[new_data] = loaded.pop(exam_name)
                exam_name = new_data
            if "d" in change_flags:
                loaded[exam_name]["exam_date"] = new_data
            if "r" in change_flags:
                loaded[exam_name]["resource_data"] = new_data
            with open(self.db_file, "w", encoding="utf-8") as exam_data_file:
                json.dump(loaded, exam_data_file)
            return True
        return False


    def del_exam(self):
        """routine for editing user input on exam data to json"""
        self.list_exam()
        exam_name = input("Listed exams! Type the name of the one you'd like to delete.\n")
        with open(self.db_file, "r", encoding="utf-8") as exam_data_file:
            loaded = json.load(exam_data_file)
        print(f"Removing the {exam_name} from the database...")
        del loaded[exam_name]
        with open(self.db_file, "w", encoding="utf-8") as exam_data_file:
            json.dump(loaded, exam_data_file)
        print("Done! What next?")


    def exam_main(self):
        """run main function while constant "run" is True, allows user to navigate main menu or quit"""
        print("Welcome to the exam-editing suite.")
        print("What would you like to do? Here are your options:")
        
        run = True
        while run is True:
            self.print_user_options()
            usr_input_mm = input("")
            if usr_input_mm == "a":  # add exam into json database
                exam_data = self.add_exam_input()
                added_exam = self.add_exam(exam_data)
                new_name = list(added_exam.keys())[-1]
                print(
                    f"{new_name} was added to the database "
                    "(you can find the database under 'exam_data.json')! "
                    "What would you like to do next?"
                )
            elif usr_input_mm == "l":  # list all exams in json database
                self.list_exam()
                print("Exam data printed! What next?")
            elif usr_input_mm == "e":  # edit exam in json json database
                exam_to_edit = input("What exam would you like to edit?\n")
                change_flags = input(f"Type the things you wanted to change about your {exam_to_edit}\n" \
                                "('n' to edit the name of the exam)\n"\
                                "('d' to edit the date of the exam)\n"\
                                "('r' to edit the resources of the exam)\n")
                exam_found = False
                if "n" in change_flags:
                    new_data = input(f"Please input the new name for your {exam_to_edit} "\
                                                    "exam\n")
                    exam_found = self.edit_exam(exam_to_edit, change_flags, new_data)

                if "d" in change_flags:
                    new_data = input(f"Please input the new date for your {exam_to_edit} "\
                                                    "exam in 'mm/dd/yyyy' format\n")
                    exam_found = self.edit_exam(exam_to_edit, change_flags, new_data)
                if "r" in change_flags:
                    new_data = self.get_resource_data()
                    exam_found = self.edit_exam(exam_to_edit, change_flags, new_data)


                if exam_found:
                    print(f"{exam_to_edit} was changed in the database! "\
                        "(you can find the database under 'exam_data.json')! "\
                    )
                else:
                    print(
                        f"{exam_to_edit} was not found. " "What would you like to do next?"
                    )

                
            elif usr_input_mm == "d":  # delete exam in json database
                self.del_exam()
            elif usr_input_mm == "q":  # quit py-study-planner program
                run = False
            else:  # exception handling: repeat user options
                print("input invalid. your options are:")
        return run


if __name__ == "__main__":
    examMgr = ExamManager()
    examMgr.exam_main()
