class CharacterSeparator:
    
    def check_string_length(self, string):
        result = len(string)
        if 2 <= result <= 10000:
            return True 
        return False

    def check_number_of_testcases(self, number):
        if type(number) != int:
            return False

        if number not in range(1, 11):
            return False
        return True

    def splitCharacters(self, string):
        odd_characters = ""
        even_characters = ""

        for letter in range(len(string)):
            if letter % 2 != 0:
                odd_characters = odd_characters + string[letter]
            else:
                even_characters = even_characters + string[letter]

        processed_string = even_characters + " " + odd_characters 
        # below line with return required to run the tests, not for hackerrank code submission
        return processed_string

""" comment all the lines below to run the tests.
Uncomment them to run this file and see the class working in the terminal """

number = int(input("How many strings do you want to process? \n (Please enter a number between 1 and 10) "))
characterSeparator = CharacterSeparator()
if characterSeparator.check_number_of_testcases(number):
    user_strings = []
    for i in range(1, number + 1):
        string = input()
        if characterSeparator.check_string_length(string):
            user_strings.append(string)
raw_inputs = [characterSeparator.splitCharacters(item) for item in user_strings]
array_separator = "\n"
formatted_inputs = array_separator.join(map(str, raw_inputs))
print(formatted_inputs)