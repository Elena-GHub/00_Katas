class StringCalculator:

    def convert_arbitrary_length_separator_to_single_comma(self, string):
        string = string.replace('\n', '')
        string = string.replace('//', '')
        while ']' in string:
            separator = string[string.find("[")+1:string.find("]")]
            string = string.replace(separator, ',')
            string = string[3:]
        return string

    def look_for_negative_numbers(self, string):
        separator = ' '
        message = 'error: negatives not allowed: '
        negative_numbers = [x for x in list(string.split(',')) if int(x) < 0 ]
        return message + separator.join(negative_numbers)
    
    def add(self, string):
        result = 0

        if not string:
            return result
        if string.startswith('//['):
           string = self.convert_arbitrary_length_separator_to_single_comma(string)
        if '\n' in string:
            string = string.replace('\n', ',')
        if string.startswith('//'):
            string = string.replace(string[2:3], ',')
            string = string[4:]
        if '-' in string:
           return self.look_for_negative_numbers(string)
        numbers = list(string.split(','))
        integers = map(int, numbers)
        integers = list(filter(lambda x : x <= 1000, integers))
        result = sum(integers)
        return result
