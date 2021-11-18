import math
import unittest
from test_common import *
import task5

class TestTask5(unittest.TestCase):
  def test_search(self):
    ed = task5.Editor()
    ed.read_filename('TestFile.txt')
    
    queries = [ ("is a", [1, 2]), # Multi-word
                ("is", [1, 2]) ]  # Multiple occurrences
    for query, lines in queries: 
      ed_lines = ed.search_string(query)
      self.assertTrue(sorted(ToList(ed_lines)) == lines, msg =  "Incorrect result for search query {0}".format(query))

if __name__ == '__main__':
  unittest.main()
