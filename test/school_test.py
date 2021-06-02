import unittest
import sys
sys.path.append('../')
from classes.school import School

class SchoolTest(unittest.TestCase):

    shared_inst = None
    
    @classmethod
    def setUpClass(cls):
        cls.shared_inst = School("Test School")

    def test_find_student_by_invalid_id(self):
        self.assertEqual (self.shared_inst.find_student_by_id('666'), 'ID not found')

    def test_find_student_by_id(self):
        self.assertIs (type(self.shared_inst.find_student_by_id('788908').name), str)

    def test_list_students(self):
        self.assertLogs(self.shared_inst.list_students())

unittest.main()