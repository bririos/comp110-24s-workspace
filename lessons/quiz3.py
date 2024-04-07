"""quiz 3 practice."""

def find_even(words: list[str]) -> str:
    idx: int = 0
    while idx < len(words):
        if len(words[idx]) % 2 == 0:
            return words[idx]
        idx += 1
    return ""


words: list[str] = []
print(find_even(words))

def remove_first_even(words: list[str]) -> None:
    idx: int = 0
    condition: bool = True
    while (idx < len(words)) and condition:
        if len(words[idx]) % 2 == 0:
            words.pop(idx)
            condition = False
        idx += 1


def random_descending_list(n: int) -> list[int]:
    """Generate a list of random descending integers."""
    new_list: list[int] = []
    value: int = randint (MAX_VAL,n)
    #n[len(new_list)-1]
    i: int = 1
    new_list[0] = MAX_VAL
    while i < n:
        #we want to append a value between MAX_Value and n
        new_list.append(value)
        i += 1
    return new_list

