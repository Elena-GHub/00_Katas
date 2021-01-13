class CharacterSeparator:
    
    def check_length(self, string):
        result = len(string)
        if 2 <= result <= 10000:
            return True 
        return False