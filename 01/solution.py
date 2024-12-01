#!/bin/python3

"""
  Do not worry Santa I am here to save Christmas thank me
  later but for now check out these sick solutions :>)
"""

import re
import bisect

INPUT_FILE = "./input.txt"

if __name__ == "__main__":
  left_list = []
  right_list = []

  with open(INPUT_FILE, 'r') as infile:
    for line in infile.readlines():
      split = re.split("\s+", line.replace("\n", ""))
      left, right = int(split[0]), int(split[1])
      left_list.insert(
        bisect.bisect(left_list, left),
        left
      )
      right_list.insert(
        bisect.bisect(right_list, right),
        right
      )
  
  distance = 0
  # Lists are already sorted upon ingestion
  for l, r in zip(left_list, right_list):
    distance += (abs(l - r))
  
  print(distance)