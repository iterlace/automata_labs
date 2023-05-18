import random
import string
from typing import Sequence


def generate_str(charset: Sequence[str], length: int) -> str:
    return "".join(random.choices(charset, k=length))


def generate_line() -> str:
    week = random.randint(1, 15)
    first_name = generate_str(string.ascii_letters + "-'", random.randint(1, 25))
    subject = generate_str(
        string.ascii_letters + string.digits + "-' ", random.randint(1, 20)
    )
    type_ = random.choice(["L", "p", "S", "lab"])
    middle_name = generate_str(string.ascii_letters + "-'", random.randint(1, 29))
    last_name = generate_str(string.ascii_letters + "-'", random.randint(1, 30))
    day = random.randint(1, 5)
    pair = random.randint(1, 4)
    course = random.randint(1, 4)
    group_code = generate_str(string.ascii_letters + string.digits, 6)
    auditorium = random.randint(5, 100)

    parts = [
        week,
        first_name,
        subject,
        type_,
        middle_name,
        last_name,
        day,
        pair,
        course,
        group_code,
        auditorium,
    ]
    separators = [";", ":", "?"]
    output = ""
    for idx, part in enumerate(parts):
        if idx == len(parts) - 1:
            output += str(part)
        else:
            output += f"{part}{random.choice(separators)}"
    return output


def main():
    with open("data/input_4.csv", "a+") as f:
        for i in range(20):
            f.write(generate_line() + "\n")


if __name__ == "__main__":
    main()
