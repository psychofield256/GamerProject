#!/usr/bin/env python
"""
Tests for the Gamer Project Game.
"""

# this time, I'll focus on the code, and write tests after
# so what it keeps is:
# todo:
# every test

from classes.skills import PermanentBoost


class TestSkill(object):
    """Test classes.skills."""

    def test_permanent_boost(self):
        """Test the PermanentBoost instances."""
        stats = {"str": 5, "vit": 2}
        pb = PermanentBoost("super strength", stats, "fake owner")
