#!/usr/bin/env python
import sys

current_show = None
current_count = 0
is_abc = False

for line in sys.stdin:
    line = line.strip()
    title, value = line.split('\t')

    if title != current_show:
        if current_show is not None and is_abc:
            print(f"{current_show} {current_count}")
        current_show = title
        current_count = 0
        is_abc = False

    if value == 'ABC':
        is_abc = True
    else:
        current_count += int(value)

# Don't forget to output the last show if it was on ABC
if is_abc:
    print(f"{current_show} {current_count}")