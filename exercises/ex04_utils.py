"""Functions."""
__author__ = "730576067"


def all(arg: list[int], arg2: int) -> bool:
    """Checks all element to be equal to the arg2."""
    i: int = 0
    if len(arg) <= 0:
        return False
    while i < len(arg):
        if arg[i] != arg2:
            return False
        else:
            i += 1
    return True


def max(arg: list[int]) -> int:
    """Checks for the max number."""
    if len(arg) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_value = arg[0]
    while i < len(arg):
        if arg[i] > max_value:
            max_value = arg[i]
        i += 1     
    return max_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if the list1 equals list2."""
    if list1 == list2:
        return True
    if list1 != list2:
        return False
    return True
    

def extend(list1: list[int], list2: list[int]) -> None:
    """Adds a list."""
    list1.extend(list2)
    return (None)

