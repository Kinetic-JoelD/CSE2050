class Entry:
    """Helper class for HashMap. Encapsulates Key and Value into a single object."""
    def __init__(self, key, value):
        """Creates a new entry"""
        self.key = key
        self.value = value

    def __repr__(self):
        """String representation of Entry"""
        return f"Entry(key={self.key}, value={self.value})"

class HashMap:
    def __init__(self):
        """Creates an empty hash map"""
        self._n_buckets = 8
        self._len = 0
        self._L = [[] for i in range(self._n_buckets)]

    def __len__(self):
        """Returns the number of k:v pairs stored"""
        return self._len


    def _find_bucket(self, key):
        """Returns the index of the bucket for a key"""
        return hash(key) % self._n_buckets

    def __setitem__(self, key, value):
        """Adds k:v pair, or updates v if k already in HashMap"""
        idx_bkt = self._find_bucket(key)

        # Search through every entry in that bucket, looking for key
        for entry in self._L[idx_bkt]:
            if key == entry.key: # We've found a matching key
                entry.value = value # update val
                self._L
                return 
            
            self._L[idx_bkt].append(Entry(key, value))
            self._len += 1
            

    def __getitem__(self, key):
        """Returns value associated with key. Raises RuntimeError if Key not in HashMap"""
        idx_bkt = self._find_bucket(key) # Find bucket for key

        # Search through every entry in that bucket, looking for key
        for entry in self._L[idx_bkt]:
            if key == entry.key: # We've found a matching key 
                return entry.value 
        
        raise RuntimeError(f"key {key} is not in HashMap")
            

    def __contains__(self, key):
        """Returns True (False) if key is (is not) in HashMap"""
        idx_bkt = self._find_bucket(key)

        # Search through every entry in that bucket, looking for key
        for entry in self._L[idx_bkt]:
            if key == entry.key: # We've found a matching key 
                return True
            
        return False

        

    def _rehash(self, new_size):
        """ 
        Rehashes every item oto new_size number of buckets
        """
        self._n_buckets = new_size
        new_L = [[] for i in range(self._n_buckets)]

        # Rehash every item 
        for bucket in self._L:
            for entry in bucket:
                idx_new = self._find_bucket(entry.key)
                new_L[idx_new] = entry

    def values(self):
        pass
        
    def __repr__(self):
        """Returns a string representation"""
        return f"Mapping(table = {self._L}"
    
    def __iter__(self):
        """Returns a string representation"""
        for bucket in self._L:
            for entry in bucket:
                yield entry.key 

if __name__ == "__main__":

    hm = HashMap()

    hm['Cassie'] = {'Wolf', 'Grizzly'}
    hm['aJake'] = {'Osprey', 'Eagle'}
    hm['Rachel'] = {'Octopus', 'Deer'}


    for k, v in hm:
        print(k, v)
    print()