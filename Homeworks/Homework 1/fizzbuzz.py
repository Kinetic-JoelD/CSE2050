###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################

def fizzbuzz(start, finish):
    """
    Prints numbers from start to finish. 
    Replaces multiples of 3 with "fizz", multiples of 5 with "buzz", and multiples of both with "fizzbuzz"
    Replaces numbers that contain 3 or 5 (e.g. 13, 52) with "fizz", "buzz", or "fizzbuzz"
    """

    #Creating a for loop to run through a range of numbers
    for x in range(start, finish+1):

        #Finding if numbers that are being run through contain a 3 or 5 and then replacing them
        if str(x).find('3') != -1 and str(x).find('5') != -1:
            print('fizzbuzz')
        elif str(x).find('3') != -1:
            print('fizz')
        elif str(x).find('5') != -1:
            print('buzz')
        
        #Finding numbers that are divisible by 3 or 5 and replacing them, 0 is an exception
        elif x == 0:
            print(0)
        elif x % 3 == 0 and x % 5 == 0:
            print('fizzbuzz')
        elif x % 3 == 0:
            print('fizz')
        elif x % 5 == 0:
            print('buzz')
       
       #Prints numbers that don't meet any of the other conditions
        else:
            print(x)
