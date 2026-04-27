###CalcProgram for practice
import argparse
from argparse import Namespace
def main(args:Namespace)->None:
    if args.operation == "add":
      result =  args.number1 + args.number2 
      print(result)
    elif args.operation == "sub":
       result = args.number1 - args.number2 
       print(result)
    elif args.operation == "mul":
       result = args.number1 * args.number2 
       print(result)
    elif args.operation == "div":
          if  args.number2 == 0:
               print("Error : Division by zero is not allowed : ")
          else:
              result = args.number1 / args.number2
              print(result)
    elif args.operation == "mod":
           result =  args.number2 % args.number1
           print(result)

if __name__ == "__main__":
     parser = argparse.ArgumentParser(prog="calcv3",description="This is calculator")
     parser.add_argument("operation",choices=["add","sub","mul","div","mod"])
     parser.add_argument("number1",type=int)
     parser.add_argument("number2",type=int)
     args = parser.parse_args()
     main(args)