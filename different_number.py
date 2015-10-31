
def different_number(l, n):
    """
    Given an array of unique numbers with size n, returns a number not in the array

    Implemented using a hash table with size n+1 that hashes to boolean (1 or 0).
    Based on the pidgeonhole principle, there will be at least one empty slot. 
    The index of the slot will also not be in the original array because 
    of modulus magic
    """

    hash_table = []

    # create hash table from 0 to n
    for i in range(0, n+1):
        hash_table.append(0)

    # put every number into the hash table
    for num in l:
        hash_table[num % (n + 1)] = 1

    # check for empty slot
    for i in range(0, n+1):
        if hash_table[i] == 0:
            return i

