"""
Tests for the Gamer Project
"""


from items import ITEMS, JEWELS, EQUIPMENTS


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
