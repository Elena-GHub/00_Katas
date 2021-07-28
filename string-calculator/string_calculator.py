class StringCalculator:
    def add(self, string):
        result = 0

        if not string:
            return result
        if '\n' in string:
            string = string.replace('\n', ',')
        if string.startswith('//'):
            string = string.replace(string[2:3], ',')
            string = string[4:]
        numbers = list(string.split(','))
        integers = map(int, numbers)
        result = sum(integers)
        return result