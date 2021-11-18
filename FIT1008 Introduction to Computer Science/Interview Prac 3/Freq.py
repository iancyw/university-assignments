#!/usr/bin/env python3
"""
:author: Graeme Gange
"""
from task1 import HashTable


class Freq:
    def __init__(self):
        self.word_frequency = HashTable()
        self.max = (None, None)
  
    def add_file(self, filename):
        with open(filename, 'r', encoding="utf-8") as f:
            for line in f:
                for word in line.split():
                    if word in self.word_frequency:
                        current = self.word_frequency[word]
                        current += 1
                        self.word_frequency[word] = current
                        if current > self.max[1]:
                            position = self.word_frequency.hash(word)
                            self.max = self.word_frequency.table[position]
                    else:
                        self.word_frequency[word] = 1
                        if self.max == (None, None):
                            position = self.word_frequency.hash(word)
                            self.max = self.word_frequency.table[position]
        f.close()

    def rarity(self, word):
        try:
            max_num = self.max[1]
            occurrences = self.word_frequency[word]
            if occurrences >= (max_num/100):
                return 0
            elif (max_num / 100) > occurrences >= (max_num / 1000):
                return 1
            elif occurrences < (max_num/100):
                return 2
        except KeyError:
            return 3

    def compare(self, other_filename):
        raise NotImplementedError
