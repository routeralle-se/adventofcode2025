import sys

grid = [list(line.strip()) for line in sys.stdin if line.strip()]
R, C = len(grid), len(grid[0])

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def accessible(r, c):
    return grid[r][c] == '@' and sum(
        0 <= r+dr < R and 0 <= c+dc < C and grid[r+dr][c+dc] == '@'
        for dr, dc in dirs
    ) < 4

def main():
    print(sum(accessible(r, c) for r in range(R) for c in range(C)))

if __name__ == "__main__":
    main()