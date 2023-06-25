"""testing exam.py file functions"""
from src.exam import ExamManager
import json


class TestExam:

    listExamMgr = ExamManager('tests/exam_db/one_test.json')
    addExamMgr = ExamManager('tests/exam_db/empty_test.json')


    def test_print_user_options(self, capfd):
        """testing the print_user_options function"""
        self.listExamMgr.print_user_options()
        test_output, _ = capfd.readouterr()
        assert test_output == "('a' and hit enter to add an exam that you are studying for)\n"\
        "('l' and hit enter to list exams that you are currently studying for)\n"\
        "('e' and hit enter to edit an exam that you are currently studying for)\n"\
        "('d' and hit enter to delete an exam that you are currently studying for)\n"\
        "('q' and hit enter to quit the exam editing suite)\n"
    
    def test_list_exam(self, capfd):
        """testing the list_exam() function"""
        self.listExamMgr.list_exam()
        test_output, _ = capfd.readouterr()
        assert test_output == "exam_name: math\n"\
            "exam_date: 10/10/2023\n"\
            "resource_data: [['textbook', '200'], ['website', '250']]\n"
    
    def test_add_exam(self):
        """testing the add_exam function"""
        exam_name = 'math'
        user_input = {f"{exam_name}": { 'exam_date': '10/10/2023', 'resource_data': [('textbook', '300')]}}
        self.addExamMgr.add_exam(user_input)
        with open(self.addExamMgr.db_file,"r", encoding='utf-8') as exam_data_file:
            loaded = json.load(exam_data_file)
        print(loaded[exam_name])
        firstItem = loaded[exam_name]
        print(firstItem)
        assert firstItem["exam_date"] == "10/10/2023"
        assert firstItem["resource_data"] == [["textbook", "300"]]
        with open(self.addExamMgr.db_file,"w", encoding='utf-8') as exam_data_file:
            json.dump({}, exam_data_file)
    
    def test_edit_exam(self):
        """testing the edit_exam function"""
        exam ='math'
        flag = 'n'
        data = 'physics'
        self.listExamMgr.edit_exam(exam, flag, data)
        with open(self.listExamMgr.db_file, 'r', encoding='utf-8') as exam_data_file:
            loaded = json.load(exam_data_file)
        assert data in list(loaded)
        self.listExamMgr.edit_exam(data, flag, exam)
    
    def test_del_exam(self):
        """testing the del_exam() function"""
        exam = 'math'
        with open(self.listExamMgr.db_file, 'r', encoding='utf-8') as exam_data_file:
            old_loaded = json.load(exam_data_file)
        self.listExamMgr.del_exam(exam)
        with open(self.listExamMgr.db_file, 'r', encoding='utf-8') as exam_data_file:
            loaded = json.load(exam_data_file)
        assert len(loaded) == 0
        with open(self.listExamMgr.db_file, "w", encoding='utf-8') as exam_data_file:
            json.dump(old_loaded, exam_data_file)

