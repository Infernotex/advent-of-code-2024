from pathlib import Path

directory = Path(__file__).resolve().parent

def extract_data(path):
    with open(path, "r") as f:
        return f.read().split("\n")

def horizontal(x, y, inp):
    instances = 0
    width = len(inp[0])

    if x + 3 < width:
        if inp[y][x] == "X" and inp[y][x+1] == "M" and inp[y][x+2] == "A" and inp[y][x+3] == "S":
            instances += 1

    if 0 <= x - 3:
        if inp[y][x] == "X" and inp[y][x-1] == "M" and inp[y][x-2] == "A" and inp[y][x-3] == "S":
            instances += 1

    return instances

def vertical(x, y, inp):
    instances = 0
    height = len(inp)

    if y + 3 < height:
        if inp[y][x] == "X" and inp[y+1][x] == "M" and inp[y+2][x] == "A" and inp[y+3][x] == "S":
            instances += 1

    if 0 <= y - 3:
        if inp[y][x] == "X" and inp[y-1][x] == "M" and inp[y-2][x] == "A" and inp[y-3][x] == "S":
            instances += 1

    return instances

def diagonal(x, y, inp):
    instances = 0
    width, height = len(inp[0]), len(inp)

    if x + 3 < width and y + 3 < height:
        if inp[y][x] == "X" and inp[y+1][x+1] == "M" and inp[y+2][x+2] == "A" and inp[y+3][x+3] == "S":
            instances += 1

    if 0 <= x - 3 and 0 <= y - 3:
        if inp[y][x] == "X" and inp[y-1][x-1] == "M" and inp[y-2][x-2] == "A" and inp[y-3][x-3] == "S":
            instances += 1
    
    if x + 3 < width and 0 <= y - 3:
        if inp[y][x] == "X" and inp[y-1][x+1] == "M" and inp[y-2][x+2] == "A" and inp[y-3][x+3] == "S":
            instances += 1
    
    if 0 <= x - 3 and y + 3 < height:
        if inp[y][x] == "X" and inp[y+1][x-1] == "M" and inp[y+2][x-2] == "A" and inp[y+3][x-3] == "S":
            instances += 1

    return instances

def part1(inp):
    instances = 0
    width, height = len(inp[0]), len(inp)

    for y in range(height):
        for x in range(width):
            instances += horizontal(x, y, inp) + vertical(x, y, inp) + diagonal(x, y, inp)
        
    print(instances)


def part2(inp):
    instances = 0
    width, height = len(inp[0]), len(inp)

    for y in range(1, height-1):
        for x in range(1, width-1):
            if inp[y][x] == "A":
                m1 = inp[y-1][x-1] + inp[y+1][x+1]
                m2 = inp[y+1][x-1] + inp[y-1][x+1]
                
                if m1 in ["MS", "SM"] and m2 in ["MS", "SM"]:
                    instances += 1
        
    print(instances)

def main():
    test_dir = directory/"test"
    test2_dir = directory/"test2"
    input_dir = directory/"input"
    inp = extract_data(input_dir)
    part1(inp)
    part2(inp)

if __name__ == "__main__":
    main()