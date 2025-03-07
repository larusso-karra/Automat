import pytest
from StringUtils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


# Тесты для метода capitilize
def test_capitilize_positive_case(string_utils):
    assert string_utils.capitilize("skypro") == "Skypro"

def test_capitilize_negative_type_error_with_list(string_utils): 
    with pytest.raises(TypeError): string_utils.capitilize(["not", "a", "string"])

def test_capitilize_empty_string(string_utils):
    assert string_utils.capitilize("") == ""


def test_capitilize_single_char(string_utils):
    assert string_utils.capitilize("s") == "S"


# Тесты для метода trim
def test_trim_positive_case(string_utils):
    assert string_utils.trim("   skypro") == "skypro"


def test_trim_no_leading_spaces(string_utils):
    assert string_utils.trim("skypro") == "skypro"


def test_trim_only_spaces(string_utils):
    assert string_utils.trim("     ") == ""


# Тесты для метода to_list
def test_to_list_default_delimiter(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]


def test_to_list_custom_delimiter(string_utils):
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]


def test_to_list_empty_string(string_utils):
    assert string_utils.to_list("") == []


# Тесты для метода contains
def test_contains_true_case(string_utils):
    assert string_utils.contains("SkyPro", "S")


def test_contains_false_case(string_utils):
    assert not string_utils.contains("SkyPro", "U")


def test_contains_empty_string(string_utils):
    with pytest.raises(ValueError):
        string_utils.contains("", "A")


# Тесты для метода delete_symbol
def test_delete_symbol_successfully(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_not_found(string_utils):
    assert string_utils.delete_symbol("SkyPro", "Z") == "SkyPro"


def test_delete_symbol_empty_string(string_utils):
    assert string_utils.delete_symbol("", "A") == ""

def test_delete_symbol_multiple_occurrences(string_utils):
    assert string_utils.delete_symbol("hellohello", "l") == "heoheo"

# Тесты для метода starts_with
def test_starts_with_true_case(string_utils):
    assert string_utils.starts_with("SkyPro", "S")


def test_starts_with_false_case(string_utils):
    assert not string_utils.starts_with("SkyPro", "P")


def test_starts_with_empty_string(string_utils):
    assert not string_utils.starts_with("", "A")

@pytest.fixture
def string_utils():
    return StringUtils()


# Тесты для метода end_with
def test_end_with_positive_case(string_utils):
    assert string_utils.end_with("SkyPro", "o")


def test_end_with_negative_case(string_utils):
    assert not string_utils.end_with("SkyPro", "y")


def test_end_with_empty_string(string_utils):
    assert not string_utils.end_with("", "A")


# Тесты для метода is_empty
def test_is_empty_positive_case(string_utils):
    assert string_utils.is_empty("")


def test_is_empty_whitespace_only(string_utils):
    assert string_utils.is_empty(" ")


def test_is_empty_non_empty_string(string_utils):
    assert not string_utils.is_empty("SkyPro")


# Тесты для метода list_to_string
def test_list_to_string_default_joiner(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"


def test_list_to_string_custom_joiner(string_utils):
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"


def test_list_to_string_empty_list(string_utils):
    assert string_utils.list_to_string([]) == ""
