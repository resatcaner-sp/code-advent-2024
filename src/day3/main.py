import re
from typing import List

regex = re.compile(r"mul\(\d{1,10},\d{1,8}\)")

def parse_text(path: str) -> List[str]:
    with open(path) as f:
        corrupted_memory = f.read()
    return re.findall(regex, corrupted_memory)

def calculate_result(functions: List[str]) -> int:
    result = 0
    for f in functions:
        result += int(f.split(',',2)[0][4:]) * int(f.split(',',2)[1][:-1])
    return result

def main() -> None:
    functions = parse_text("input.txt")
    print(calculate_result(functions))

if __name__ == "__main__":
    main()


