from collections import Counter

class Finder:
    
    def find_integer_with_odd_occurences(self, seq):
        # Given an array of integers, find the one that appears an odd number of times.
        # There will always be only one integer that appears an odd number of times.
        
        seq_counter = Counter(seq)
        key_list = list(seq_counter.keys())
        val_list = list(seq_counter.values())
        for value in val_list:
            if value % 2 != 0:
                return key_list[val_list.index(value)]
