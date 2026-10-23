# tests/test_z1.py
import pytest

from Zadania.z_1.module import make_extremum


def test_make_max_returns_max_function():
    f_max = make_extremum()
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    assert f_max(data) == 9


def test_make_min_returns_min_function():
    f_min = make_extremum("min")
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    assert f_min(data) == 1


def test_make_extremum_with_negative_numbers():
    f_max = make_extremum("max")
    f_min = make_extremum("min")
    data = [-10, -5, -20, -1]

    assert f_max(data) == -1
    assert f_min(data) == -20


def test_make_extremum_with_single_element():
    f_max = make_extremum()
    assert f_max([42]) == 42


def test_make_extremum_with_empty_list():
    f_max = make_extremum()

    with pytest.raises(ValueError):
        f_max([])


def test_make_extremum_with_strings():
    f_max = make_extremum("max")
    data = ["apple", "banana", "cherry"]
    assert f_max(data) == "cherry"