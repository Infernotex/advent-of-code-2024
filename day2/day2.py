from pathlib import Path

directory = Path(__file__).resolve().parent

def extract_data(path):
    inp = []

    with open(path, "r") as f:
        for line in f:
            inp.append([int(x) for x in line.split()])
        
    return inp

def is_safe(line):
    pairs = list(zip(line[:-1], line[1:]))
    if all(i < j for i, j in pairs) or all(j < i for i, j in pairs):
        if all(1 <= abs(i - j) and abs(i - j) <= 3 for i, j in pairs):
             return True
    
    return False

def part1(inp):
    safe = 0
    for line in inp:
        if is_safe(line):
            safe += 1

    print(safe)

def part2(inp):
    safe = 0
    for line in inp:
        if is_safe(line):
            safe += 1
        else:
            for i in range(len(line)):
                if is_safe(line[:i] + line[i+1:]):
                    safe += 1
                    break

    print(safe)

def main():
    test_dir = directory/"test"
    input_dir = directory/"input"
    inp = extract_data(input_dir)
    part1(inp)
    part2(inp)

if __name__ == "__main__":
    main()