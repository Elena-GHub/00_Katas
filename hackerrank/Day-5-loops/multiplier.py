class Multiplier:

    def multiply_number_by_one_to_ten(self, number):
        if self.check_number_is_in_range(number):
            list_of_results = []
            separator = "\n"
            for index in range(1, 11):
                result = number * index
                list_of_results.append(f"{number} x {index} = {result}")
            formatted_list = separator.join(map(str, list_of_results))
            return(formatted_list)
        return "Number outside valid range."
    
    def check_number_is_in_range(self, number):
        minimum_value = 2
        maximum_value = 20
        if minimum_value <= number <= maximum_value:
            return True
        return False
   