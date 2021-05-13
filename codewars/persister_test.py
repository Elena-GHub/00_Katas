from persister import Persister


def test_persistence():
    persister = Persister()
    assert persister.get_product_count_until_number_is_one_digit(39) == 3
    assert persister.get_product_count_until_number_is_one_digit(4) == 0
    assert persister.get_product_count_until_number_is_one_digit(25) == 2
    assert persister.get_product_count_until_number_is_one_digit(999) == 4
