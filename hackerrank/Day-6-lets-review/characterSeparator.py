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