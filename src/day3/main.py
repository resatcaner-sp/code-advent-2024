import re
from typing import List

regex = re.compile(r"mul\(\d{1,10},\d{1,8}\)")


def parse_text(text: str) -> List[str]:
    return re.findall(regex, text)


def calculate_result(functions: List[str]) -> int:
    result = 0
    for f in functions:
        result += int(f.split(',', 2)[0][4:]) * int(f.split(',', 2)[1][:-1])
    return result


def main() -> None:
    with open('input.txt') as f:
        corrupted_memory = f.read()
    functions = parse_text(corrupted_memory)
    print(f"part 1 {calculate_result(functions)}")
    print(f"part 2 {calculate_result(parse_text(process_do_dont(corrupted_memory)))}")


def process_do_dont(text: str) -> str:
    splitted = text.split("don't()")
    to_process = splitted[0]
    for text in splitted[1:]:
        to_process += text.partition("do()")[2]
    return to_process


if __name__ == "__main__":
    main()
