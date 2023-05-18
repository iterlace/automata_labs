import re

separators = re.compile(r"")
pattern = re.compile(
    r"(\d{1,15})[;:?]"  # week
    r"([a-z\-']{1,25})[;:?]"  # first_name
    r"([a-z\d\-'\s]{1,20})[;:?]"  # subject
    r"(L|p|S|lab)[;:?]"  # type_
    r"([a-z\-']{1,29})[;:?]"  # midle_name
    r"([a-z\-']{1,30})[;:?]"  # last_name
    r"(\d{1,5})[;:?]"  # day
    r"(\d{1,4})[;:?]"  # pair
    r"(\d{1,4})[;:?]"  # course
    r"([a-z\d]{1,6})[;:?]"  # group_code
    r"(\d+)",  # auditorium
    re.I,
)


def validate(line: str) -> bool:
    match = pattern.match(line)
    if match is None:
        return False
    return True


def main() -> None:
    with open("data/input_4.csv", "r") as f:
        for line in f.readlines():
            if validate(line):
                print(f"Line is valid: {line.strip()}")
            else:
                print(f"Line is invalid: {line.strip()}")


if __name__ == "__main__":
    main()
