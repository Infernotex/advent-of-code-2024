from pathlib import Path

directory = Path(__file__).resolve().parent

def extract_data(path):
    l1 = []
    l2 = []

    with open(path, "r") as f:
        for line in f:
            l = [int(x) for x in line.split()]
            l1.append(l[0])
            l2.append(l[1])
    
    return l1, l2

def part1(l1, l2):
    distance = 0
    l1.sort()
    l2.sort()
    
    for i, a in enumerate(l1):
        distance += abs(a - l2[i])
    
    print(distance)

def part2(l1, l2):
    instances = {}
    similarity_score = 0

    for i in l2:
        if i in instances:
            instances[i] += 1
        else:
            instances[i] = 1
    
    for i in l1:
        if i in instances:
            similarity_score += i * instances[i]
    
    print(similarity_score)

def main():
    test = directory/"test"
    input = directory/"input"
    l1, l2 = extract_data(input)
    part1(l1, l2)
    part2(l1, l2)

if __name__ == "__main__":
    main()