import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task6

class TestTask6(TestCase):
  def test_addfile(self):
    with self.vis():
      freq = task6.Freq()
      freq.add_file('words_simple.txt')
      for word in ['this', 'dictionary', 'words']:
        self.assertEqual(freq.word_frequency[word], 1,
          "Incorrect frequency.")

    with self.vis():
      freq = task6.Freq()
      freq.add_file('words_dup.txt')
      for (word, count) in [('words', 3), ('and', 2)]:
        self.assertEqual(freq.word_frequency[word], count,
          "Incorrect frequency.")

    with self.vis():
      freq = task6.Freq()
      freq.add_file('words_freq.txt')
      for (word, count) in [('b', 9), ('cuttlefish', 30), ('fish', 1)]:
        self.assertEqual(freq.word_frequency[word], count,
          "Incorrect frequency.")
     
    self.assertTrue(self.check_okay("addfile"))

  def test_rarity(self):
    with self.vis():
      freq = task6.Freq()
      freq.add_file('words_freq.txt')

      self.assertEqual(freq.rarity('a'), 0,
        "Incorrect rarity.")

    with self.vis():
      self.assertEqual(freq.rarity('fish'), 2,
        "Incorrect rarity.")

    with self.vis():
      self.assertEqual(freq.rarity('cuttlefish'), 0,
        "Incorrect rarity.")

    with self.vis():
      self.assertEqual(freq.rarity('b'), 1,
        "Incorrect rarity.")

    with self.vis():
      freq1 = task6.Freq()
      freq1.add_file('words_dup.txt')
      assert freq1.max == ('words', 3)

      self.assertEqual(freq1.rarity('and'), 0,
        "Incorrect rarity.")

    self.assertTrue(self.check_okay("rarity"))

if __name__ == '__main__':
  unittest.main()
