import re

separators = re.compile(r"")
pattern = re.compile(
    r"(\d{1,15})\s*?[;:?]\s*?"  # week
    r"([a-zA-Z\-']{1,25})\s*?[;:?]\s*?"  # first_name
    r"([a-zA-Z\d\-'\s]{1,20})\s*?[;:?]\s*?"  # subject
    r"(L|p|S|lab)\s*?[;:?]\s*?"  # type_
    r"([a-zA-Z\-']{1,29})\s*?[;:?]\s*?"  # midle_name
    r"([a-zA-Z\-']{1,30})\s*?[;:?]\s*?"  # last_name
    r"(\d{1,5})\s*?[;:?]\s*?"  # day
    r"(\d{1,4})\s*?[;:?]\s*?"  # pair
    r"(\d{1,4})\s*?[;:?]\s*?"  # course
    r"([a-zA-Z\d]{1,6})\s*?[;:?]\s*?"  # group_code
    r"(\d+)",  # auditorium
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
