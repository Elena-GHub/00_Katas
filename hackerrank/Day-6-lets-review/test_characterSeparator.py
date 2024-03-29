# problem running with pytest
# Run in terminal with
# python3 -m unittest test_characterSeparator.py

from characterSeparator import CharacterSeparator

def test_input_string_is_in_valid_length_range():
    string = "Hello"
    characterSeparator = CharacterSeparator()
    assert characterSeparator.check_string_length(string) == True

def test_number_of_testcases():
    characterSeparator = CharacterSeparator()
    assert characterSeparator.check_number_of_testcases(2) == True
    assert characterSeparator.check_number_of_testcases(11) == False
    assert characterSeparator.check_number_of_testcases(0) == False
    assert characterSeparator.check_number_of_testcases("a") == False

def test_characters_splitting_into_odd_and_even_indexed_characters():
    characterSeparator = CharacterSeparator()
    string = "Hello"
    assert characterSeparator.split_characters(string) == "Hlo el"
