# pylint: disable=F0401,E0611
"""
Tests for the Gamer Project
"""

# todo:
# jewel test
# equipment test
# PassiveBoost test (with a real owner)

from random import randrange

from functions.levels import getexp, getlvl
from items import ITEMS, JEWELS, EQUIPMENTS
from classes.item import Item
from classes.potion import Potion
from classes.skills import PassiveBoost


def test_getexp():
    """Tests the getexp function"""
    lvl = 5
    # 5^3 = 125
    real_exp = 5 ** 3
    assert real_exp == 125
    test_exp = getexp(5)
    assert real_exp == test_exp

    lvl = randrange(30)
    real_exp = lvl ** 3
    test_exp = getexp(lvl)
    assert real_exp == test_exp


def test_getlvl():
    """Tests the getlvl function"""
    exp5 = 124
    exp6 = 125

    assert getlvl(exp5) == 5
    assert getlvl(exp6) == 6
    assert getlvl(exp5) == getlvl(exp6) - 1
    assert getlvl(0) == 1
    assert getlvl(1) == 2

#items lists

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
    boosts = (10,10,20)
    # owner should not be None, but entities are still not made
    boost = PassiveBoost(stats, boosts, owner=None)
    

