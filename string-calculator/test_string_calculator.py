from string_calculator import StringCalculator

def test_empty_string_should_return_zero():
    string = ''
    calculator = StringCalculator()
    assert calculator.add(string) == 0

def test_single_number_should_return_same_input_number():
    string = '4'
    calculator = StringCalculator()
    assert calculator.add(string) == 4

def test_two_numbers_should_return_their_sum():
    string = '1,2'
    calculator = StringCalculator()
    assert calculator.add(string) == 3

def test_more_than_two_numbers_should_return_their_sum():
    string = '1,2,3,4,5,6,7,8,9'
    calculator = StringCalculator()
    assert calculator.add(string) == 45

def test_input_with_newline_separator_should_return_their_sum():
    string = '1\n2,3'
    calculator = StringCalculator()
    assert calculator.add(string) == 6
    
def test_input_with_custom_separator_should_return_their_sum():
    string = '//;\n1;2'
    second_string = '//*\n1*2'

    calculator = StringCalculator()
    assert calculator.add(string) == 3
    assert calculator.add(second_string) == 3

def test_input_with_negative_number_should_return_error_message():
    string = '1,-2,-3'
    message = 'error: negatives not allowed: '

    calculator = StringCalculator()
    assert calculator.add(string) == message + '-2 -3'

def test_input_with_number_over_one_thousand_should_be_ignored_in_the_sum():
    string = '1001, 2'

    calculator = StringCalculator()
    assert calculator.add(string) == 2

def test_input_with_arbitrary_length_separators_should_return_their_sum():
    string = "//[***]\n1***2***3"

    calculator = StringCalculator()
    assert calculator.add(string) == 6

def test_input_with_multiple_single_length_separator_should_return_their_sum():
    string = "//[*][%]\n1*2%3"

    calculator = StringCalculator()
    assert calculator.add(string) == 6

def test_input_with_multiple_separators_with_any_character_length_should_return_their_sum():
    string = "//[foo][bar]\n1foo2bar3"

    calculator = StringCalculator()
    assert calculator.add(string) == 6
