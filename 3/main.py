import sys

def max_bank_joltage(bank: str) -> int:
    """
        input a string which represents a bank of batteries,
        return the largest possible two-digit number formed by
        picking two digits in order (i < j)
    """
    digits = list(map(int, bank))
    best = -1
    suffix_max = -1
    # scan the string, right to left
    for d in reversed(digits):
        if suffix_max != -1:
            candidate = 10 * d + suffix_max
            if candidate > best:
                best = candidate
        # update the best digit seen to the right
        if d > suffix_max:
            suffix_max = d
    return best

def main():
    total = 0
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line:
            total += max_bank_joltage(line)
    print(total)


if __name__ == "__main__":
    main()
