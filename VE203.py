import numpy as np
import math
import argparse
import requests
import re
from bs4 import BeautifulSoup

# ----------Argument Parsing


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-dio", "--diophantine", nargs=3, help="Solve a Diophantine equation.")
    parser.add_argument(
        "-ff", "--factorize", nargs=1, help="Fermat factorization.")
    parser.add_argument(
        "-gcd", "--greatcommondivisor", nargs=2, help="Great common divisor.")
    parser.add_argument(
        "-euc", "--euclidian", nargs=3, help="Find the solution to the extended Euclidian algorithm.")
    return parser.parse_args()

# ----------Utilizations


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


def find_modular_inverse(a, m):
    b = 0
    # Print out the process of finding a modular inverse.
    # Finding b s.t. a * b === 1 (mod m)
    [x1, x2] = [a, m]
    [x1_alias, x2_alias] = [x1, x2]
    x1_list = [x1]
    x2_list = [x2]
    remainder = 0
    while(remainder != 1):
        x1 = x2_alias
        x2 = x1_alias//x2_alias
        remainder = x1_alias-(x1_alias//x2_alias)*x2_alias
        [x1_alias, x2_alias] = [x1, x2]
        x1_list.append(x1)
        x2_list.append(x2)
    return b


def linear_congruence(x1, x2, do_print):
    [x1_alias, x2_alias] = [x1, x2]
    x1_list = [x1]
    x2_list = [x2]
    coeff = []
    remainder = 100000
    while(remainder != 0):
        x1 = x2_alias
        remainder = x1_alias-(x1_alias//x2_alias)*x2_alias
        x2 = x1_alias//x2_alias
        if (do_print):
            print(str(x1_alias), "=", str(x1_alias//x2_alias),
                  "×", str(x2_alias), "+", str(remainder))
        x2 = remainder
        coeff.append(x1_alias//x2_alias)
        [x1_alias, x2_alias] = [x1, x2]
        x1_list.append(x1)
        x2_list.append(x2)
    return [x1_list, x2_list, coeff]


def euclidian(a, b, do_print):  # YES I AM F**KING LAZY
    # Gives an solution to  ax + by = 1
    x0, y0 = 0, 0
    if do_print:
        r = requests.post('https://www.math.uwaterloo.ca/~snburris/cgi-bin/linear-query',
                          data={'coeff1': a, 'coeff2': b, 'coeff': 1, 'data': "Solve It"})
        soup = BeautifulSoup(r.text)
        text = soup.get_text().replace("\n\n", "\n").replace("Thoralf Responds", "") + \
            "\nRetrieved from https://www.math.uwaterloo.ca/~snburris/htdocs/linear.html\n"

        print(text)
        patternx = re.compile(r'(?<=x0 = )([+-]?[1-9]\d*|0)')
        x0 = int(patternx.findall(text)[0])
        patterny = re.compile(r'(?<=y0 = )([+-]?[1-9]\d*|0)')
        y0 = int(patterny.findall(text)[0])
    else:
        x0, x = 1, 0
        y0, y = 0, 1
        while b:
            q = a//b
            x, x0 = x0 - q*x, x
            y, y0 = y0 - q*y, y
            a, b = b, a % b
    return [x0, y0]

# ----------Tool Functions


def gcd_a_b(a, b):
    [x1_list, x2_list, coeff] = linear_congruence(a, b, True)
    print("Therefore gcd of", str(a), "and", str(b), "is", str(x2_list[-2]))
    return


def solve_diophantine_eqn(a, b, c):  # The form of ax+by = c
    gcd_a_b = math.gcd(a, b)
    if (c % gcd_a_b) != 0:
        print("The Diophantine equation "+str(a)+"x + " +
              str(b)+"y = "+str(c)+"has no solution!")
    else:
        pass
    # TODO: DE
    return


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


def chinese_remainder_theorem(x, a_n, m_n):
    if len(a_n) != len(m_n):
        print("Invalid input!")
        return
    return


if __name__ == "__main__":
    args = parse_args()
    if args.diophantine != None:
        solve_diophantine_eqn(int(args.diophantine[0]), int(
            args.diophantine[1]), int(args.diophantine[2]))
    elif args.factorize != None:
        fermat_factorization(int(args.factorize[0]))
    elif args.greatcommondivisor != None:
        gcd_a_b(int(args.greatcommondivisor[0]), int(
            args.greatcommondivisor[1]))
    elif args.euclidian != None:
        euclidian(int(args.euclidian[0]), int(
            args.euclidian[1]), True)
    else:
        while(1):
            cmd = input('\nEnter command:\n')
            cmd = cmd.split(" ")
            if cmd[0] == "exit":
                break
            elif (cmd[0] == "dio") | (cmd[0] == "diophantine"):
                try:
                    print("YAY")
                    solve_diophantine_eqn(
                        int(cmd[1]), int(cmd[2]), int(cmd[3]))
                except IndexError:
                    print("Argument numbers invalid!")
            elif (cmd[0] == "ff") | (cmd[0] == "factorize"):
                try:
                    fermat_factorization(int(cmd[1]))
                except IndexError:
                    print("Argument numbers invalid!")
            elif (cmd[0] == "gcd") | (cmd[0] == "greatcommondivisor"):
                try:
                    gcd_a_b(int(cmd[1]), int(cmd[2]))
                except IndexError:
                    print("Argument numbers invalid!")
            elif (cmd[0] == "euc") | (cmd[0] == "euclidian"):
                try:
                    euclidian(int(cmd[1]), int(cmd[2]), True)
                except IndexError:
                    print("Argument numbers invalid!")
            else:
                pass
