"""Mutating functions."""
__author__ = "730576067"


def manual_append(lists: list[int], num: int) -> None:
    """Adds a word."""
    lists.append(num)
    return (None)


def double(list2: list[int]) -> None:
    """Doubles a lists idx by idx."""
    i: int = 0
    while i < len(list2):
        list2[i] *= 2
        i += 1
    return (None)

   