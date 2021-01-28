from reverter import Reverter

def test_list_elements_are_reversed():
    input_length = 4
    input = "1 2 3 4"
    
    reverter = Reverter()
    assert reverter.revert_list(input_length, input) == "4 3 2 1"


def test_list_length_is_valid():
    input_true = 4
    input_false = 1002

    reverter = Reverter()
    assert reverter.validate_list_length(input_true) == True
    assert reverter.validate_list_length(input_false) == False

def test_list_values_are_valid():
    valid_items = "1 2 3 4"
    invalid_items = "10002 2 3"

    reverter = Reverter()
    assert reverter.validate_list_values(valid_items) == True
    assert reverter.validate_list_values(invalid_items) == False
