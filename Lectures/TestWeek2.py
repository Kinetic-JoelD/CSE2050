import unittest
from Week2 import Professor, Person, Student

class testProfessor(unittest.TestCase):
    def test_init(self):
        self.p1 = Professor('jake', 'jas14034', 'APIR', 'EII', {'23Fall':{'cse2050', 'cse4939w'}})
        self.assertEqual(self.p1.name, 'jake')
        self.assertEqual(self.p1.netID, 'jas14034')

    def test_addcourses(self):
        self.p1.add_course('24Fall', 'Engl1007')
        assert 'Engl1007' in self.p1.courseload['24Fall']
