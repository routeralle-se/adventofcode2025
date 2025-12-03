import sys

DIAL_SIZE = 100  # possible positions 0 to 99

def apply_rotation(position, rotation):
    """
        return the new dial position after applying rotation
    """
    direction = rotation[0]
    distance = int(rotation[1:])
    if direction == 'L':
        return (position - distance) % DIAL_SIZE
    if direction == 'R':
        return (position + distance) % DIAL_SIZE

def main():
    position = 50
    zeros_hit = 0
    for line in map(str.strip, sys.stdin):
        if not line:
            continue
        position = apply_rotation(position, line)
        if position == 0:
            zeros_hit += 1
    print(zeros_hit)

if __name__ == "__main__":
    main()