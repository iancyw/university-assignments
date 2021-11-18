import math
import unittest
from test_common import *
import task2

class TestTask2(unittest.TestCase):
  def test_insert(self):
    x = task2.ListADT(10)
    
    ## This should not fail.
    append(x, [1 for i in range(1000)])
    
    ## If the ListADT has renamed the underlying array, or used some other
    ## representation, we can't realy test whether resizing is handled correctly.
    if not hasattr(x, "the_array"):
      raise AttributeError("could not identify underlying array for the ListADT.")

    y = task2.ListADT(10)

    # If we gave a smaller constant, should have become 40.
    self.assertEqual(len(y.the_array), 40, "Allocated array below threshold.")

    # ... and with rounding
    y = task2.ListADT(44)
    for i in range(45):
      y.insert(i, i)
    self.assertEqual(len(y.the_array), 84, "Incorrect grow.") # math.ceil(44 * 1.9)

    # Check shrinking
    for i in range(25):
      y.delete(len(y)-1)
    self.assertTrue(len(y.the_array) == 42, "Incorrect shrink.")

    # ... and with rounding
    z = task2.ListADT(54)
    for i in range(55):
      z.insert(i, i)
    self.assertEqual(len(z.the_array), 103, "Incorrect grow.")  # math.ceil(44 * 1.9)

    # Check shrinking
    for i in range(30):
      z.delete(len(z) - 1)
    self.assertEqual(len(z.the_array), 52, "Incorrect shrink.")

if __name__ == '__main__':
  unittest.main()
