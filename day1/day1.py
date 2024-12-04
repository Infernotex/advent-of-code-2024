from pathlib import Path

directory = Path(__file__).resolve().parent

def extract_data(path):
    l = []
    r = []

    with open(path, "r") as f:
        for line in f:
            inp = [int(x) for x in line.split()]
            l.append(inp[0])
            r.append(inp[1])

    return l, r

def part1(l, r):
    distance = 0
    l.sort()
    r.sort()
    
    for i, a in enumerate(l):
        distance += abs(a - r[i])
    
    print(distance)

def part2(l, r):
    instances = {}
    similarity_score = 0

    for i in r:
        if i in instances:
            instances[i] += 1
        else:
            instances[i] = 1
    
    for i in l:
        if i in instances:
            similarity_score += i * instances[i]
    
    print(similarity_score)

def main():
    test_dir = directory/"test"
    input_dir = directory/"input"
    l, r = extract_data(input_dir)
    part1(l, r)
    part2(l, r)

if __name__ == "__main__":
    main()