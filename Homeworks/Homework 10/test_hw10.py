import unittest, random

from hw10 import Patient, PriorityQueue, EmergencyRoom


class test_patient_creation(unittest.TestCase):
    """
    Test the creation of a Patient object
    """
    def test_patient_creation(self):
        Zoey = Patient('Zoey', 1)
        Garfield = Patient('Garfield', 2)
        Patrick = Patient('Patrick', 1)

        self.assertFalse(Zoey < Garfield)
        self.assertTrue(Garfield < Zoey)
        
        
        # Edge Case: Same Priority
        # Patrick and Zoey are the same so one  is less than the other 
        self.assertFalse(Zoey < Patrick)
        self.assertFalse(Patrick < Zoey)




class test_priority_queue_push_pop(unittest.TestCase):
    """
    Test the push and pop operations in the priority queue
    """
    def test_priority_queue_push_pop(self):
        Garfield = Patient('Garfield', 2)
        Patrick = Patient('Patrick', 1)
        my_PQ = PriorityQueue()
        mi_PQ = PriorityQueue()


        # Testiing simple push pop
        self.assertTrue(my_PQ.is_empty())
        my_PQ.push(Patient('Zoey', 1))

        self.assertEqual(my_PQ.pop().name, 'Zoey')
        self.assertTrue(my_PQ.is_empty())

        my_PQ.push(Patient('Zoey', 2))
        my_PQ.push(Garfield)
        my_PQ.push(Patrick)

        my_PQ.pop()
        my_PQ.pop()

        self.assertFalse(my_PQ.is_empty())

        my_PQ.pop()

        self.assertTrue(my_PQ.is_empty())


        # Creating a bunch of patients with random severities
        for i in range(1000):
            # Create Patients with random priorities
            mi_PQ.push = Patient(f'patient{i}', random.randint(1, 5))
        
        for i in range(1000):
            # Removing all the patients from the priority queue
            if len(mi_PQ) != 0:
                mi_PQ.pop()
                self.assertEqual(len(mi_PQ), 100 - i)
            else:
                # Checking to make sure an error is raised whent PQ is empty
                with self.assertRaises(IndexError):
                    mi_PQ.pop()



class test_emergency_room_simulation(unittest.TestCase):
    """
    Test the overall simulation process in the EmergencyRoom class.
    """
    def test_admit_patient(self):

        my_ER = EmergencyRoom()

        # Initlaized ER is empty
        self.assertTrue(my_ER.waiting_room.is_empty)
        
        # Expected use
        expected = 'Plankton admitted to the emergency room with severity 5'
        self.assertEqual(my_ER.admit_patient(Patient('Plankton', 5)), expected)


        # Edge case: Raises an exception when a person doesn't use the patient class
        with self.assertRaises(Exception):
            my_ER.admit_patient('Tracy')



    def test_treat_patient(self):
        # Expected use
        my_ER = EmergencyRoom()
        expected = 'Treating Plankton with severity 5'
        my_ER.admit_patient(Patient('Plankton', 5))
        self.assertEqual(my_ER.treat_patient(), expected)


        # Waiting room is empty 
        self.assertTrue(my_ER.waiting_room.is_empty())



    def test_simulate_emergency_room(self):

        emergency_room = EmergencyRoom()

        # Simulate admitting and treating patients
        num_patients = 5
        emergency_room.simulate_emergency_room(num_patients)

        # Assert that after simulation, the waiting room is empty
        self.assertTrue(emergency_room.waiting_room.is_empty())
    

unittest.main()