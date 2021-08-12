# st


def st(string, variables):
    # st reg1 mem_addr

    vdct = {i[0]: i[1] for i in variables}

    arr = string.split()
    output = "00101"

    registers = {
        "R0": "000",
        "R1": "001",
        "R2": "010",
        "R3": "011",
        "R4": "100",
        "R5": "101",
        "R6": "110",
    }

    if len(arr) == 3:
        if arr[1] in registers:
            output = output + registers.get(arr[1])
            if vdct.get(arr[2]):
                mem = vdct.get(arr[2])
                output = output + bin(mem)[2:].zfill(8)
                return output
            else:
                err = "ERROR: VARIABLE WAS NOT FOUND"
                return err
        elif arr[1] == "FLAGS":
            err = "ERROR: CANNOT SAVE FLAG REGISTER TO MEMORY"
            return err
        else:
            err = "ERROR: NO SUCH REGISTER"
            return err
    else:
        err = "ERROR: INCORRECT SYNTAX"
        return err
