from typing import List


def vertical_count(text_list: List[str]) -> int:
    number_of_lines = len(text_list)
    result = 0
    for i in range(number_of_lines):
        for j in range(len(text_list[i])):
            if i + 3 < number_of_lines:
                # check for XMAS down
                if text_list[i][j] == 'X' and text_list[i + 1][j] == 'M' and text_list[i + 2][j] == 'A' and \
                        text_list[i + 3][j] == 'S':
                    result += 1
                # check for SMAX down
                if text_list[i][j] == 'S' and text_list[i + 1][j] == 'A' and text_list[i + 2][j] == 'M' and \
                        text_list[i + 3][j] == 'X':
                    result += 1
    return result


def horizontal_count(text_list: List[str]) -> int:
    result = 0
    for text in text_list:
        result += text.count('XMAS')
        result += text.count('SAMX')
    return result


def diagonal_count(text_list: List[str]) -> int:
    number_of_lines = len(text_list)
    result = 0
    for i in range(number_of_lines):
        for j in range(len(text_list[i])):
            if i + 3 < number_of_lines and j + 3 < len(text_list[i]):
                # check for XMAS right down
                if text_list[i][j] == 'X' and text_list[i + 1][j + 1] == 'M' and text_list[i + 2][j + 2] == 'A' and \
                        text_list[i + 3][j + 3] == 'S':
                    result += 1

            if i + 3 < number_of_lines and j - 3 >= 0:
                # check for XMAS left down
                if text_list[i][j] == 'X' and text_list[i + 1][j - 1] == 'M' and text_list[i + 2][j - 2] == 'A' and \
                        text_list[i + 3][j - 3] == 'S':
                    result += 1

            if i - 3 >= 0 and j + 3 < len(text_list[i]):
                # check for XMAS right up
                if text_list[i][j] == 'X' and text_list[i - 1][j + 1] == 'M' and text_list[i - 2][j + 2] == 'A' and \
                        text_list[i - 3][j + 3] == 'S':
                    result += 1

            if i - 3 >= 0 and j - 3 >= 0:
                # check for XMAS left up
                if text_list[i][j] == 'X' and text_list[i - 1][j - 1] == 'M' and text_list[i - 2][j - 2] == 'A' and \
                        text_list[i - 3][j - 3] == 'S':
                    result += 1

    return result


def mas_check(text_list: List[str]) -> int:
    numbers_of_lines = len(text_list)
    result = 0
    for i in range(numbers_of_lines):
        for j in range(len(text_list[i])):
            if 0 < i < numbers_of_lines - 1 and 0 < j < len(text_list[i]) - 1:
                if text_list[i][j] == 'A':
                    condition_1 = (text_list[i - 1][j - 1] == 'M' and text_list[i + 1][j + 1] == 'S') or (
                             text_list[i - 1][j - 1] == 'S' and text_list[i + 1][j + 1] == 'M')
                    condition_2 = (text_list[i + 1][j - 1] == 'M' and text_list[i - 1][j + 1] == 'S') or (
                             text_list[i + 1][j - 1] == 'S' and text_list[i - 1][j + 1] == 'M')
                    if condition_1 and condition_2:
                        result += 1
    return result


def main() -> None:
    with open('input.txt') as f:
        text_list = [line.strip() for line in f]
    print(f"part 1 {horizontal_count(text_list) + vertical_count(text_list) + diagonal_count(text_list)}")
    print(f"part 2 {mas_check(text_list)}")


if __name__ == "__main__":
    main()
