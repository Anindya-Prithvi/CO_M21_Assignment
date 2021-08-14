def div(div_instruction):
    register = {
        "R0": "000",
        "R1": "001",
        "R2": "010",
        "R3": "011",
        "R4": "100",
        "R5": "101",
        "R6": "110",
    }
    list = div_instruction.split()
    if "FLAGS" in list:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"
    if len(list) < 3:
        return "ERROR: INCOMPLETE INSTRUCTION"
    if list[0] != "div":
        return "ERROR: ILLEGAL ARGUMENT"
    else:
        c = 0
        bin_string = "0011100000"
        for j in range(1, 3):
            for i in register:
                if i == list[j]:
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    c = 1
            if c == 1:
                return "ERROR: INVALID REGISTER CODE"
        return bin_string


# instruct="div R1 R2"
# print(div(instruct))
