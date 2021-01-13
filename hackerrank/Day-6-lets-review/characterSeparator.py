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

        return even_characters + " " + odd_characters