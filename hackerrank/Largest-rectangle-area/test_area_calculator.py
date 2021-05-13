from area_calculator import AreaCalculator

def test_ascending_list_till_five_should_return_nine():
    array = [1, 2, 3, 4, 5]
    blocks = []
    area_calculator = AreaCalculator()
    assert area_calculator.get_largest_rectangle_area(array, blocks) == 9

def test_minimum_value_in_middle_should_return_six():
    array = [3, 2, 1, 3, 4]
    blocks = []
    area_calculator = AreaCalculator()
    assert area_calculator.get_largest_rectangle_area(array, blocks) == 6

def test_two_subsequent_twos_in_seven_blocks_should_return_fourteen():
    array = [5, 4, 2, 2, 3, 4, 6]
    blocks = []
    area_calculator = AreaCalculator()
    assert area_calculator.get_largest_rectangle_area(array, blocks) == 14
