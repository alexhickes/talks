"""
dividemo - tool to divide two integer numbers.
"""
import argparse
import logging
import sys


def divided(dividend, divisor):
    return dividend // divisor  # //=integer division


def main(arguments):
    # Parse command line arguments.
    parser = argparse.ArgumentParser(description='divide two integer numbers.')
    parser.add_argument('dividend', metavar='DIVIDEND', type=int,
                        help='number to divide')
    parser.add_argument('divisor', metavar='DIVISOR', type=int,
                        help='number to divide by')
    args = parser.parse_args(arguments)
    if args.divisor == 0:
        parser.error('DIVISOR must not be 0')

    # Process arguments and print result.
    result = divided(args.dividend, args.divisor)
    print(result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main(sys.argv[1:])
