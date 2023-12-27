import timeit, random
from HashMap import Entry, HashMap

SETUP_CODE = """from __main__ import collection"""
TEST_CODE = """-1 in collection"""

# Table header
WIDTH = 80
print(" SORTED ".center(WIDTH, "="))
print(f"{'n ':7}{'t_lst':>11}{'size_lst':>11} | {'t_set':>11}{'size_set':>11} | {'t_hm':>11}{'size_hm':>11}")
print("-"*WIDTH)

# Table Body
for n in range(1, 11):
    n = int(n*1E3)
    L = [i for i in range(n)]
    S = {i for i in range(n)}
    HM = HashMap()
    for i in range(n):
        HM[i] = str(i)
    collections = [L, S, HM]

    print(f"{n:7}", end='', flush=True)

    for collection in collections:
        # Worst case time in ms (search for item not in collection)
        t = 1000*timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=100)
        print(f"{t:>8.3g} ms", end='', flush=True)

        # Size of collection in MB
        size = collection.__sizeof__()/1E6
        print(f"{size:>8.3g} MB", end='', flush=True)
        
        print(" | ", end='', flush=True)
    input()

# footer
print("-"*WIDTH)