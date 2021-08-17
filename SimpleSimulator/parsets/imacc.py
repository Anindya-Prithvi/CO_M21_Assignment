# IMACC
import re


class IMACC:
    def __init__(self, stdin):
        self.inst_mem = stdin.split("\n")
        self.inst_mem = [l for l in self.inst_mem if not re.match("^\s*$", l)]
        self.inst_mem = [i.strip() for i in self.inst_mem]
        for i in range(256 - len(self.inst_mem)):
            self.inst_mem.append("0000000000000000")

    def getData(self, PC):
        return self.inst_mem[PC.PC]

    def maintainvar(self, addr, value):
        # called by execution engine incase of ld,st
        self.inst_mem[int(addr,2)] = value

    def dump(self):
        print("\n".join(self.inst_mem))
        return None


class PROGC:
    PC = 0

    def __init__(self, val):
        self.PC = val

    def update(self, new_PC):
        self.PC = new_PC

    def dump(self):
        print(bin(self.PC)[2:].zfill(8), end=" ")


class REGFLPC:
    rfpc = {
        "R0": "0000000000000000",
        "R1": "0000000000000000",
        "R2": "0000000000000000",
        "R3": "0000000000000000",
        "R4": "0000000000000000",
        "R5": "0000000000000000",
        "R6": "0000000000000000",
        "FLAGS": "0000000000000000",
        "PC": 0,
    }

    def __init__(self):
        pass

    def asdct(self):
        return self.rfpc

    def update(self, new_regs, new_PC):
        self.rfpc.update(new_regs)
        self.rfpc.update({"PC": new_PC})

    def dump(self):
        temp = [[i, self.rfpc[i]] for i in self.rfpc]
        temp.sort()
        temp.append(temp.pop(0))
        temp.pop(0)
        # print(temp)
        temp1 = [i[1] for i in temp]
        print(" ".join(temp1))
