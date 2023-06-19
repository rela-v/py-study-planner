"""testing exam.py file functions"""
import json
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


def test_list_exam(capfd):
    """testing the list_exam() function"""
    list_exam('list_exam_test.json')
    test_output, _ = capfd.readouterr()
    assert test_output == "exam_name: math\n"\
        "exam_date: 10/10/2023\n"\
        "resource_data: [['textbook', '300']]\n"

def test_add_exam():
    """testing the add_exam function"""
    file_name = 'add_exam_test.json' 
    user_input = {'exam_name': 'math', 'exam_date': '10/10/2023', 'resource_data': [('textbook', '300')]}
    add_exam(user_input, file_name)
    with open(file_name,"r", encoding='utf-8') as exam_data_file:
        loaded = json.load(exam_data_file)
    attribute = list(loaded.keys())[0]
    print(loaded[attribute])
    firstItem = loaded[attribute]
    print(firstItem)
    assert firstItem["exam_name"] == "math"
    assert firstItem["exam_date"] == "10/10/2023"
    assert firstItem["resource_data"] == [["textbook", "300"]]
    with open(file_name,"w", encoding='utf-8') as exam_data_file:
        json.dump({}, exam_data_file)

def test_edit_exam():
    """testing the edit_exam() function"""
    exam = "math"
    file = 'edit_exam_test.json'
    flag = "n"
    data = "physics"

    edit_exam(exam, file, flag, data)
    with open(file,'r', encoding='utf-8') as exam_data_file:
        loaded = json.load(exam_data_file)
    assert loaded["527761539"]["exam_name"] == data

    edit_exam(data, file, flag, exam)

def test_del_exam():
    """testing the del_exam() function"""
    file = 'del_exam_test.json'
    exam = "math"
    del_exam(file, exam)
    user_input = {'exam_name': 'math', 'exam_date': '10/10/2023', 'resource_data': [('textbook', '300')]}
    add_exam(user_input, file)


