## sys is a standard library, it is used to store command line arguments
## argv - is simply a  list that holds all the values 
## sys.argv - it is used to pass the values to  python script 
##from the command line at run time  
import sys
##This is entry point of application
def print_usage():
    print("""
 usage:calc.py <operation><arg1><arg2>
 <operation> = add |sub|mul|div
 arg1 = anynumber
 arg2 = anynumber
            """)        
def main(args:list[str])->None:
    if args[0] == 'add':
        result = int(args[1])+ int(args[2])
        print(result)
    elif args[0] == 'sub':
        result = int(args[1]) - int(args[2])
        print(result)
    elif args[0] == 'mul':
        result = int(args[1]) * int(args[2])
        print(result)
    elif args[0] == 'div':
        if int(args[2]) == 0:
           print("cannot divide by zero")
        else:
           result = int(args[1]) / int(args[2])
           print(result)
    else:
        print("invalid operator  ")
        print_usage()
if __name__ == "__main__":
    #print(sys.argv)
    args = sys.argv[1::]
    if len(args)  !=3:
        print("Invalid argument passed")
        print_usage()
        exit(1)
    print(args)
    main(args)
    exit(0)
