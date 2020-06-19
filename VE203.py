import numpy as np
import math
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-dio", "--diophantine", nargs=3, help="Solve a Diophantine equation.")
    parser.add_argument(
        "-ff", "--factorize", nargs=1, help="Fermat factorization.")
    return parser.parse_args()


def solve_diophantine_eqn(a, b, c):  # The form of ax+by = c
    gcd_a_b = math.gcd(a, b)
    if (c % gcd_a_b) != 0:
        print("The Diophantine equation "+str(a)+"x + " +
              str(b)+"y = "+str(c)+"has no solution!")
    else:
        pass
    # TODO: DE
    return


def fermat_factorization(number_in, tab_level=0):
    print(number_in)
    # TODO: Recursively factorize the number.
    return


if __name__ == "__main__":
    args = parse_args()
    if args.diophantine != None:
        solve_diophantine_eqn(int(args.diophantine[0]), int(
            args.diophantine[1]), int(args.diophantine[2]))
    elif args.factorize != None:
        fermat_factorization(int(args.factorize[0]))
    else:
        while(1):
            cmd = input('Enter command:\n')
            cmd.split(" ")
            if cmd[0] == "exit":
                break
            elif (cmd[0] == "dio") | (cmd[0] == "diophantine"):
                try:
                    solve_diophantine_eqn(
                        int(cmd[1]), int(cmd[2]), int(cmd[3]))
                except IndexError:
                    print("Argument numbers invalid!")
            elif (cmd[0] == "ff") | (cmd[0] == "factorize"):
                try:
                    fermat_factorization(int(cmd[1]))
                except IndexError:
                    print("Argument numbers invalid!")
            else:
                pass
