import app.main as main


def test_check_zeros_arguments() -> None:
    assert main.get_human_age(0, 0) == [0, 0], \
        "Result should be 0"


def test_limit_of_the_first_threshold() -> None:
    assert main.get_human_age(14, 14) == [0, 0], \
        "Result should be 0, because the threshold is less than 15"


def test_first_threshold_reached() -> None:
    assert main.get_human_age(15, 15) == [1, 1], \
        "Result should be 1, because the first threshold reached"


def test_before_second_threshold() -> None:
    assert main.get_human_age(23, 23) == [1, 1], \
        "Result should be 1, because the first threshold must be =>15 and <=23"


def test_second_threshold_reached() -> None:
    assert main.get_human_age(24, 24) == [2, 2], \
        "Result should be 2, because the second threshold reached"


def test_before_third_threshold() -> None:
    assert main.get_human_age(27, 28) == [2, 2], \
        "Result should be 2, because third threshold not reached yet"


def test_third_threshold_for_cat() -> None:
    assert main.get_human_age(28, 28) == [3, 2], \
        "Cat gets +1 every 4 years, dog every 5 years after second threshold"


def test_third_threshold_for_dog() -> None:
    assert main.get_human_age(28, 29) == [3, 3], \
        "Dog gets +1 every 5 years, cat every 4 years after second threshold"


def test_big_values() -> None:
    assert main.get_human_age(100, 100) == [21, 17], \
        "Result should correctly convert large cat and dog ages to human years"
