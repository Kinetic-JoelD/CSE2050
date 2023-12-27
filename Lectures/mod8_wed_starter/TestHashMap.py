from HashMap import Entry, HashMap
import unittest

class TestEntry(unittest.TestCase):
    def setUp(self):
        """Creates some entries for later"""
        self.e1 = Entry(key=5, value="hello")

    def test_init(self):
        """initialize k:v pair"""
        self.assertEqual(self.e1.key, 5)
        self.assertEqual(self.e1.value, "hello")

    def test_repr(self):
        """two entries are equal iff their keys are equal"""
        self.assertEqual(repr(self.e1), "Entry(key=5, value=hello)")

class TestHashMap(unittest.TestCase):
    def test_init(self):
        """Tests an empty hashmap"""
        hm = HashMap()
        self.assertEqual(len(hm), 0)

    def test_put(self):
        """Tests that we can add keys and check membership"""
        n = 100
        hm = HashMap()

        for i in range(n):
            # Before adding
            self.assertEqual(len(hm), i)
            self.assertNotIn(i, hm)

            # Add
            hm[i] = str(i)
            
            # After adding
            self.assertIn(i, hm)

        # Repeat above, but guarantee no dups
        for i in range(n):
            hm[i] = str(i)
            self.assertIn(i, hm)
            self.assertEqual(len(hm), n)

    def test_put_get(self):
        """Tests that we can add keys, check membership, and retrieve keys"""
        n = 100
        hm = HashMap()

        for i in range(n):
            # Before adding
            self.assertEqual(len(hm), i)
            self.assertNotIn(i, hm)
            with self.assertRaises(RuntimeError):
                hm[i] # Not added - get raises runtime error

            # Add
            hm[i] = str(i)
            
            # After adding
            self.assertIn(i, hm)
            self.assertEqual(hm[i], str(i))
        
        # Repeat above, but guarantee no dups
        for i in range(n):
            hm[i] = str(i)
            self.assertIn(i, hm)
            self.assertEqual(len(hm), n)
            self.assertEqual(hm[i], str(i))

unittest.main()