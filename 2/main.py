import sys
from typing import List, Tuple

def parse_ranges(text: str) -> List[Tuple[int, int]]:
    """
        parse comma separated list of ranges as '11-22,95-115,998-1012'
        into a list of (start, end) integer tuples
    """
    ranges = []
    for part in text.split(','):
        part = part.strip()
        if not part:
            continue
        start_str, end_str = part.split('-', 1)
        ranges.append((int(start_str), int(end_str)))
    return ranges

def is_invalid_id(n: int) -> bool:
    """
        an ID is valid only if it contains a sequence of integers that are repeated twice
        i.e. 11 -> '1' '1'
             6464 -> '64' '64'
    """
    s = str(n)
    # check that amount of digits are equal
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def main():
    raw = sys.stdin.read().strip()
    if not raw:
        print(0)
        return
    ranges = parse_ranges(raw)
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):  # inclusive
            if is_invalid_id(n):
                total += n
    print(total)

if __name__ == "__main__":
    main()
