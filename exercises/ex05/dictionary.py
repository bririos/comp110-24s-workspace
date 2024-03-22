"""Practice with dictionary functions."""
__author__ = "730576067"


def invert(keys: dict[str, str]) -> dict[str, str]:
    """Inverts the key and value."""
    empty: dict[str, str] = {}
    for key in keys:
        if keys[key] in empty:
            raise KeyError("error message of your choice here!")
        val = keys[key]
        empty[val] = key
    return empty

    
def favorite_color(names: dict[str, str]) -> str:
    """Prints out the top showed up color."""
    colors: dict[str, int] = {}
    for name in names:
        colors[names[name]] = 0
    
    for name in names:
        colors[names[name]] += 1
    
    color_max: str = ""
    for color in colors:
        if color_max == "":
            color_max = color
        if colors[color] > colors[color_max]:
            color_max = color
    return color_max


def count(counting: list[str]) -> dict[str, int]:
    """Counts the numbers."""
    empty_dict: dict[str, int] = {}
    for item in counting:
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1
    return empty_dict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Groups together a list of words."""
    empty_words: dict[str, list[str]] = {}
    for word in list1:
        first_letter = word[0].lower()
        if first_letter in empty_words:
            empty_words[first_letter].append(word)
        else:
            empty_words[first_letter] = [word]
    return empty_words   


def update_attendance(week: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the list."""
    if day in week:
        if (student not in week[day]):
            week[day].append(student)
    else:
        week[day] = [student]
    return None    