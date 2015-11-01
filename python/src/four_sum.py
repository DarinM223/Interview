
def four_sum(arr, s):
    """
    Given an array of numbers arr and a number S, find 4 different numbers in arr that sum up to S.

    Write a function that gets arr and S and returns an array with 4 indices of such numbers in arr, 
    or null if no such combination exists.  Explain and code the most efficient solution possible, 
    and analyze its runtime and space complexity.

    Solution: 
    Treat it like the 2 sum problem but instead of caching the number for each number, you are caching
    the number1 + number2 for each number1 and number2. Then you just loop through all pairs and try to find 
    the other pair by subtracting from target.
    """

    ht = {}
    # Cache the addition of pairs to a tuple of their indexes
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            ht[arr[i] + arr[j]] = (i, j)

    for key in ht:
        if s - key in ht:
            # Get two pairs that add up to the target number
            (first, second) = ht[key]
            (third, fourth) = ht[s - key]

            # Checks for duplicate indexes or duplicate values
            noDuplicateIndex = first != third and first != fourth and second != third and second != fourth
            noDuplicates = len(set([arr[first], arr[second], arr[third], arr[fourth]])) == 4

            if noDuplicateIndex and noDuplicates:
                return (arr[first], arr[second], arr[third], arr[fourth])

    return None

