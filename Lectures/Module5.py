def reverse_str_recur(string, idx):
    #Base case

    #list that takes in the last element every call

    reversedLst = []

    reversedStr= reversedLst.join()
    
    idx = len(string) - 1
    
    if idx != -1:
        reversedLst.append(string[idx])
        reverse_str_recur(string, idx)

    if idx < 0:
        return reversedStr
    


    def rev_str_rec(s):
        """Recursivelyy reverses a string"""

        # Base case - string of 0 or 1 letters is reversed
        if len(s) <= 1: return s
        return rev_str_rec(s[1:]) + s[0]
    
    def bs_recr_idx(L, item, i_left, i_right):
        if i_right - i_left <= 1: return False
        elif i_right - i_left == 2: return L[i_left] == item

        i_med = (i_left + i_right) // 2

        if[i_med] == item: return True
        elif item < L[i_med]: return bs_recr_idx(L, item, i_left, i_med)
        elif item > L[i_med]: return bs_recr_idx(L, item, i_med, i_right)

    


    if __name__ == '__main__':
        pass
