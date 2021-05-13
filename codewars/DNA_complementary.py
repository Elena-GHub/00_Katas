# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

class DNAcomplementary:

    def get_complementary_dna(self, dna):
        my_table = dna.maketrans("ATCG", "TAGC")
        return dna.translate(my_table)


#MY FIRST SOLUTION until I discovered the maketrans method
# def DNA_strand(dna):
#     complementary_dna = ""
    
#     for letter in dna:
#         if letter == "A":
#             complementary_dna += "T"
#         elif letter == "T":
#             complementary_dna += "A"
#         elif letter == "G":
#             complementary_dna += "C"
#         else:
#             complementary_dna += "G"
    
#     return complementary_dna
