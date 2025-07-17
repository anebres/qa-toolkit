# Automated test cases using pytest
# import pytest
from test_utils import assert_equal, has_duplicates, find_empty_fields

# def test_assert_equal():
#     assert assert_equal("a", "a") == "PASS"
#     assert assert_equal("a", "b") == "FAIL: Expected a, got b"

def test_assert_equal():
    assert_equal("a", "a")
    try:
        assert_equal("a", "b")
    except AssertionError as e:
        assert str(e) == "Expected a, got b"

def test_has_duplicates():
    assert has_duplicates(["a", "b", "a"]) is True
    assert has_duplicates(["x", "y", "z"]) is False

def test_find_empty_fields():
    form = {"name": "", "email": "test@example.com", "age": "  "}
    assert find_empty_fields(form) == ["name", "age"]