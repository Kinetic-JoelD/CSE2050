class Record:
    def __init__(self, key, count):
        self.key = key
        self.count = count


class Hashtable:
    def __init__(self):
        self._n_buckets = 8
        self._n_keys = 0
        self._n_total = 0
        self._L[[] for i in range(self._n_buckets)]

    def __len__(self):
        return self._n_total
    
    def _rehash(self, new_size):
        self._n_buckets = new_size
        new_L = [[] for i in range(self._n_buckets)]

        for bucket in self._L:
            for record in bucket:
                new_L[self._find_bucket(record.key)].append(record)

        self._L = new_L

    def _find_bucket(self, key):
        return key % self._n_buckets
    

    def add(self, key):
        """Increment the count of a key by 1, or adds it with a count of 1 if not already in hashtable"""

    def __getitem__(self, key):
        """Returns the count associated wiht a key. Return 0 if key in Hastable"""
        