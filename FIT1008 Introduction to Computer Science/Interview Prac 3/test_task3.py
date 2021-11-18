import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task3

class TestTask3(TestCase):
  def test_statistics(self):
    table = task3.HashTable(1024, 1)

    with self.vis("testing statistics"):
      for key in ["abcdef", "defabc"]:
        table[key] = 1
      stats = table.statistics()
      self.assertEqual(stats, (1, 1, 1, 0), "incorrect statistics")

    with self.vis():
      for key in ["acbedf"]:
        table[key] = 1
      stats = table.statistics()
      self.assertEqual(stats, (2, 3, 2, 0), "incorrect statistics")

    with self.vis():
      for key in ["abcedf"]:
        table[key] = 1
      stats = table.statistics()
      self.assertEqual(stats, (3, 6, 3, 0), "incorrect statistics")

    with self.vis():
      for key in ["abcd"]:
        table[key] = 1
      stats = table.statistics()
      self.assertEqual(stats, (3, 6, 3, 0), "incorrect statistics")

    with self.vis():
      for key in ["abdc"]:
        table[key] = 1
      stats = table.statistics()
      self.assertEqual(stats, (4, 7, 3, 0), "incorrect statistics")

    with self.vis():
      for key in ["bacd"]:
        table[key] = 1
      stats = table.statistics()
      self.assertEqual(stats, (5, 9, 3, 0), "incorrect statistics")

    with self.vis():
      for key in ["badc"]:
        table[key] = 1
      stats = table.statistics()
      self.assertEqual(stats, (6, 12, 3, 0), "incorrect statistics")

    self.assertTrue(self.check_okay("statistics"))

  def test_load_statistics(self):
    with self.vis("reporting words"):
      (w, _, _, _, _, _) = self.with_deadline(1, task3.load_dictionary_statistics, (1, 1024, "words_perm.txt", 10))
      self.assertEqual(w, 5, "incorrect word count")

    self.assertTrue(self.check_okay("load_statistics"))

if __name__ == '__main__':
  unittest.main()
