from multiplier import Multiplier


def test_number_value_is_between_two_and_twenty():
    multiplier = Multiplier()
    # pylint: disable=maybe-no-member
    assert multiplier.check_number_is_in_range(5) == True

def test_number_value_is_one_should_return_false():
    multiplier = Multiplier()
    assert multiplier.check_number_is_in_range(1) == False

def test_number_value_is_bigger_than_twenty_should_return_false():
    multiplier = Multiplier()
    assert multiplier.check_number_is_in_range(23) == False

def test_number_multiplied_should_return_times_one_through_ten():
    multiplier = Multiplier()
    numbers = range(2, 21)
    factors = range(1, 11)
    
    for number in numbers:
        for factor in factors:
            result = number * factor
            assert f"{number} x {factor} = {result}" in multiplier.multiply_number_by_one_to_ten(number)

    assert "2 x 2 = 4" in multiplier.multiply_number_by_one_to_ten(2)
    assert "2 x 3 = 6" in multiplier.multiply_number_by_one_to_ten(2)
    assert "3 x 1 = 3" in multiplier.multiply_number_by_one_to_ten(3)
    assert "3 x 2 = 6" in multiplier.multiply_number_by_one_to_ten(3)
    assert "3 x 3 = 9" in multiplier.multiply_number_by_one_to_ten(3)
    assert "20 x 1 = 20" in multiplier.multiply_number_by_one_to_ten(20)
    assert "20 x 9 = 180" in multiplier.multiply_number_by_one_to_ten(20)
    assert "20 x 10 = 200" in multiplier.multiply_number_by_one_to_ten(20)
    assert "Number outside valid range." in multiplier.multiply_number_by_one_to_ten(21)
    