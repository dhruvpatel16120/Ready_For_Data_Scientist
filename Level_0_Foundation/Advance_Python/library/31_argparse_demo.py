import argparse
import sys

def argparse_demo():
    print("--- Python CLI Argument Parsing (argparse) ---")
    
    # 1. Create the parser
    parser = argparse.ArgumentParser(
        description="A demonstration of command line argument parsing in Python.",
        epilog="Usage: python 31_argparse_demo.py --name Antigravity --verbose"
    )

    # 2. Add arguments
    # Positional argument (Required)
    # Note: If no arguments are provided, this script will show an error.
    # To make it work in this environment, we'll check sys.argv first.
    
    parser.add_argument("command", choices=["greet", "add", "list"], help="The operation to perform")

    # Optional argument with a value
    parser.add_argument("-n", "--name", default="User", help="Name to greet (default: User)")
    
    # Optional flag (boolean)
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    # Arguments with types
    parser.add_argument("--count", type=int, default=1, help="Number of times to repeat (default: 1)")

    # 3. Parse arguments
    # If no args are passed (like in many interactive environments), we'll simulate them
    if len(sys.argv) == 1:
        print("No command line arguments provided. Simulating: 'greet --name Alice --count 3'")
        args = parser.parse_args(["greet", "--name", "Alice", "--count", "3"])
    else:
        args = parser.parse_args()

    # 4. Use the arguments
    if args.verbose:
        print(f"DEBUG: Arguments received: {args}")

    if args.command == "greet":
        for _ in range(args.count):
            print(f"Hello, {args.name}!")
    
    elif args.command == "add":
        print("Additive logic would go here.")
    
    elif args.command == "list":
        print("Listing logic would go here.")

    print("\nArgparse demo completed.\n")

if __name__ == "__main__":
    argparse_demo()
