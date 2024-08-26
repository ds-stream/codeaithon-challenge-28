import pytest


def test_single_word(solution):
    assert solution.reverse_substrings("hello") == "olleh"


def test_multiple_words(solution):
    assert solution.reverse_substrings("hello world") == "olleh dlrow"


def test_empty_string(solution):
    assert solution.reverse_substrings("") == ""


def test_palindrome_words(solution):
    assert solution.reverse_substrings("madam racecar level") == "madam racecar level"


def test_sentence_with_punctuation(solution):
    assert solution.reverse_substrings("hello, world!") == ",olleh !dlrow"


def test_spaces_between_words(solution):
    assert solution.reverse_substrings("  hello   world  ") == "  olleh   dlrow  "


def test_single_character_words(solution):
    assert solution.reverse_substrings("a b c") == "a b c"
