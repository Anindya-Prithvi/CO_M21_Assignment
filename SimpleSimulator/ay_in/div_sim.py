# div reg2 reg3 = 00111 00000 010 011
def div_instruction(instruct, reg):
    if instruct[:5] != "00111":
        return "ERROR:ILLEGAL INSTRUCTION"

    register = {
        "R0": "000",
        "R1": "001",
        "R2": "010",
        "R3": "011",
        "R4": "100",
        "R5": "101",
        "R6": "110",
        "FLAGS": "111",
    }
    if (
        instruct[10:13] == register["FLAGS"]
        or instruct[13:] == register["FLAGS"]
    ):
        return "ERROR:FLAG REGISTER WAS ACCESSED"

    reg["FLAGS"] = "0" * 16

    cx, cy = 0, 0

    for key in register:
        if register[key] == instruct[10:13]:
            cx = 1
            key1 = key
        elif register[key] == instruct[13:]:
            cy = 1
            key2 = key

    if cx == 0 or cy == 0:
        return "ERROR:INVALID REGISTER"
    x = int(reg[key1], 2)
    y = int(reg[key2], 2)
    if y == 0:
        return "ERROR:DIVISION BY ZERO"
    t = divmod(x, y)  # is this operation legal: div R0 R1
    reg["R0"] = format(t[0], "016b")
    reg["R1"] = format(t[1], "016b")
    reg["PC"] = reg["PC"] + 1
    return reg


# test
# rpc = {
#         "R0": "0000000000000000",
#         "R1": "0000000000000000",
#         "R2": "0000000000000011",
#         "R3": "0000000000000010",
#         "R4": "0000000000000000",
#         "R5": "0000000000000000",
#         "R6": "0000000000000000",
#         "FLAGS":"0000000000000000",
#         "PC": 10
#     }

# print(div_instruction("0011100000010011",rpc))
