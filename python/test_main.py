# pylint: disable=F0401,E0611
"""
Tests for the Gamer Project
"""

# todo:
# jewel test
# equipment test
# PassiveBoost test (with a real owner)

# from random import randrange

from functions.levels import getexp, getlvl
from items import ITEMS, JEWELS, EQUIPMENTS
from classes.item import Item
from classes.potion import Potion
from classes.skills import PassiveBoost


def test_getexp():
    """Tests the getexp function"""
    lvl = 5
    # 1^3 = 1
    # 2^3 = 8
    # 3^3 = 27
    # 4^3 = 64
    # 5^3 = 125
    # 1+8+27+64+125 = 225
    real_exp = 225
    assert real_exp == getexp(lvl)


    assert getexp(0) == 0
    assert getexp(1) == 1
    assert getexp(2) == 9
    assert getexp(3) == 36
    assert getexp(4) == 100


def test_getlvl():
    """Tests the getlvl function"""
    explvl2 = 9
    explvl3 = 36
    explvl4 = 100
    explvl5 = 225

    assert getlvl(explvl2) == 2
    assert getlvl(explvl2-1) == 1
    assert getlvl(explvl2+1) == 2
    assert getlvl(explvl3) == 3
    assert getlvl(explvl3-1) == 2
    assert getlvl(explvl3+1) == 3
    assert getlvl(explvl4) == 4
    assert getlvl(explvl4-1) == 3
    assert getlvl(explvl4+1) == 4
    assert getlvl(explvl5) == 5
    assert getlvl(explvl5-1) == 4
    assert getlvl(explvl5+1) == 5

    # can be level 0, but level ups with 1 exp
    assert getlvl(0) == 0
    assert getlvl(-1) == 0
    assert getlvl(1) == 1

# items lists


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

# items instances


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


def test_jewel_item():
    """Tests for items that are jewels"""
    src = {
        "name": "jewel",
        "lore": "item that can be inserted",
        "lvl": 5,
        "weight": 2,
        "stats": {
            "str": 1, "dex": 2, "vit": 3,
            "int": 4, "wis": 5, "luk": 6
        }
    }
    jewel = Item(src, jewel=True)

# todo finish test


def test_potion_object():
    """Tests the Potion class."""
    potion = Potion(2)
    assert potion.itemtype == "potion"
    assert potion.potiontype == "life"
    assert potion.regen == 400

    i = potion.infos
    assert i["name"] == "Life Potion lvl 2"
    assert i["lore"] == "A magic beverage that instantly regenerates " \
        "your life from 400 points."
    assert i["lvl"] == 2
    assert i["weight"] == 0.1

    mpotion = Potion(3, "Mana")
    assert mpotion.itemtype == "potion"
    assert mpotion.potiontype == "mana"
    assert mpotion.regen == 600

    i = mpotion.infos
    assert i["name"] == "Mana Potion lvl 3"
    assert i["lore"] == "A magic beverage that instantly regenerates " \
        "your mana from 600 points."
    assert i["lvl"] == 3
    assert i["weight"] == 0.1


def test_passiveboost():
    """Tests the PassiveBoost class."""
    stats = ("str", "dex", "vit")
    boosts = (10, 10, 20)
    # owner should not be None, but entities are still not made
    boost = PassiveBoost(stats, boosts, owner=None)
