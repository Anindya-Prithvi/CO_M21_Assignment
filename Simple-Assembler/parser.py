# Parser for A,B,C,D,E,F

from sh_in import AND, Compare, Invert, Lshift, OR, Rshift, XOR
from ay_in import add, div, sub, mul, mov
from an_in import jgt, ld, st, jmp, jlt, je


def parser(string, labels, variables):
    # TODO
    parsed_string = ""

    break_string = string.split()
    if break_string==[]:
        return "ERROR: LABEL WAS NOT FOLLOWED BY AN INSTRUCTION"
    op = break_string[0]

    if op ==   "hlt":
        return "1001100000000000"
    elif op == "add":
        parsed_string = add(string)
    elif op == "sub":
        parsed_string = sub(string)
    elif op == "mul":
        parsed_string = mul(string)
    elif op == "div":
        parsed_string = div(string)
    elif op == "mov":
        parsed_string = mov(string)
    elif op == "and":
        parsed_string = AND(string)
    elif op == "cmp":
        parsed_string = Compare(string)
    elif op == "not":
        parsed_string = Invert(string)
    elif op == "ls":
        parsed_string = Lshift(string)
    elif op == "rs":
        parsed_string = Rshift(string)
    elif op == "or":
        parsed_string = OR(string)
    elif op == "xor":
        parsed_string = XOR(string)
    elif op == "jgt":
        parsed_string = jgt(string, labels)
    elif op == "ld":
        parsed_string = ld(string, variables)
    elif op == "st":
        parsed_string = st(string, variables)
    elif op == "jmp":
        parsed_string = jmp(string, labels)
    elif op == "jlt":
        parsed_string = jlt(string, labels)
    elif op == "jgt":
        parsed_string = je(string, labels)
    else:
        parsed_string = "ERROR: WRONG MNENOMIC in " + string

    return parsed_string
