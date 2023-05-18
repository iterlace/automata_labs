from task_4 import pattern  # isort: skip


def main() -> None:
    with open("data/input_4.csv", "r") as fi:
        with open("data/output_5.csv", "w") as fo:
            for line in fi.readlines():
                # skip \4 (type_)
                out = pattern.sub(r"\1;\2;\3;\5;\6;\7;\8;\9;\10;\11", line)
                fo.write(out)


if __name__ == "__main__":
    main()
