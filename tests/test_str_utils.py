import pytest

from ie_titanic_utils.str_utils import extract_title


def test_extract_title_returns_expected_title():
    input_str = "Mr. John Doe"
    expected_title = "Mr"

    title = extract_title(input_str)

    assert title == expected_title


def test_empty_separator_raises_error():
    with pytest.raises(ValueError, match="Separator cannot be empty"):
        extract_title("...", "")


@pytest.mark.parametrize("separator", list(".:;-Ñ"))
def test_separator_works_as_expected(separator):

    expected_title = "Mr"
    input_str = "Mr" + separator + " John Doe"

    title = extract_title(input_str, separator=separator)

    assert title == expected_title
