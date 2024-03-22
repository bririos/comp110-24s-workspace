"""Test my EX05 functions."""
__author__ = "730576067"

import pytest
from exercises.ex05.dictionary import invert


from exercises.ex05.dictionary import count


from exercises.ex05.dictionary import favorite_color


from exercises.ex05.dictionary import alphabetizer


from exercises.ex05.dictionary import update_attendance


def test_invert_input1() -> None:
    """This is a use cases."""
    keys: dict[str, str] = {"x": "a", "d": "e"}
    assert invert(keys) == {"a": "x", "e": "d"}


def test_invert_input2() -> None:
    """This is a use cases."""
    with pytest.raises(KeyError):
        keys: dict[str, str] = {"x": "a", "s": "a"}
        invert(keys)
    

def test_invert_empty() -> None:
    """This is an edge case."""
    keys: dict[str, str] = {}
    assert invert(keys) == {}


def test_favorite_color1() -> None:
    """Testing regular input."""
    names: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(names) == "blue"


def test_favorite_color2() -> None:
    """Testing regular input."""
    names: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Anna": "orange", "Hannah": "orange"}
    assert favorite_color(names) == "blue"
 

def test_favorite_color_empty() -> None:
    """Testing regular input."""
    names: dict[str, str] = {}
    assert favorite_color(names) == ""


def test_count_input1() -> None:
    """Testing regular input."""
    counting: list[str] = ["hi", "hello"]
    assert count(counting) == {"hi": 1, "hello": 1}


def test_count_input2() -> None:
    """Testing regular input."""
    counting: list[str] = ["hi", "hello", "hello"]
    assert count(counting) == {"hi": 1, "hello": 2}


def test_count_input_empty() -> None:
    """Testing regular input."""
    counting: list[str] = []
    assert count(counting) == {}


def test_alphabetizer1() -> None:
    """Testing regular inputs."""
    alpha: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(alpha) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer2() -> None:
    """Testing regular inputs."""
    alpha: list[str] = ["cat", "apple", "cat", "boy", "angry", "bad", "car"]
    assert alphabetizer(alpha) == {'c': ['cat', 'cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_empty() -> None:
    """Testing regular inputs."""
    alpha: list[str] = []
    assert alphabetizer(alpha) == {}


def test_update_attendance1() -> None:
    """Test use case."""
    week: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Monday"
    student: str = "Anna"
    result: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb", "Anna"], "Tuesday": ["Alyssa"]}
    update_attendance(week, day, student)
    assert (week) == result


def test_update_attendance2() -> None:
    """Test use case."""
    week: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Monday"
    student: str = "Kaleb"
    result: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(week, day, student)
    assert (week) == result 
   

def test_update_attendance_empty() -> None:
    """Test use case."""
    week: dict[str, list[str]] = {}
    day: str = ""
    student: str = ""
    result: dict[str, list[str]] = {"": [""]}
    update_attendance(week, day, student)
    assert (week) == result