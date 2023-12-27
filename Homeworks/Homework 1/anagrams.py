def is_anagram(word1, word2):
    """
    Compares two wrods given by the user to see if its a string.
    """
    #Reverses the first word
    word1 = word1[::-1]

    #Are the reversed word and the first one the same?
    if word1 == word2:
        return True
    else:
        return False