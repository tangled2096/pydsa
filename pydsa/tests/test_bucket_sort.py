from pydsa import bucket_sort
from random import randint


def test_bucket_sort():
    a = b = [randint(1, 100) for i in range(100)]
    assert bucket_sort(a) == sorted(b)