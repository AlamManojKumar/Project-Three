import argparse
from argparse import Namespace

def main(args: Namespace) -> None:
    """Performs a calculation based on the provided operation and numbers.

    Supports basic arithmetic operations such as addition, subtraction,
    multiplication, division, and modulus.

    Args:
        args (Namespace): Parsed command-line arguments containing:
            - operation (str): The operation to perform ("add", "sub", "mul", "div", "mod").
            - number1 (int): The first integer operand.
            - number2 (int): The second integer operand.

    Returns:
        None
    """
    if args.operation == "add":
        result = args.number1 + args.number2
        print(result)


if __name__ == "__main__":
    """Entry point of the calculator CLI application.

    Parses command-line arguments and invokes the main function.
    """
    # Create argparse argument parser
    parser = argparse.ArgumentParser(
        prog="calcv2",
        description="This is Calculator"
    )

    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div", "mod"],
        help="Arithmetic operation to perform"
    )
    parser.add_argument(
        "number1",
        type=int,
        help="First number"
    )
    parser.add_argument(
        "number2",
        type=int,
        help="Second number"
    )

    args = 
    main(args)