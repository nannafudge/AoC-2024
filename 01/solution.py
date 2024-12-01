#!/bin/python3

"""
  Do not worry Santa I am here to save Christmas thank me
  later but for now check out these sick solutions :>)
"""

import re
import bisect
import argparse

INPUT_FILE = "./input.txt"

argparser = argparse.ArgumentParser()
argparser.add_argument("-p", "--part", type=int, default=0)

def read_input_sorted():
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

  return left_list, right_list

def part_zero():
  left_list, right_list = read_input_sorted()
  distance = 0

  # Lists are already sorted upon ingestion
  for l, r in zip(left_list, right_list):
    distance += (abs(l - r))

  print(distance)

def part_one():
  left_set = set()
  right_bucket = dict()

  similarity = 0
  with open(INPUT_FILE, 'r') as infile:
    for line in infile.readlines():
      split = re.split("\s+", line.replace("\n", ""))
      left, right = int(split[0]), int(split[1])
      left_set |= {left}

      if right_bucket.get(right) is None:
        right_bucket[right] = 1
      else:
        right_bucket[right] += 1

  for left in left_set:
    if right_bucket.get(left) is not None:
      similarity += left * right_bucket[left]

  print(similarity)

# Sry santa
SOLUTION_MAP = {
  0: part_zero,
  1: part_one,
}

if __name__ == "__main__":
  args = argparser.parse_args()
  SOLUTION_MAP[args.part]()