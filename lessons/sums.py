"""Sum all elements in a list."""

def sum(elements: list[int]) -> None:
    """Sum all elements in elem."""
    total: int = 0
    for elem in elements:
        total += elem
    return total