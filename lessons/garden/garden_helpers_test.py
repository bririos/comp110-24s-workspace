"""Test my garden functions."""
__author__ = "730576067"


from lessons.garden.garden_helpers import add_by_kind


from lessons.garden.garden_helpers import add_by_date


from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_input() -> None:
    #typical
    """Tests when adding a new plan kind and new plant."""
    by_kind: dict[str, list[str]]= {"flower": ["daisy"], "vegetable": ["carrots"]}
    new_plant_kind: str = "Tree"
    new_plant: str = "pine tree"
    test: dict[str, list[str]] = {"flower": ["daisy"], "vegetable": ["carrots"], "Tree": ["pine tree"]}
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert (by_kind) == test


def test_add_by_kind() -> None:
    #not typical
    """Tests when the dictionary is empty at the begining."""
    by_kind: dict[str, list[str]]= {}
    new_plant_kind: str = "Tree"
    new_plant: str = "pine tree"
    test: dict[str, list[str]] = {"Tree": ["pine tree"]}
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert (by_kind) == test



def test_add_by_date_input() -> None:
    #typical
    """Tests when appending a new month."""
    garden_by_date: dict[str, list[str]] = {"January": ["marigold"], "July": ["carrots"]}
    month: str = "January"
    plant: str = "roses"
    result: dict[str, list[str]] = {"January": ["marigold","roses"], "July": ["carrots"]}
    add_by_date(garden_by_date, month, plant)
    assert garden_by_date == result


def test_add_by_date() -> None:
    #not typical
    """Tests when the dictionary is empty and appending a month with a plant kind."""
    garden_by_date: dict[str, list[str]] = {}
    month: str = "January"
    plant: str = "roses"
    result: dict[str, list[str]] = {"January":["roses"]}
    add_by_date(garden_by_date, month, plant)
    assert garden_by_date == result





def test_lookup_by_kind_and_date_input() -> None:
    #typical
    """"Testing input in dictionary."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    plants_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    kind: str = "flower"
    month: str = "January"
    lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month)
    result: str = "flowers to plant in April: ['marigold']"
    assert (plants_by_kind, plants_by_date) == result


def test_lookup_by_kind_and_date() -> None:
    #not typical
    """Adding a neww kind."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    plants_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    kind: str = "Tree"
    month: str = "January"
    lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month)
    result: str = ""
    assert (plants_by_kind,plants_by_date) == result
