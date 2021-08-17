def st(inst, rfpc, memobj):
    rfpc["FLAGS"] = "0" * 16
    rfpc["PC"] += 1
    memobj.inst_mem[int(inst[8:], 2)] = rfpc["R" + str(int(inst[5:8]), 2)]
    return rfpc
