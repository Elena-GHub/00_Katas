from characterSeparator import CharacterSeparator

# def test_whatever():
    # f = classname()
    # assert f.say(result) == 'expected value'

def test_input_string_is_in_valid_length_range():
    string = "Hello"
    characterSeparator = CharacterSeparator()
    assert characterSeparator.check_string_length(string) == True