import argparse
import sys

def greet(name):
    if name:
        return f'Hello {name}.'
    return f'Hello Panama City, Panama.'

def main(args=None):
    if not args:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('hello', type=str, help='a generic greeting')
    parser.add_argument('--name', help='a customized greeting')
    args = parser.parse_args(args)
    greeting = greet(args.name)
    print(greeting)
    return greeting