#!/usr/bin/python
"""
The script calculates Fibonacci numbers

If not provided with arguments, the script asks for an input of how many 
Fibonacci numbers should be printed out in the sequence to file in the same folder.

Example of Fibonacci sequence (count number, sequence number):
1  2  3  4  5  6   7   8   9  10 
1  1  2  3  5  8  13  21  34  55

Example of usage:
python fibo.py --count 10 --path ./fibo.txt
"""

import argparse


def fibo_generator(n):
    """ Get generator to receive fibo numbers as stream """
    last = 0
    current = 1
    if n > 0:
        yield current
    else:
        yield None
    for i in range(1, n):
        temp = current
        current = current + last
        last = temp
        yield current


def parse_args():
    """ Parse cmd arguments """
    parser = argparse.ArgumentParser(description='The script writes Fibonacci numbers to file')
    parser.add_argument('--count', type=int, default=None,
                    help='an integer - how many Fibonacci numbers should be printed out')
    parser.add_argument('--path', type=str, default='./fibo.txt',
            help='a string - path to the file with Fibonacci numbers (default: ./fibo.txt)')
    args = parser.parse_args()
    return args


def main():
    """ Main logic of the script: parse arguments, open file and calculate fibo numbers there """
    try:
        args = parse_args()
        if args.count is None:  # ask for a numbers count if it isn't provided
            try:
                args.count = int(input('How many Fibonacci numbers should be printed out?\n'))
            except ValueError:
                print('Incorrect count of Fibonacci numbers')
                exit(1)

        try:
            with open(args.path, "w") as out:
                for fibo_number in fibo_generator(args.count):  # write fibo numbers as stream
                    out.write('{}\n'.format(fibo_number))
            print('Done, check {}'.format(args.path))
        except IOError:
            print('Error with writing to file!')
            exit(1)
    except KeyboardInterrupt:
        print('Exit from keyboard')


if __name__ == '__main__':
    main()

