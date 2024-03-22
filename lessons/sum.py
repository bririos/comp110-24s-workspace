"""Summing the elements of a list using different loops."""
__author__ = "730576067"


def w_sum(vals: list[float]) -> float:
    """Sums values with while loop."""
    i: int = 0
    sum_elements = 0.0
    while i < len(vals):
        sum_elements += vals[i]
        i += 1
    return sum_elements


def f_sum(vals: list[float]) -> float:
    """Using for in loop sumation."""
    sum_of_elements: float = 0.0
    for i in vals:
        sum_of_elements = sum_of_elements + i
    return sum_of_elements


def f_range_sum(vals: list[float]) -> float:
    """Using for in range loop."""
    sum_of_elem: float = 0.0
    for i in range(len(vals)):
        sum_of_elem = sum_of_elem + vals[i]
    return sum_of_elem