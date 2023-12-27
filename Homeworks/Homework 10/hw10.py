import random

class Patient:
    def __init__(self, name, severity):
        """
        Initialize a Patient object.
        Parameters:
        - name (str): The name of the patient.
        - severity (int): The severity level of the patient's condition.
        """
        self.name = name
        self.severity = severity

    def __lt__(self, other):
        """
        Compare two patients based on severity for priority queue ordering.
        Parameters:
        - other (Patient): Another patient to compare.
        Returns:
        - bool: True if the current patient has higher priority (lower severity), False otherwise.
        """
        return self.severity > other.severity

class PriorityQueue:
    def __init__(self):
        """Initialize an empty priority queue."""
        self._entries = []

    def is_empty(self):
        """
        Check if the priority queue is empty.
        Returns:
        - bool: True if the priority queue is empty, False otherwise.
        """
        return len(self._entries) == 0

    def push(self, item):
        """
        Add an item to the priority queue.
        Parameters:
        - item: The item to add to the priority queue.
        """
        self._entries.append(item)
        self._upheap(len(self._entries) - 1)

    def pop(self):
        """
        Remove and return the item with the highest priority from the priority queue.
        Returns:
        - item: The item with the highest priority.
        """
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        self._swap(0, -1)
        item = self._entries.pop()
        self._downheap(0)
        return item

    def _parent(self, i):
        """
        Get the index of the parent of the element at index i.
        """
        return (i - 1) // 2

    def _children(self, i):
        """
        Get the indices of the children of the element at index i.
        """
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._entries), right + 1))

    def _swap(self, a, b):
        """
        Swap elements at indices a and b in the priority queue.
        """
        L = self._entries
        L[a], L[b] = L[b], L[a]

    def _upheap(self, i):
        """
        Restore the heap order after adding an element to the end.
        """

        L = self._entries

        parent = self._parent(i)
        # Looking at children if the child at that index is less than the parent
        if i > 0 and L[i] < L[parent]:
            # swap the parent with the child
            self._swap(i, parent)
            # Calls upheap again until reach the root making sure heap order is sustained
            self._upheap(parent)

    def _downheap(self, i):
        """
        Restore the heap order after removing the root element.
        """
        L = self._entries

        children = self._children(i)
        if children:
            # Find the index of the child node with the smallest value in list L
            min_child_index = children[0] 
            
            # Iterate through the children to find the one with the smallest value
            for child_index in children:
                if L[child_index] < L[min_child_index]:
                    min_child_index = child_index
            
            # Check if the value of the smallest child is less than its parent's value
            if L[min_child_index] < L[i]:
                # swaps the values of the parent and the smallest child
                self._swap(i, min_child_index)
                
                # Recursively call _downheap() on the smallest child to maintain the heap property downward
                self._downheap(min_child_index)

    def __len__(self):
        """ Gets the length of the Priority Queue """
        return len(self._entries)

class EmergencyRoom:
    def __init__(self):
        """Initialize an EmergencyRoom object with an empty waiting room."""
        self.waiting_room = PriorityQueue()
        self.treated_patients = []

    def admit_patient(self, patient):
        """
        Admit a patient to the emergency room.
        Parameters:
        - patient (Patient): The patient to admit.
        """
        if isinstance(patient, Patient):
            self.waiting_room.push(patient)
            print(f'{patient.name} admitted to the emergency room with severity {patient.severity}')
            return f'{patient.name} admitted to the emergency room with severity {patient.severity}'
        else:
            raise Exception(f"Entered incorretly. Patient({patient}, Serverity number 1-10)")

    def treat_patient(self):
        """Treat the next patient in the waiting room, if any."""
        if self.waiting_room != 0:
            treating_patient = self.waiting_room.pop()
            print(f'Treating {treating_patient.name} with severity {treating_patient.severity}')
            return f'Treating {treating_patient.name} with severity {treating_patient.severity}'


    def simulate_emergency_room(self, num_patients):
        """ Simulate the operation of the emergency room. """
        for i in range(num_patients):
            name = f"Patient-{i+1}"
            severity = random.randint(1, 10)  # Severity level is randomly assigned
            patient = Patient(name, severity)
            self.admit_patient(patient)

        while not self.waiting_room.is_empty():
            self.treat_patient()

if __name__ == "__main__":
    er = EmergencyRoom()
    er.simulate_emergency_room(10)
