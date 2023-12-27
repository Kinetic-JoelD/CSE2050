import unittest, random
from usermap import UserRecord, UserMap, PasswordError


class TestUserRecord(unittest.TestCase):
    def testCreation(self):
        # Normal creation case
        username = "usertest"
        password = "password123"
        user_record = UserRecord(username, password)
        
        self.assertEqual(user_record.username, username)
        self.assertTrue(user_record.salt)

    
    def testRepr(self):
        username = "Joel"
        password = "Duah"
        user_record = UserRecord(username, password)
                
        expected_repr = f"UserRecord: {username}"
        self.assertEqual(repr(user_record), expected_repr)

class TestUserMap(unittest.TestCase):
    def testLength(self):
        records1 = UserMap()

        records1.add_user('Albert', 'Password1')
        self.assertEqual(len(records1), 1)
        records1.add_user('Chip', 'Password2')
        records1.add_user('Trippie', 'Password3')
        self.assertEqual(len(records1), 3)

    def testGetItem(self):
        records = UserMap()

        mylast = 0

        for i in range(mylast, round(records._num_buckets * 0.75) + 1):
            records.add_user(f"user{i}", f"password'{i}")
            self.assertTrue(f'user{i}' in records)
            mylast += 1
            
        expected = "UserRecord: user3"
        result = str(records['user3'])

        self.assertEqual(result, expected)

    def testAddUser(self):
        records1 = UserMap()
        
        # Add a user to the empty user map
        records1.add_user('Joel', 'Duah')
        self.assertEqual(len(records1), 1)

        # Testing Contains function
        self.assertTrue('Joel' in records1)

        
        # Tests that a Runtime Error is raised for a duplicate
        with self.assertRaises(RuntimeError):
            records1.add_user('Joel', 'SomePass')
            pass

        # Tests that a user doesn't exisit
        self.assertFalse('Chris' in records1)

        # Creating a bunch of records and testing to see if thy are there and the length is correct
        records1.add_user('Beetlejuice', 'Password1')
        records1.add_user('Chip', 'Password2')
        records1.add_user('Dale', 'Password3')
        self.assertEqual(len(records1), 4)
        self.assertTrue('Beetlejuice' in records1)
        self.assertTrue('Chip' in records1)
        self.assertTrue('Dale' in records1)

    def testDouble(self):
        records2 = UserMap()

        # Adding users
        records2.add_user('Beetlejuice', 'Password1')
        records2.add_user('Chip', 'Password2')
        records2.add_user('Dale', 'Password3')
        self.assertEqual(records2._num_buckets, 8)

        # Add more users to trigger the resizing
        records2.add_user('Dave', 'Password4')
        records2.add_user('Eve', 'Password5')
        records2.add_user('Crisp', 'Password6')
        self.assertEqual(records2._num_buckets, 16)
        

        # Check that the records are correctly rehashed
        self.assertTrue('Beetlejuice' in records2)
        self.assertTrue('Chip' in records2)
        self.assertTrue('Dale' in records2)
        self.assertTrue('Dave' in records2)
        self.assertTrue('Eve' in records2)
        

        mylast = 7

        for i in range(mylast, round(records2._num_buckets * 0.75) + 1):
            records2.add_user(f"user{i}", f"password'{i}")
            self.assertTrue(f'user{i}' in records2)
            mylast += 1
        
        self.assertEqual(records2._num_buckets, 32)


        for i in range(mylast, round(records2._num_buckets * 0.75) + 1):
            records2.add_user(f"user{i}", f"password'{i}")
            self.assertTrue(f'user{i}' in records2)
            mylast += 1
        
        self.assertEqual(records2._num_buckets, 64)

        
        for i in range(mylast, round(records2._num_buckets * 0.75) + 1):
            records2.add_user(f"user{i}", f"password'{i}")
            self.assertTrue(f'user{i}' in records2)
            mylast += 1

        self.assertEqual(records2._num_buckets, 128)

        for i in range(mylast, round(records2._num_buckets * 0.75) + 1):
            records2.add_user(f"user{i}", f"password'{i}")
            self.assertTrue(f'user{i}' in records2)
            mylast += 1

        self.assertEqual(records2._num_buckets, 256)


    def testUpdatePassword(self):
        records1 = UserMap() 

        # We know the password 
        records1.add_user('Mickey', 'Password1')
        records1.update_password('Mickey', 'Password1', 'Password2')
    
        # An error has been raised for the old password so we know its changed
        with self.assertRaises(PasswordError):
            records1.update_password('Mickey', 'Password1', 'Wrong')
        
        # We are able to update the password so the new password is correct
        records1.update_password('Mickey', 'Password2', 'Password3')
        
        # We aren't able to change the passwrod with the old new passwrod so we know the implementation was done correctly
        with self.assertRaises(PasswordError):
            records1.update_password('Mickey', 'Password2', 'Wrong')
        
        

if __name__ == "__main__":
    unittest.main()