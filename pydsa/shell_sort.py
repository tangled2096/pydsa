# Shell sort
# Complexity: Best case: O(n log2 n), Average case: depends on gap sequence,
# Worst case: О(n^2)


def shell_sort(A):
    
    """
        Sorts the list 'A' using Bucket sort algorithm
        >>> from pydsa import shell_sort
        >>> A = [3, 4, 2, 1, 12, 9]
        >>> shell_sort(A)
        [1, 2, 3, 4, 9, 12]
    """
    inc = len(A) // 2
    while inc:
        for i in range(len(A)):
            j = i
            temp = A[i]
            while j >= inc and A[j-inc] > temp:
                A[j] = A[j - inc]
                j -= inc
            A[j] = temp
        inc = inc//2 if inc//2 else (0 if inc == 1 else 1)
    return A
