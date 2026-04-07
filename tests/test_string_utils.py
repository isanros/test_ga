"""Unit tests for the string_utils module."""
import pytest

from src.string_utils import reverse, is_palindrome, count_words, capitalize_words, truncate


class TestReverse:
    def test_reverse_normal_string(self):
        assert reverse("hello") == "olleh"

    def test_reverse_empty_string(self):
        assert reverse("") == ""

    def test_reverse_single_char(self):
        assert reverse("a") == "a"

    def test_reverse_palindrome(self):
        assert reverse("racecar") == "racecar"


class TestIsPalindrome:
    def test_palindrome_word(self):
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_palindrome_with_spaces(self):
        assert is_palindrome("a man a plan a canal panama") is True

    def test_case_insensitive(self):
        assert is_palindrome("Racecar") is True

    def test_single_character(self):
        assert is_palindrome("a") is True


class TestCountWords:
    def test_count_regular_sentence(self):
        assert count_words("hello world") == 2

    def test_count_empty_string(self):
        assert count_words("") == 0

    def test_count_single_word(self):
        assert count_words("hello") == 1

    def test_count_whitespace_only(self):
        assert count_words("   ") == 0

    def test_count_multiple_spaces(self):
        assert count_words("one  two  three") == 3


class TestCapitalizeWords:
    def test_capitalize_lowercase(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_capitalize_already_capitalized(self):
        assert capitalize_words("Hello World") == "Hello World"

    def test_capitalize_mixed_case(self):
        assert capitalize_words("hElLo wOrLd") == "Hello World"

    def test_capitalize_single_word(self):
        assert capitalize_words("python") == "Python"


class TestTruncate:
    def test_truncate_long_string(self):
        assert truncate("Hello, World!", 5) == "Hello..."

    def test_truncate_exact_length(self):
        assert truncate("Hello", 5) == "Hello"

    def test_truncate_short_string(self):
        assert truncate("Hi", 10) == "Hi"

    def test_truncate_custom_suffix(self):
        assert truncate("Hello, World!", 5, suffix="~") == "Hello~"

    def test_truncate_zero_length(self):
        assert truncate("Hello", 0) == "..."

    def test_truncate_negative_length_raises(self):
        with pytest.raises(ValueError, match="max_length must be a non-negative integer."):
            truncate("Hello", -1)
