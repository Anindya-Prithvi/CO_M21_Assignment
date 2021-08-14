import re
import sys
from parser import parser

variables = []

run = True


def varproc(string):
    inst = string.split()
    if not (len(inst) == 2):
        return '[91m' + "ERROR:" + '[0m' + " INVALID VARIABLE DECLARATION"
    # first part of string has var
    if re.match(".*[^A-Za-z0-9_]+", inst[1]):
        return '[91m' + "ERROR:" + '[0m' + " INVALID VARIABLE NAME"
    if inst[1] in {
        "add",
        "sub",
        "mov",
        "ld",
        "st",
        "mul",
        "div",
        "rs",
        "ls",
        "xor",
        "or",
        "and",
        "not",
        "cmp",
        "jmp",
        "jlt",
        "jgt",
        "je",
        "hlt",
    }:
        return '[91m' + "ERROR:" + '[0m' + " VARIABLE NAME SAME AS MNENOMIC"
    # second needs to be regexed
    # append to variable storage(address after instruction mem is made)
    variables.append([inst[1], 0])  # stored variable (not addressed)
    return None


def labelproc(string):
    # here string is always a valid label

    if string[: string.index(":")].strip() in {
        "add",
        "sub",
        "mov",
        "ld",
        "st",
        "mul",
        "div",
        "rs",
        "ls",
        "xor",
        "or",
        "and",
        "not",
        "cmp",
        "jmp",
        "jlt",
        "jgt",
        "je",
        "hlt",
    }:
        return '[91m' + "ERROR:" + '[0m' + " LABEL NAME SAME AS MNENOMIC"
    labels.append([string[: string.index(":")].strip(), proc1.index(string)])

    if len(set([i[0] for i in labels])) != len([i[0] for i in labels]):
        return '[91m' + "ERROR:" + '[0m' + " MULTIPLE SAME NAME LABEL DECLARATION FOUND"

    ninst = string[string.index(":") :].lstrip(":")
    proc1l[proc1.index(string)] = ninst
    return None


# files have been read to input stream using < command
# hence using stdin.read to read the whole stream together
assembly = sys.stdin.read()

if bool(re.match("\s*$", assembly)):
    print("ln: 0 --> " + '[91m' + "ERROR:" + '[0m' + " EMPTY STDIN OR NO INSTRUCTION")
    run = False


if run:
    # process each line of assembly
    lines_assembly = assembly.split("\n")

    # ignore blank lines
    proc1 = [l for l in lines_assembly if not re.match("^\s*$", l)]

while run:
    if proc1 == []:
        break
    if proc1[0].split()[0] == "var":
        if (e := varproc(ln := proc1.pop(0))) is not None:
            print(f"ln: {lines_assembly.index(ln)+1} --> " + e)
            run = False
            break
    else:
        break

# now proc1 is free of variables (hopefully)
if run and any((j := re.match("\s*var.*", i)) for i in proc1):
    print(
        f"ln: {lines_assembly.index(j.string)+1} --> "
        + '[91m' + "ERROR:" + '[0m' + " VARIABLE NOT DECLARED AT START"
    )
    run = False

# guaranteed proc1 only has instructions

if run:
    inst_len = len(proc1)
    for i in variables:
        i[1] = inst_len
        inst_len += 1

    # all variables now have address

    # now process for labels
    labels = []

    proc1l = proc1.copy()


if run:
    for i in proc1:
        if re.match("\s*[A-Za-z0-9_]+:.*", i):
            if (e := labelproc(i)) is not None:
                print(f"ln: {lines_assembly.index(i)+1} --> " + e)
                run = False


if run:
    # check hlt instruction
    hlts = [
        l
        for l in lines_assembly
        if re.match("\s*hlt\s*", l) or re.match("[A-Za-z0-9]+:\s*hlt\s*", l)
    ]
    if len(hlts) > 1:
        print(
            f"ln: {lines_assembly.index(hlts[0])+1} --> " + '[91m' + "ERROR:" + '[0m' + " MULTIPLE HALT INSTRUCTIONS IN STDIN"
        )
        run = False
    if len(hlts) == 1:
        if proc1.index(hlts[0]) != len(proc1) - 1:
            print(
                f"ln: {lines_assembly.index(hlts[0])+1} --> " + '[91m' + "ERROR:" + '[0m' + " HALT IS NOT LAST INSTRUCTION"
            )
            run = False
        else:
            pass

if run:
    parsed = [parser(i.strip(), labels, variables) for i in proc1l]
    for i, e in enumerate(parsed):
        if e[0] != "0" and e[0] != "1":
            print(f"ln: {lines_assembly.index(proc1[i])+1} --> " + '\033[91m' + "ERROR:" + '\033[0m' + e[6:])
            run = False
            
    if parsed == [] or parsed[-1] != "1001100000000000":
        run = False
        print("ln: xx ERROR: HALT INSTRUCTION NOT FOUND")

    ## if non_binary in parsed: print error
    ## else: create for loop and print binaries

if run:
    print("\n".join(parsed))
