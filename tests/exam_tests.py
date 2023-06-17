"""testing exam.py file functions"""



import unittest
from unittest import mock
from io import StringIO
from src.exam import random_number_gen
from src.exam import database_id_search
from src.exam import print_user_options
from src.exam import get_resource_data
from src.exam import add_exam
from src.exam import list_exam
from src.exam import edit_exam
from src.exam import del_exam
from src.exam import exam_main

# These tests can be run using the command: python3 -m unittest tests/exam_tests.py in the root directory

class testRandomNumberGen(unittest.TestCase):
    def test(self):
        """testing the random_number_gen function"""
        n = 13
        rand_num = random_number_gen(n)
        self.assertEqual(len(str(rand_num)) ,n)
        self.assertIsInstance(rand_num, int)


class testDatabase(unittest.TestCase):
    def test_database_id_search(self):
        """testing the database_id_search function"""
        database = {'0130487135087': \
          {'exam_name': 'your_exam', \
           'exam_date': '01-01-2000', \
            'resource_data':[["osmosis", "1000"], ["first-aid", "1000"]]}}
        db_id = database_id_search(database, 'your_exam')
        db_na_id = database_id_search(database, 'not_your_exam')
        self.assertIsInstance(db_id, str)
        self.assertEqual(db_id, '0130487135087')
        self.assertIsNone(db_na_id)
        """This acomplishes the same as capfd.readouterr()"""
        with mock.patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            db_na_id = database_id_search(database, 'not_your_exam')
            test_output = mocked_stdout.getvalue()
        self.assertTrue(test_output == "key not found\n" or test_output is None)

class testUserOptions(unittest.TestCase):
    def test_print_user_experience(self):
        with mock.patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            print_user_options()
            test_output = mocked_stdout.getvalue()
            self.assertEqual(test_output, "('a' and hit enter to add an exam that you are studying for)\n"\
    "('l' and hit enter to list exams that you are currently studying for)\n"\
    "('e' and hit enter to edit an exam that you are currently studying for)\n"\
    "('d' and hit enter to delete an exam that you are currently studying for)\n"\
    "('q' and hit enter to quit the exam editing suite)\n")
    
    def test_get_resource_data(self):
        ...

if __name__ == '__main__':
    unittest.main()
