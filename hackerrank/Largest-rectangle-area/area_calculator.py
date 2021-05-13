# https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues


#!/bin/python3

class AreaCalculator:
    
    def get_rectangle_list(self, array, blocks):

        if array == []:
            return
        else:
            blocks.append(array)
            lowest_height = array.index(min(array))
            self.get_rectangle_list(array[:lowest_height], blocks)
            self.get_rectangle_list(array[lowest_height + 1:], blocks)

    def calculate_rectangle_area(self, array):
        areas = []
        for sublist in array:
            areas.append(min(sublist) * len(sublist))

        return max(areas)

    def get_largest_rectangle_area(self, array, blocks):
        self.get_rectangle_list(array, blocks)
        return self.calculate_rectangle_area(blocks)
