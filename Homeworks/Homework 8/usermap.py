import random
import string

class PasswordError(Exception):
    """Custom error to be used in UserMap when wrong password is given for a user."""
    def __init__(self, message):
        self.message = message
    def __repr__(self):
        return f"PasswordError: {repr(self.message)}"

class UserRecord:
    def __init__(self, username, password):
        self.username = username
        # Generating random string of 8 characters
        self.salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        self.password_hash = hash(self.salt + password)
    
    def __repr__(self):
        """Returns a string represention of a UserRecord."""
        return f"UserRecord: {self.username}"

class UserMap:
    def __init__(self):
        self._num_buckets = 8
        self._max_load_factor = .75
        self._len = 0
        self._buckets = [None for i in range(self._num_buckets)]
    
    def __len__(self):
        """Returns the number of records stored in the database."""
        return self._len
    
    def _find_bucket_index(self, username):
        """Returns the index of the bucket `item` should go in, based on hash(item) and self.n_buckets"""
        return hash(username) % self._num_buckets

 
    def __getitem__(self, username):
        """Returns the stored user recored for a given username. Raises KeyError if a record for the given username is not in the database."""
        # The index the user should be put at
        bucket_idx = self._find_bucket_index(username)

        # Loop that checks the expected index for the username if a spot is none it means its not there
        while self._buckets[bucket_idx] is not None:
            if self._buckets[bucket_idx].username == username:
                # Prof said in discord to return the record 
                return self._buckets[bucket_idx]
            
            
            # Increment to the next possible spot the item could be at (linear Probing)
            bucket_idx = (bucket_idx + 1) % self._num_buckets

        # Not found in the database so it raises a key error
            raise KeyError('Username is not in database')
    
    def __contains__(self, username):
        """Returns True or (False) if a given username is (is not) registered in the database"""
        # The index the user should be put at
        bucket_idx = self._find_bucket_index(username)

        # Loop that checks the expected index for the username if a spot is none it means its not there
        while self._buckets[bucket_idx] is not None:
            if self._buckets[bucket_idx].username == username:
                return True
            
            # Increment to the next possible spot the item could be at (linear Probing)
            bucket_idx = (bucket_idx + 1) % self._num_buckets

        # The user was not found so return false
        return False
    
    def add_user(self, username, password):
        """Adds a user record to the database using the given username and password."""
        # The index the user should be put at
        bucket_idx = self._find_bucket_index(username)

        #Loop through the hash to find a spot for it
        while self._buckets[bucket_idx] is not None:
            # The username already exisists in the has
            if self._buckets[bucket_idx].username == username:
                # raises an error
                raise RuntimeError("This user already exisists")
            # The username wasn't found at that index so increment to the next index
            bucket_idx = (bucket_idx + 1) % self._num_buckets

        # At an open hash we add the record the user wants to add 
        self._buckets[bucket_idx] = UserRecord(username, password)

        # Increment length plus one
        self._len += 1

        # Checking if the laod factor hasn't exceeded our max items if so we double the hastable
        if (self._len / self._num_buckets) >= self._max_load_factor:
            self._double()


    def _double(self):
        """ Private method that is used to double the size of internal storage within the database when the number of records exceeds 75%. """
        # The number we want to double the hashtable to
        self._num_buckets = self._num_buckets * 2

        # Creating the new buckets
        new_buckets = [None] * self._num_buckets

        # Move existing records to their new positions in the bigger buckets
        for record in self._buckets:
            if record is not None:
                # Find the new index for the record in the bigger buckets
                idx = self._find_bucket_index(record.username)
                while new_buckets[idx] is not None:
                    idx = (idx + 1) % self._num_buckets
                # Place the record in its new location
                new_buckets[idx] = record

        # Update the old buckets with the bigger buckets
        self._buckets = new_buckets

    def update_password(self, username, current_password, new_password):
        # The index the user should be put at
        bucket_idx = self._find_bucket_index(username)
        print(bucket_idx)
        user_found = False

        # Taking the current password and the old salt combingig to see if its the correct hash
        while self._buckets[bucket_idx] is not None:
            if self._buckets[bucket_idx].username == username:

                # Creating a hash with the stored salt and the user entered password
                verification = hash(self._buckets[bucket_idx].salt + current_password)

                # Checking to see if the hash created matches with the stored hash
                if self._buckets[bucket_idx].password_hash == verification:
                    # Generates a new salt for the new password
                    self._buckets[bucket_idx].salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
                    # Creating a new passwrod hash with the new salt and the new password
                    self._buckets[bucket_idx].password_hash = hash(self._buckets[bucket_idx].salt + new_password)
                    # we found the user we were looking for so an error doesn't need ot be raised when we break 
                    user_found = True
                    break
                # User was found but wrong password was entered
                else: 
                    raise PasswordError('Incorrect Password')
            
            # Increment to check the next bucket
            bucket_idx = (bucket_idx + 1) % self._num_buckets

            # The user isn't found so raise an error
            if user_found is False:
                raise KeyError("User Not in Database")


    def __repr__(self):
        """Returns a string representation of the internal storage of UserMap."""
        return "\n".join(f"bucket{b}: {rec}" for b, rec in enumerate(self._buckets))


if __name__ == "__main__":
    records = UserMap()

    records.add_user('user1','password1')

    print(records['user1'])
    records.update_password('user1', 'password4', 'password2')