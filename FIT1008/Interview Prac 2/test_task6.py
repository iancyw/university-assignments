import math
import unittest
from test_common import *
import task2
import task6

class TestTask6(unittest.TestCase):
  def test_undo(self):
    ed = task6.Editor()
    
    extra_lines = [ "These are some extra lines.", "They are will be added to the string." ]

    ed.read_filename('TestFile.txt')
    ed.delete_num("")
    ed.insert_num_strings("1", ToListADT(task2.ListADT, extra_lines))

    ed.undo()
    self.assertTrue(equal_lines(ed, []))
    ed.undo()
    self.assertTrue(equal_lines(ed, test_content))
    with self.assertRaises(Exception, msg = "Undoing past the beginning of history should have failed."):
      ed.undo()


if __name__ == '__main__':
  unittest.main()
