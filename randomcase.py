import click
import random


@click.command()
@click.argument("input_string", nargs=-1)
def main(input_string):
    input_string = " ".join(input_string)
    for c in input_string:
        if random.random() < 0.5:
            print(c, end="")
        else:
            print(c.upper(), end="")
    print()


if __name__ == "__main__":
    main()
