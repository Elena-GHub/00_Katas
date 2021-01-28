class Reverter:

    def validate_list_length(self, length):
        if 0 < length < 1001:
            return True
        return False

    def validate_list_values(self, series):
        list_series = list(series.rstrip().split())
        numbers = [int(item) for item in list_series]

        for number in numbers:
            if 0 < number < 10001:
                return True
            return False
    
    def revert_list(self, length, series):
        if self.validate_list_length(length) and self.validate_list_values(series):
            reversed_series = series[::-1]
            output = ''.join(str(item) for item in reversed_series)
            return output     
