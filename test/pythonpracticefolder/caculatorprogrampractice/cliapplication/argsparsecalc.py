import argparse
from argparse import Namespace
def main(args: Namespace)->None:
    if args.operation == "add":
        result = args.number1 +args.number2
        print(result)
    elif args.operation == "sub":
        result = args.number1 -args.number2
        print(result)
    elif args.operation == "mul":
        result = args.number1 * args.number2
        print(result)
    elif args.operation == "div":
        if args.number2 == 0:
            print("Error:Division by zero is not allowed ")
        else:
            result = args.number1 / args.number2
            print(result)
    elif args.operation == "mod":
         result = args.number1 % args.number2
if __name__ == "__main__":
    # create argument parser
    parser = argparse.ArgumentParser("calcv2",description="This is calculator") 
    parser.add_argument("operation",choices=["add","sub","mul","div","mod"])
    parser.add_argument("number1",type=int)
    parser.add_argument("number2",type=int)
    args = parser.parse_args()
    main(args)
    
