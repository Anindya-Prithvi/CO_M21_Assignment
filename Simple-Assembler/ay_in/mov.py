def mov(mov_instruction):
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
    list = mov_instruction.split()
    if len(list)!=3:
        return "ERROR: TOO MANY OPERANDS"
    if list[2] in register:
        c = 0
        bin_string = "0001100000"
        for j in range(1, 3):
            for i in register:
                if i == list[j] and (not ((j == 1) and (i == "FLAGS"))):
                    bin_string = bin_string + register[i]
                    c = 0
                    break
                else:
                    if (list[j] == "FLAGS") and (j==1):
                        return "ERROR: CANNOT WRITE TO FLAGS"
                    c = 1
            if c == 1:
                return "ERROR: INVALID REGISTER CODE"
        return bin_string

    else:
        c = 0
        bin_string = "00010"

        if list[2][0] != "$":
            return "ERROR: INVALID OPERAND"
        list[2] = list[2][1:]

        try:
            num = int(list[2])
            if num > 255 or num < 0:
                return f"ERROR: {num} CANNOT BE USED AS AN IMMEDITATE VALUE"
            for i in register:
                if i == list[1] and i != "FLAGS":
                    bin_string = bin_string + register[i]
                    break
                elif i=="FLAGS":
                    return "ERROR: IMMEDITATE VALUES CANNOT BE WRITTEN TO FLAGS"
            else:
                return "ERROR: INVALID REGISTER CODE"
            bin_string = bin_string + format(num, "08b")
            return bin_string
        except:
            return "ERROR: THIS INSTRUCTION ONLY TAKES INT/REG"


# instruct="mov R1 $a"
# print(mov(instruct))

# instruct="mov R1 R2"
# print(mov(instruct))
