# Map ADT supports at a minimum:
#       * put(key, value) -  adds key:value pair
#       * get(key)        - returns value associated with key


class Entry :
    def __init__(self, key, value):
        self.key = key
        self.value = value

        
class Mapping:
    def __init__(self):
        self._L = []


    def __setitem__(self, key, value):
        pass

    def __getitem__(self, key):
        pass

if __name__ == "__main__":
    m = Mapping()
    n = 100

    for i in range(n):
        m[i] = str(i)

    for i in range(n):
        assert m[i] == str(i)