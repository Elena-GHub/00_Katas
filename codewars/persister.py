# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python


from functools import reduce

class Persister:

    def get_product_count_until_number_is_one_digit(self, number):
        prod_count = 0
        product_result = 1
        
        while number > 9:
            string = str(number)
            for i in string:
                operator = int(i)
                product_result *= operator
            prod_count += 1
            number = product_result
            product_result = 1
        
        return prod_count
