def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {} # Declaring a counter using dictionary to create a frequency the numbers occurred
    
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    most_common = max(counts, key=counts.get)
    return most_common
    