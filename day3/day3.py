import re
from pathlib import Path

directory = Path(__file__).resolve().parent

def extract_data(path):
    with open(path, "r") as f:
        return f.read()

def part1(inp):
    sum = 0

    muls = re.findall(r"mul\(\d+,\d+\)", inp)
    for mul in muls:
        factors = [int(x) for x in mul.replace("mul", "").replace("(", "").replace(")", "").split(",")]
        sum += factors[0] * factors[-1]
    
    print(sum)


def part2(inp):
    sum = 0

    filtered = re.sub(r"don't\(\)(.|\n)+?do\(\)", "", inp)
    filtered = re.sub(r"don't\(\)(.|\n)*", "", filtered)
    muls = re.findall(r"mul\(\d+,\d+\)", filtered)
    for mul in muls:
        factors = [int(x) for x in mul.replace("mul", "").replace("(", "").replace(")", "").split(",")]
        sum += factors[0] * factors[-1]
    
    print(sum)

def main():
    test_dir = directory/"test"
    input_dir = directory/"input"
    inp = extract_data(input_dir)
    part1(inp)
    part2(inp)

if __name__ == "__main__":
    main()