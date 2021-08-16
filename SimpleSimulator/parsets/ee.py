from sh_in import*
from an_in import*

class ExecE:
    def __init__(self, memobj):
        self.mem = memobj

    def execute(self, inst16bit, rfpc):
        if inst16bit[:5] == "00101":  # store
            self.mem.maintainvar(
                inst16bit[8:], rfpc.get(inst16bit[5:8]).zfill(16)
            )
            rfpc["PC"] += 1
            rfpc["FLAGS"] = "0000000000000000"
            return False, rfpc["PC"], rfpc
        elif inst16bit[:5] == "10011":
            return True, -1, rfpc
        else:
            rfpc = ExecE.parse(inst16bit, rfpc)
            return False, rfpc["PC"], rfpc

    def parse(inst16bit, rfpc):
        if inst16bit[:5] == "00000":
            return add(inst16bit, rfpc)
        elif inst16bit[:5] == "00001":
            return sub(inst16bit, rfpc)
        elif inst16bit[:5] == "00010":
            return movim(inst16bit, rfpc)
        elif inst16bit[:5] == "00011":
            return movr(inst16bit, rfpc)
        elif inst16bit[:5] == "00100":
            return ld(inst16bit, rfpc)  # add provision for mem view
        # elif inst16bit[:5]=="00101":
        # 	return st(inst16bit, rfpc)
        elif inst16bit[:5] == "00110":
            return mul(inst16bit, rfpc)
        elif inst16bit[:5] == "00111":
            return div(inst16bit, rfpc)
        elif inst16bit[:5] == "01000":
            return rshift(inst16bit, rfpc)
        elif inst16bit[:5] == "01001":
            return lshift(inst16bit, rfpc)
        elif inst16bit[:5] == "01010":
            return xor(inst16bit, rfpc)
        elif inst16bit[:5] == "01011":
            return OR(inst16bit, rfpc)
        elif inst16bit[:5] == "01100":
            return AND(inst16bit, rfpc)
        elif inst16bit[:5] == "01101":
            return invert(inst16bit, rfpc)
        elif inst16bit[:5] == "01110":
            return compare(inst16bit, rfpc)
        elif inst16bit[:5] == "01111":
            return jmp(inst16bit, rfpc)
        elif inst16bit[:5] == "10000":
            return jlt(inst16bit, rfpc)
        elif inst16bit[:5] == "10001":
            return jgt(inst16bit, rfpc)
        elif inst16bit[:5] == "10010":
            return je(inst16bit, rfpc)
