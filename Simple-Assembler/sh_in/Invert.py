def Invert(str_in):

    arr = str_in.split()
    output = "01101"
    output = output + "00000"
    err = ""
    if "FLAGS" in arr:
        return "ERROR: FLAGS CANNOT BE AN OPERAND HERE"

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

    if len(arr) == 3:
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

        return output

    else:
        err = "ERROR: INVALID NUMBER OF ARGUMENTS"
        return err


# TEST
# s_in = "not R1 R2"
# print(Invert(s_in))
# output = 01101 00000 001 010
