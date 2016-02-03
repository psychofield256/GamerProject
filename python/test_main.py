# pylint: disable=F0401,E0611
"""
Tests for the Gamer Project
"""


from items import ITEMS, JEWELS, EQUIPMENTS
from classes.item import Item


def test_item_list():
    """Tests each dict of the item list (items.py)"""
    for item in ITEMS:
        assert isinstance(item["name"], str)
        assert isinstance(item["lore"], str)
        assert isinstance(item["lvl"], int)
        assert isinstance(item["weight"], int)


def test_jewel_list():
    """Tests each dict of the jewel list (items.py)"""
    for jewel in JEWELS:
        assert isinstance(jewel["name"], str)
        assert isinstance(jewel["lore"], str)
        assert isinstance(jewel["lvl"], int)
        assert isinstance(jewel["weight"], int)
        for stat in jewel["stats"].values():
            assert isinstance(stat, int)


def test_equipment_list():
    """Tests each dict of the equipment list (items.py)"""
    possible_slots = ["weapon", "helmet", "chestplate", "leggings", "boots"]
    for equip in EQUIPMENTS:
        assert isinstance(equip["name"], str)
        assert isinstance(equip["lore"], str)
        assert isinstance(equip["lvl"], int)
        assert isinstance(equip["weight"], int)
        assert equip["slot"] in possible_slots
        assert isinstance(equip["emptyslots"], int)
        for stat in equip["stats"].values():
            assert isinstance(stat, int)

def test_item_object():
    """Tests the Item class.
    Creates a dict for this, so it won't need items.py to be working"""

    src = {
        "name": "test",
        "lore": "description",
        "lvl": 4,
        "weight": 20,
    }

    item = Item(src)
    for info in ["name", "lore", "lvl", "weight"]:
        assert item.infos[info] == src[info]
    assert item.itemtype == "item"
    assert item.src == src
    assert not hasattr(item, "stats")
    assert item.saystats() is None
    # to be sure the item is stopping before making errors
    assert item.takestats(src) is None
    assert str(item) == "name: test\nlore: description\nlvl: 4\nweight: 20\n"

    item2 = Item(src)
    item2.name = "name"
    assert item == item2
