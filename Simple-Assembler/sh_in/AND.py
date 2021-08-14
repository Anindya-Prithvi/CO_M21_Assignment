def AND(str_in):

    arr = str_in.split()
    output = "01100"
    err = ""
    if "FLAGS" in arr: return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"

    register = {
        "R0": "000",
        "R1": "001",
        "R2": "010",
        "R3": "011",
        "R4": "100",
        "R5": "101",
        "R6": "110",
        # 'R7':'111';
    }

    rlist = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]

    if len(arr) == 4:
        if arr[1] == "FLAGS":
            err = "ERROR: INVALID USE OF FLAGS"
            return err
        if arr[1] in rlist:
            output = output + register.get(arr[1])
        else:
            err = "ERROR: INVALID REGISTER CODE"
            return err
        if arr[2] == "FLAGS":
            err = "ERROR: INVALID USE OF FLAGS"
            return err

        if arr[2] in rlist:
            output = output + register.get(arr[2])
        else:
            err = "ERROR: INVALID REGISTER CODE"
            return err
        if arr[3] == "FLAGS":
            err = "ERROR: INVALID USE OF FLAGS"
            return err
        if arr[3] in rlist:
            output = output + register.get(arr[3])
        else:
            err = "ERROR: INVALID REGISTER CODE"
            return err
        output = output + "00"
        return output

    else:
        err = "ERROR: INVALID NUMBER OF ARGUMENTS"
        return err


# TEST
# s_in = "and R1 R2 R3"
# print(AND(s_in))
# output = 01100 001 010 011 00
