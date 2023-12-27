import string

def count_letters(file):
    """
    Counts the occurrence of lower case letters in a text
    Returns the dictionary of letter:count pairs. Only include letters present in the file 
    """

    #opens text file and creating a new dictionary
    f = open(file)
    my_letters = {}

    #Runs through lines
    for line in f:

        #Runs through each letter in that line
        for letter in line:
            letter = letter.lower()
            #Is the space I'm currently at a lowercase letter and not in the dictionary?
            if letter not in my_letters.keys() and letter in string.ascii_lowercase:
                #True: Create a new dictionary with the value of 1
                my_letters[letter] = 1
            elif letter in string.ascii_lowercase:
                #Reoccuring letter just add one to the value
                my_letters[letter] += 1
            else:
                #False: move on to the next letter
                continue

    #Closing the file and returning the dictionary
    f.close
    return my_letters            


