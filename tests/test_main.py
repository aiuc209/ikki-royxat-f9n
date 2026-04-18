import pytest

def power_numbers(numbers, exponents):
    return [n ** e for n, e in zip(numbers, exponents)]

def test_power_numbers():
    numbers = [2, 3, 4]
    exponents = [2, 3, 4]
    expected_result = [4, 27, 256]
    assert power_numbers(numbers, exponents) == expected_result

def test_power_numbers_empty_lists():
    numbers = []
    exponents = []
    expected_result = []
    assert power_numbers(numbers, exponents) == expected_result

def test_power_numbers_different_length_lists():
    numbers = [2, 3, 4]
    exponents = [2, 3]
    with pytest.raises(ValueError):
        power_numbers(numbers, exponents)

def test_power_numbers_negative_exponents():
    numbers = [2, 3, 4]
    exponents = [-2, -3, -4]
    expected_result = [0.25, 0.03703703703703704, 0.00390625]
    assert power_numbers(numbers, exponents) == pytest.approx(expected_result)

def test_power_numbers_zero_exponents():
    numbers = [2, 3, 4]
    exponents = [0, 0, 0]
    expected_result = [1, 1, 1]
    assert power_numbers(numbers, exponents) == expected_result
