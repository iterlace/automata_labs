import re

separators = re.compile(r"")
pattern = re.compile(
    r"(\d{1,15})[;:?]"
    r"([a-z\-']{1,25})[;:?]"
    r"([a-z\d\-'\s]{1,20})[;:?]"
    r"(L|p|S|lab)[;:?]"
    r"([a-z\-']{1,29})[;:?]"
    r"([a-z\-']{1,30})[;:?]"
    r"(\d{1,5})[;:?]"
    r"(\d{1,4})[;:?]"
    r"(\d{1,4})[;:?]"
    r"([a-z\d]{1,6})[;:?]"
    r"(\d+)",
    re.I,
)


def validate(line: str) -> bool:
    match = pattern.match(line)
    if match is None:
        return False
    line.split()
    return True


def main() -> None:
    with open("input_4.csv", "r") as f:
        for line in f.readlines():
            is_valid = validate(line)
            if is_valid:
                print(f"Line is valid: {line.strip()}")
            else:
                print(f"Line is invalid: {line.strip()}")


if __name__ == "__main__":
    main()
