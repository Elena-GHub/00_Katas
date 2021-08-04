class StringCalculator:
    def add(self, string):
        result = 0

        if not string:
            return result
        if string.startswith('//['):
            string = string.replace('\n', '')
            ending_index = string.index(']')
            string = string.replace(string[3:ending_index], ',')
            string = string[5:]
        if '\n' in string:
            string = string.replace('\n', ',')
        if string.startswith('//'):
            string = string.replace(string[2:3], ',')
            string = string[4:]
        if '-' in string:
            separator = ' '
            message = 'error: negatives not allowed: '
            negative_numbers = [x for x in list(string.split(',')) if int(x) < 0 ]
            return message + separator.join(negative_numbers)
        numbers = list(string.split(','))
        integers = map(int, numbers)
        integers = list(filter(lambda x : x <= 1000, integers))
        result = sum(integers)
        return result