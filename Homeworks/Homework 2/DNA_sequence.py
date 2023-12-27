class Sequence:
    def __init__(self, seq):
        self.seq = seq

    def get_sequence(self):
        """ Returns the DNA sequence """
        return f'{self.seq}'
    
    def calculate_length(self):
        """ Calculates and returns the length of the sequence """
        return len(self.seq)
    
    def count_nucleotides(self):
        """ Counts and returns a dictionary that contains the number of each nucleotide (A, T, C, G) in the sequence"""

        # created the dictionary
        nucleotides = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

        # Iterate through the given string
        for base in self.seq:
            
            # Checks if the base is in the dict if so add one else continue through the string
            if base in nucleotides.keys():
                nucleotides[base] += 1 
            else:
                continue 

        return nucleotides


class DNA(Sequence):
    def __init__(self, DNA_seq):
        Sequence.__init__(self, DNA_seq)

    def reverse_complement(self):
        """
        Returns the reverse complement of the DNA sequence. The reverse
        complement is obtained by reversing the sequence and replacing each nucleotide with its complement
        (A with T, T with A, C with G, and G with C) 
        """

       #Creating an empty string
        reverse = ''
        valid_bases = ['A','C','G','T']

        #Iterate through the string
        for base in self.seq[::-1]:

            #No valid base then move on to the next letter in the string
            if base not in valid_bases:
                continue
            
            # Replacing bases with their reverse
            elif base == 'A':
                reverse += 'T'
            elif base == 'T':
                reverse += 'A'

            elif base == 'C':
                reverse += 'G' 
            elif base == 'G':
                reverse += 'C'

        #Returns the reversed list
        return reverse
        

    def find_pattern(self, pattern):
        """
        Returns the starting indices of all occurrences of a given pattern in
        the DNA sequence.
        """

        # Initializing variables. Counter counts the occurrences of the patter in the sequence
        pattern_lst = []
        # To not iterate through repeat spots that would cause duplicate counts
        jumper = 0

        # Iterate through the sequence
        while jumper < len(self.seq) - 1:

            # Finds the index of where pattern is located at starting from jumper
            pattern_idx = self.seq.find(pattern, jumper)

            # If there is a pattern in the sequence count it and then move jumper to the next base after it
            if pattern_idx != -1:
                pattern_lst.append(pattern_idx)
                jumper = pattern_idx + 1
            else:
                break

        return pattern_lst
        
    

    def calculate_gc_content(self):
        """
        Calculates and returns the GC content of the DNA sequence as a
        percentage 
        """

        # Initializing variables. Counter counts the occurrences of GC sequence in the sequence
        counter = 0
        # To not iterate through repeat spots that would cause duplicate counts
        jumper = 0

        # Iterate through the sequence
        while jumper < len(self.seq) - 1:

            # Finds and the index of where GC is located
            gc_idx = self.seq.find('GC',jumper)

            # If there is a GC in the sequence count it and then move jumper to the next base after it
            if gc_idx != -1:
                counter += 1
                jumper = gc_idx + 1
            else:
                break

            # Math to figure out the percentage GC makes up of the whole sequence

        return float(format(((counter * 2) / len(self.seq)) * 100, '.1f'))


if __name__ == "__main__":
    # Creating an instance of the sequence class
    s1 = Sequence('ATGTTCCGA')
    d1 = DNA('ATGCATGCGGGCA')

    # Test the implemented methods of the sequence class
    get_sequence = s1.get_sequence()
    calculate_length = s1.calculate_length()
    count_nucleotides = s1.count_nucleotides()

    # Test the implemented methods the DNA class
    reverse_compliment = d1.reverse_complement()
    find_pattern = d1.find_pattern('CA')
    calculate_gc_content = d1.calculate_gc_content()

    print(f'Originial Sequence: {get_sequence}')
    print(f'Sequence Length: {calculate_length}')
    print(f'Sequence nucleotides: {count_nucleotides}')
    print(f'Reverse Complement: {reverse_compliment}')
    print(f'Pattern Indicies: {find_pattern}')
    print(f'GC Content: {calculate_gc_content}')

