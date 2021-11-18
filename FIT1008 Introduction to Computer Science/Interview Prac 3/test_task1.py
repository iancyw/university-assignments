import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task1

class TestTask1(TestCase):
  def test_init(self):
    with self.vis("empty init"):
      x = task1.HashTable()
    with self.vis("init with size and base"):
      z = task1.HashTable(800, 2398)
      
    assert self.check_okay("init")
    
  def test_hash(self):

    x = task1.HashTable(1024, 17)
    for (key, expect) in [("", 0),
                          ("abcdef", 389),
                          ("defabc", 309)]:
        with self.vis():
          self.assertEqual(x.hash(key), expect, msg=f"Unexpected hash with base 17 and key {key}.")

    assert self.check_okay("hash")

  def test_set(self):

    x = task1.HashTable()
    x["Aho"] = "item1"
    x["Test"] = "item2"
    x["Help"] = "item3"
    assert x.table[49][1] == "item1"
    assert x.table[12][1] == "item2"
    assert x.table[41][1] == "item3"
    assert x.count == 3
    x["Aho"] = "item4"
    assert x.table[49][1] == "item4"
    assert x.count == 3

    assert self.check_okay("set")

  # The tests for __contains__ and __getitem__ use __setitem__, so we don't make any assumptions
  # about the underlying array representation. Remember to define your own tests for __setitem__
  # (and rehash)
  def test_contains(self):
    x = task1.HashTable(1024, 1)

    with self.vis():
      self.assertFalse("abcdef" in x, "False positive in __contains__ for empty table.")

    with self.vis("unexpected failure in setitem"):
      x["abcdef"] = 18
      x["definitely a string"] = None
      x["abdcef"] = "abcdef"
    
    for key in ["abcdef", "definitely a string", "abdcef"]:
      with self.vis():
        self.assertTrue(key in x, "False negative in __contains__ for key {}".format(key))

    assert self.check_okay("contains")

  def test_getitem(self):
    x = task1.HashTable(1024, 1)

    with self.vis():
      with self.assertRaises(KeyError, msg="x[key] should raise KeyError for missing key."):
        elt = x["abcdef"]
      
    with self.vis("unexpected failure in setitem"):
      x["abcdef"] = 18
      x["definitely a string"] = None

    with self.vis():
      self.assertEqual(x["abcdef"], 18, msg = "Read after store failed.")

    x["abdcef"] = 22

    assert self.check_okay("getitem")

  def test_rehash(self):

    x = task1.HashTable(3, 1)
    x["Aho"] = "item1"
    x["Test"] = "item2"
    x["Help"] = "item3"
    assert x.count == 3
    assert x.table_size == 3
    x["Yes"] = "item4"
    assert x.table_size == 7
    assert x["Aho"] == "item1"
    assert x["Test"] == "item2"
    assert x["Help"] == "item3"
    assert x["Yes"] == "item4"

    assert self.check_okay("rehash")


if __name__ == '__main__':
  unittest.main()
