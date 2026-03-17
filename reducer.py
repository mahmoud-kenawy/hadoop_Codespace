#!/usr/bin/env python
import sys

current_name = None
max_volume = 0

for line in sys.stdin:
    name, volume = line.strip().split('\t')
    volume = int(volume)

    if name == current_name:
        if volume > max_volume:
            max_volume = volume
    else:
        if current_name is not None:
            print(f"{current_name}\t{max_volume}")
        current_name = name
        max_volume = volume

if current_name is not None:
    print(f"{current_name}\t{max_volume}")