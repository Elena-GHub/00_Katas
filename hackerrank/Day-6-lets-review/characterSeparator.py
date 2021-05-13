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

    def split_characters(self, string):
        odd_characters = ""
        even_characters = ""

        for letter in range(len(string)):
            if letter % 2 != 0:
                odd_characters = odd_characters + string[letter]
            else:
                even_characters = even_characters + string[letter]

        processed_string = even_characters + " " + odd_characters 
        return processed_string

    def format_inputs_to_string(self, user_list):
        array_separator = "\n"
        formatted_inputs = array_separator.join(map(str, user_list))
        return formatted_inputs

    def split_user_inputs(self, number):
        number = int(input("How many strings do you want to process? \n (Please enter a number between 1 and 10) "))

        if self.check_number_of_testcases(number):
            user_strings = []
            for i in range(1, number + 1):
                string = input()
                if self.check_string_length(string):
                    user_strings.append(string)
        raw_inputs = [self.split_characters(item) for item in user_strings]
        final_output = self.format_inputs_to_string(raw_inputs)
        print(final_output)


""" comment all the lines below to run the tests.
Uncomment them to run this file and see the class working in the terminal """

characterSeparator = CharacterSeparator()
characterSeparator.split_user_inputs(2)
