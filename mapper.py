#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader, None)  # skip header

for row in reader:
    try:
        name = row[6]
        volume = int(row[5])
        print(f"{name}\t{volume}")
    except:
        continue  # skip malformed rows