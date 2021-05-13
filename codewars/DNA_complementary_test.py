from DNA_complementary import DNAcomplementary


def test_number_value_is_between_two_and_twenty():
    dna_complementary = DNAcomplementary()
    # pylint: disable=maybe-no-member
    assert dna_complementary.get_complementary_dna("AAAA") == "TTTT"
    assert dna_complementary.get_complementary_dna("ATTGC") == "TAACG"
    assert dna_complementary.get_complementary_dna("GTAT") == "CATA"
