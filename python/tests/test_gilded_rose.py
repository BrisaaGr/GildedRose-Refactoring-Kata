# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

        
if __name__ == '__main__':
    unittest.main()

def test_conjured_item_degrades_twice_as_fast_before_sell_date():
    items = [Item("Conjured Mana Cake", 5, 20)]
    gr = GildedRose(items)
    gr.update_quality()
    assert items[0].quality == 18


def test_conjured_item_degrades_four_times_after_sell_date():
    items = [Item("Conjured Mana Cake", 0, 20)]
    gr = GildedRose(items)
    gr.update_quality()
    assert items[0].quality == 16


def test_conjured_quality_never_below_zero():
    items = [Item("Conjured Mana Cake", 5, 1)]
    gr = GildedRose(items)
    gr.update_quality()
    assert items[0].quality == 0