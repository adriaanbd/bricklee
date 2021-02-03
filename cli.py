import argparse

def main():
    parser = argparse.ArgumentParser
    parser.add_argument("Hello", type=str)
    args = parser.parse_args()
    print(args)