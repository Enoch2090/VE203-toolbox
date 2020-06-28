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


def is_square(number_in):
    is_square = False
    if int(math.sqrt(number_in))*int(math.sqrt(number_in)) == number_in:
        is_square = True
    return is_square


def is_prime(number_in):
    is_prime = True
    if number_in > 1:
        for i in range(2, number_in//2+1):
            if (number_in % i) == 0:
                is_prime = False
                break
    return is_prime


def fermat_factorization(number_in):
    indent = "\t"
    if number_in < 0:
        print("Invalid input!")
        return
    elif number_in == 1:
        return
    else:
        print("Now fatorizing:", number_in)
        n_1 = math.floor(math.sqrt(number_in))
        n_2 = n_1 + 1
        print("We find", str(n_1)+"² < " +
              str(number_in)+" < "+str(n_2)+"².")
        print("We need to calculate k²−" +
              str(number_in), "for", str(n_2)+" < k < "+"("+str(number_in)+"+1)/2 = "+str((number_in+1)/2))
        square_found = False
        while(not square_found):
            print(indent+"We find:")
            remainder = n_2*n_2-number_in
            if (is_square(remainder)):
                print(indent+str(n_2) + "² -",
                      str(number_in), "=", str(remainder), "=", str(
                          int(math.sqrt(remainder)))+"².")
                print("Therefore", number_in, "=", str(
                    n_2-int(math.sqrt(remainder))), "×", str(n_2+int(math.sqrt(remainder)))+".")
                if not is_prime(n_2-int(math.sqrt(remainder))):
                    print(str(n_2-int(math.sqrt(remainder))),
                          "is not a prime, continue factorization.")
                if not is_prime(n_2+int(math.sqrt(remainder))):
                    print(str(n_2+int(math.sqrt(remainder))),
                          "is not a prime, continue factorization.")
                if is_prime(n_2-int(math.sqrt(remainder))) and is_prime(n_2+int(math.sqrt(remainder))):
                    print("Both are primes.")
                return
            else:
                print(indent+str(n_2) + "² -",
                      str(number_in), "=", str(remainder)+",")
                n_2 += 1
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
