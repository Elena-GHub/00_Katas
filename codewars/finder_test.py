from finder import Finder


def test_find_integer_with_odd_occurences():
    finder = Finder()
    assert finder.find_integer_with_odd_occurences([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
    assert finder.find_integer_with_odd_occurences([1,1,2,-2,5,2,4,4,-1,-2,5]) == -1
    assert finder.find_integer_with_odd_occurences([20,1,1,2,2,3,3,5,5,4,20,4,5]) == 5
    assert finder.find_integer_with_odd_occurences([10]) == 10
    assert finder.find_integer_with_odd_occurences([1,1,1,1,1,1,10,1,1,1,1]) == 10
    assert finder.find_integer_with_odd_occurences([5,4,3,2,1,5,4,3,2,10,10]) == 1
