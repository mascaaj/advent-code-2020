from dayX.src.puzzle2 import xyz, abc

def test_xyz():
    expected = [1, 3, 1]
    actual = [1, 3, 1]
    print(actual)
    assert len(expected) == len(actual)
    assert all([a == b for a, b in zip(actual, expected)])
    print(all([a == b for a, b in zip(actual, expected)]))

def test_abc():

    assert 
