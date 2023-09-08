#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    count = len(sys.argv) - 1
    if count == 0:
        print("0 argument")
    elif count == 1:
        print("1 argument")
    else:
        print("{} arguments".format(count))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
