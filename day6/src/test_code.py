
import numpy as np
from day6.src.puzzle2 import histogram,hist_val_check

def test_hist():
    expected = [1, 3, 1]
    actual = np.fromiter(histogram("puppy").values(),dtype="int")
    print(actual)
    assert len(expected) == len(actual)
    assert all([a == b for a, b in zip(actual, expected)])
    print(all([a == b for a, b in zip(actual, expected)]))

def test_hist_val_check():
    hist = histogram("macuziywlbapodgevujnskptruz")
    assert hist_val_check(hist,1,3) == 1
