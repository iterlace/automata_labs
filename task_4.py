import re

separators = re.compile(r";:\?")
pattern = re.compile(r"", re.I)


def validate(line: str) -> (bool, str):
    match = pattern.match(line)
    if match is None:
        return False
    line.split()
    return True


def main() -> None:
    with open("input_4.csv", "r") as f:
        for line in f.readlines():
            is_valid, comment = validate(line)
            if is_valid:
                print(f"Line is valid: {line}")
            else:
                print(f"Line is invalid ({comment}): {line}")


if __name__ == "__main__":
    main()
