import sys

def main():
    exec('from fxy.calc import *')

    if len(sys.argv) > 1:
        expression = sys.argv[1]
        try:
            result = eval(expression)
            print(result)
        except Exception as e:
            print(f"Error evaluating expression: {e}")
    else:
        print("Please provide a valid 'fxy' expression to evaluate.")

if __name__ == "__main__":
    main()

