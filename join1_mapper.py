#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()  # Remove any whitespace
    parts = line.split(",")  # Split the line into parts

    if len(parts) != 2:
        continue  # Skip any lines that don't have exactly two parts

    title, value = parts

    # Check if the value part is a channel or a number of viewers
    if value.isdigit():
        # It's a viewer count, emit title and viewer count
        print(f"{title}\t{value}")
    elif value == 'ABC':
        # It's an ABC show, emit title and channel marker
        print(f"{title}\tABC")