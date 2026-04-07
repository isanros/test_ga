"""String utility functions for demonstrating unit tests with GitHub Actions."""


def reverse(s: str) -> str:
    """Return the reversed string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Return True if the string is a palindrome (case-insensitive)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_words(s: str) -> int:
    """Return the number of words in a string."""
    if not s.strip():
        return 0
    return len(s.split())


def capitalize_words(s: str) -> str:
    """Return the string with each word capitalized."""
    return " ".join(word.capitalize() for word in s.split())


def truncate(s: str, max_length: int, suffix: str = "...") -> str:
    """Truncate a string to max_length characters, appending suffix if truncated.

    Raises:
        ValueError: If max_length is negative.
    """
    if max_length < 0:
        raise ValueError("max_length must be a non-negative integer.")
    if len(s) <= max_length:
        return s
    return s[:max_length] + suffix
