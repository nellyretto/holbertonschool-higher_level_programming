#!/usr/bin/python3
import sys


def main():

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 argument(s): .")
    else:
        print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:", end='\n\n')
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")


if __name__ == "__main__":
    main()
