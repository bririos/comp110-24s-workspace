"""Splitting a dictionary into two lists."""
__author__ = "730576067"


def get_keys(keys: dict[str, int]) -> list[str]:
    """Functions that returns a list of words."""
    list1: list[str] = []
    if keys == {}:
        return list1
    for key in keys:
        list1.append(key)
    return (list1)

 
def get_values(values: dict[str, int]) -> list[int]:
    """Functions returns num."""
    list1: list[int] = []
    if values == {}:
        return list1
    for elem in values:
        list1.append(values[elem])
    return (list1)