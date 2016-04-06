def bucket_sort(A):

    """
    Sorts the list 'a' using Bucket sort algorithm
    >>> from pydsa import bucket_sort
    >>> a = [3, 4, 2, 1, 12, 9]
    >>> bucket_sort(a)
    [1, 2, 3, 4, 9, 12]
    """
    buckets = [[] for x in range(11)]
    for i, x in enumerate(A):
        buckets[x//10].append(x)
    out = []
    for buck in buckets:
        out += isort(buck)
    return out


def isort(A):
    if len(A) <= 1: 
        return A
    i = 1
    while i < len(A):
        k = A[i]
        j = i - 1
        while j >= 0 and A[j] > k:
            A[j+1] = A[j]
            A[j] = k
            j -= 1      
        i += 1
    return A
