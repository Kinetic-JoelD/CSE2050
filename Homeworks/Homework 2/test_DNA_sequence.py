import unittest
from DNA_sequence import Sequence, DNA


class TestSequence(unittest.TestCase):
    def setUp(self):
        self.sequence = Sequence('ATAACGGGCCA')

    def test_get_sequence(self):
        assert isinstance(self.sequence.get_sequence(), str) 

    def test_calculate_length(self):
        count = self.sequence.calculate_length()
        self.assertEqual(count, 11)

    def test_count_nucleotides(self):
        count = self.sequence.count_nucleotides()
        self.assertEqual(count['T'], 1)


class TestDNA_Sequence(unittest.TestCase):
    def setUp(self):
        """Creating the variable that will be tested on in the later tests"""
        self.sequence = DNA('GCATTGG')

    def test_reverse_complement(self):
        """ Tests the reverse compliment """
        self.assertEqual(self.sequence.reverse_complement(),'CCAATGC')

    def test_find_pattern(self):
        """ Tests the find pattern function """
        self.assertEqual(self.sequence.find_pattern('GG'),[5])

    def test_calculate_gc_content(self):
        """ Tests the calculate gc content function """
        self.assertEqual(self.sequence.calculate_gc_content(), 28.6)


unittest.main()