import check_for_factor

def test_should_return_true():
    assert check_for_factor.check_for_factor(10, 2) == True
    assert check_for_factor.check_for_factor(63, 7) == True
    assert check_for_factor.check_for_factor(2450, 5) == True
    assert check_for_factor.check_for_factor(24612, 3) == True


