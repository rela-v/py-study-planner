"""testing main.py file functions"""

from src.main import MainProgram
import json
import os

class TestMain:
    main = MainProgram()
    file_path = 'exam_data.json'

    def test_print_user_options(self, capfd):
        self.main.print_user_options()
        test_output, _ = capfd.readouterr()
        assert test_output == "('e' and hit enter to enter the exam editing menu)\n"\
                              "('s' and hit enter to enter the schedule editing menu)\n"\
                              "('q' and hit enter to quit py-study-planner)\n"

        

        

