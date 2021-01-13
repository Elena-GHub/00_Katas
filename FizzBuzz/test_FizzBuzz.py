from FizzBuzz import FizzBuzz


def test_multiple_of_five_and_three_should_return_fizzbuzz():
    f = FizzBuzz()
    assert f.say(15) == 'FizzBuzz'


def test_multiple_of_three_should_return_fizz():
    f = FizzBuzz()
    assert f.say(6) == 'Fizz'


def test_multiple_of_five_should_return_buzz():
    f = FizzBuzz()
    assert f.say(10) == 'Buzz'


def test_return_number_if_not_multiple_of_three_nor_five():
    f = FizzBuzz()
    assert f.say(13) == 13
