#!/usr/bin/env python
"""
Common functionality for ListADT testing.

:author: Graeme Gange
"""
def ToListADT(Ty, elts):
  result = Ty()
  for i, elt in enumerate(elts):
    result.insert(i, elt)
  return result

def ToList(elts):
  l = []
  for i in range(len(elts)):
    l.append(elts[i])
  return l

## Syntactic sugar for building/comparing ListADTs.
def append(l, elts):
  sz = len(l)
  for i, e in enumerate(elts):
    l.insert(sz+i, e)

def equal(l, elts):
  if len(l) != len(elts):
    return False
  for i, x in enumerate(elts):
    if l[i] != x:
      return False
  return True

trail_content = ["This is a test file",
                 "It is a file that is used for testing.",
                 "It has several lines. And some trailing space ->  ",
                 "Those lines contain words."]

test_content = ["This is a test file",
                "It is a file that is used for testing.",
                "It has several lines.",
                "Those lines contain words."]

## Correct for possible '\n'
def equal_lines(ed, lines):
  ed_lines = ed.text_lines
  if len(ed_lines) != len(lines):
    return False
  for i, line in enumerate(lines):
    if ed_lines[i].strip('\n') != line:
      return False
  return True
