import math
import unittest
from test_common import *
import task1

class TestTask1(unittest.TestCase):
  # Check that initialisation doesn't fail
  def test_init(self):
    y = task1.ListADT(10)

  def test_str(self):
    # Check str for non-empty lists
    x = task1.ListADT(10)
    append(x, [1, 2, 3])
    self.assertEqual(str(x).strip('\n'), '1\n2\n3')

  def test_len(self):
    # Test length of an empty list
    x = task1.ListADT(20)
    self.assertEqual(len(x), 0, msg="Length of empty list should be 0")
    # And for a non-empty one
    x.insert(0, 2)
    self.assertEqual(len(x), 1, msg="Length should be 1")

  def test_get(self):
    x = task1.ListADT(10)
    append(x, [0, 1, 2, 3, 4])
    
    # Check both positive and negative indices
    for index, value in [ (1, 1), (-2, 3)]:
      self.assertEqual(x[index], value, msg="Incorrect _getitem_.")

  def test_set(self):
    x1 = task1.ListADT(10)
    # Testing assignment in empty list
    with self.assertRaises(IndexError, msg = "Assignment in empty list should fail"):
      x1[0] = 8
    append(x1, [1, 2, 3])
    # Testing assignment (and implicitly _getitem_)
    x1[0] = 8
    self.assertTrue(equal(x1, [8, 2, 3]), msg = "Incorrect assignment at index 0")
    # Testing assignment out of bounds
    with self.assertRaises(IndexError, msg = "Assignment out of bounds should fail"):
      x1[3] = 8


  def test_eq(self):
    x1 = task1.ListADT(10)
    x2 = task1.ListADT(20)
    # Check equality for lists of different size
    self.assertTrue(x1 == x2, msg =  "Lists with different capacity should still be equal.")
    # Check that equality tests for List type.
    append(x1, [1, 2, 3])
    self.assertFalse(x1 == [1, 2, 3], "Equality test doesn't check type.")
    append(x2, [1, 2, 3])
    self.assertTrue(x1 == x2, msg = "ListADT with same elements should return True")

  def test_insert(self):
    x = task1.ListADT(10)
    # Check insertion at beginning
    x.insert(0, 1)
    self.assertTrue(equal(x, [1]), msg =  "Insertion in empty list failed")
    # And at end.
    x.insert(1, 2)
    self.assertTrue(equal(x, [1, 2]), msg =  "Insertion at end failed")
    x.insert(-2, 0)
    self.assertTrue(equal(x, [0, 1, 2]), msg = "Insertion at front failed")
    x.insert(-1, 3)
    self.assertTrue(equal(x, [0, 1, 2, 3]), msg = "Insert at end failed using negative index")

    # Check insertion out-of-bounds
    with self.assertRaises(IndexError, msg = "Inserting out of bounds should fail"):
      x.insert(6, 8)

    with self.assertRaises(Exception, msg = "Inserting above capacity should raise an exception."):
      append(x, [1 for i in range(20) ])

  def test_delete(self):
    x = task1.ListADT(10)
    append(x, [0,1,2,3,4,5])
    # Test deletion from the middle.
    x.delete(2)
    self.assertTrue(equal(x, [0,1,3,4,5]), msg =  "Delete from middle failed")
    # checks length of list has decreased
    self.assertTrue(x.length == 5, msg = "Length has not decreased")
    # And from a negative index.
    x.delete(-4)
    self.assertTrue(equal(x, [0,3,4,5]), msg =  "Negative deletion failed")
    # checks length of list has decreased
    self.assertTrue(x.length == 4, msg="Length has not decreased")



if __name__ == '__main__':
  unittest.main()
