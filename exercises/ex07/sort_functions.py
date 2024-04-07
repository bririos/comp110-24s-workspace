"""Functions that implement sorting algorithms."""

__author__ = "730576067"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    sorted: int = 0
    unsorted: int = 0
    while sorted <= len(x)-1:
        unsorted= sorted 
        while unsorted > 0 and x[unsorted] < x[unsorted-1]:
            temp: int = x[unsorted]
            x[unsorted] = x[unsorted-1]
            x[unsorted-1] = temp
            unsorted -= 1
        sorted += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx1: int = 0
    idx2: int = 0
    min_value: int = idx1
    while idx1 < len(x):
        min_value = idx1
        idx2 = idx1
        while idx2 < len(x):
            if x[idx2] < x[min_value]:
                min_value = idx2
            idx2 += 1
        temp: int = x[min_value]
        x[min_value] = x[idx1]
        x[idx1] = temp
        idx1 += 1
    return None

    