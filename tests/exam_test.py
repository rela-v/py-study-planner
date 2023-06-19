"""testing exam.py file functions"""

from src.exam import random_number_gen
from src.exam import database_id_search
from src.exam import print_user_options
from src.exam import get_resource_data
from src.exam import add_exam
from src.exam import list_exam
from src.exam import edit_exam
from src.exam import del_exam
from src.exam import exam_main

def test_random_number_gen():
    """testing the random_number_gen function"""
    rand_num = random_number_gen(13)
    assert len(str(rand_num)) == 13
    assert isinstance(rand_num, int)

def test_database_id_search(capfd):
    """testing the database_id_exam_name: math
exam_date: 10/10/2023
resource_data: [['textbook', '300']]search function"""
    database = {'0130487135087': \
          {'exam_name': 'your_exam', \
           'exam_date': '01-01-2000', \
            'resource_data':[["osmosis", "1000"], ["first-aid", "1000"]]}}
    db_id = database_id_search(database, 'your_exam')
    db_na_id = database_id_search(database, 'not_your_exam')
    assert isinstance(db_id, str)
    assert db_id == '0130487135087'
    assert db_na_id is None
    test_output, _ = capfd.readouterr()
    assert test_output == "key not found\n" or test_output is None

def test_print_user_options(capfd):
    """testing the print_user_options function"""
    print_user_options()
    test_output, _ = capfd.readouterr()
    assert test_output == "('a' and hit enter to add an exam that you are studying for)\n"\
    "('l' and hit enter to list exams that you are currently studying for)\n"\
    "('e' and hit enter to edit an exam that you are currently studying for)\n"\
    "('d' and hit enter to delete an exam that you are currently studying for)\n"\
    "('q' and hit enter to quit the exam editing suite)\n"

def test_get_resource_data():
    ...

def test_list_exam(capfd):
    list_exam()
    test_output, _ = capfd.readouterr()
    assert test_output == "exam_name: math\n"\
        "exam_date: 10/10/2023\n"\
        "resource_data: [['textbook', '300']]\n"
