#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
