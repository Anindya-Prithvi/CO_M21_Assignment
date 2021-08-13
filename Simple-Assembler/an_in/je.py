# je


def je(string, labels):

    arr = string.split()
    output = "10010"
    err = ""

    lbdct = {i[0]: i[1] for i in labels}
    if len(arr) == 2:
        output = output + "000"
        if lbdct.get(arr[1]) is not None:
            mem = lbdct.get(arr[1])
            output = output + bin(mem)[2:].zfill(8)
            return output
        else:
            err = "ERROR: LABEL WAS NOT FOUND"
            return err

    else:
        err = "ERROR: INVALID NUMBER OF ARGUMENTS"
        return err
