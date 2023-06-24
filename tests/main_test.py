"""testing main.py file functions"""

from src.main import MainProgram
import json
import os

class TestMain:
    main = MainProgram()

    def test_print_user_options(self, capfd):
        self.main.print_user_options()
        test_output, _ = capfd.readouterr()
        assert test_output == "('e' and hit enter to enter the exam editing menu)\n"\
                              "('s' and hit enter to enter the schedule editing menu)\n"\
                              "('q' and hit enter to quit py-study-planner)\n"
    
    def test_check_database_file(self):
        file_path = 'tests/main_db/main_test.json'
        if os.path.exists('tests/main_test.json'):
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Error: {e.filename} - {e.strerror}.")
        
        self.main.check_database_file(file_path)
        assert os.path.exists(file_path)
        with open(file_path, 'r', encoding='utf-8') as data_file:
            loaded = json.load(data_file)
        assert str(loaded) == '{}'

        





        

        

