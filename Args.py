import argparse
from email import parser
import sys

def input():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=5,
               help='Enter the first number:  ')
    parser.add_argument('--y', type=float, default=3,
               help='Enter the second number:  ')
    parser.add_argument('--operator', type=str, default='division',
               help='Enter the (addition, subtraction, multiplication, division):  ')
    args = parser.parse_args()
    sys.stdout.write(str(calculation(args)))                       

def calculation(args):
    if args.operator == 'addition':
        return args.x + args.y
    elif args.operator == 'subtraction':
        return args.x - args.y 
    elif args.operator == 'multiplication':
        return args.x * args.y
    elif args.operator == 'division':
        return args.x / args.y  

if __name__== '__main__':
    input()