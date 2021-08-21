import sys
import warnings

import matplotlib.pyplot as plt
from parsets import IMACC, IMG, PROGC, REGFLPC, ExecE, plot

warnings.filterwarnings("ignore")

MEM = IMACC(sys.stdin.read())  # Load memory from stdin
PC = PROGC(0)  # Start from the first instruction
RF = REGFLPC()  # initialize register and flags
EE = ExecE(MEM)
IM = IMG()
halted = False
cycle = 0

if MEM.inst_mem == ["0" * 16 for i in range(256)]:
    halted = True

while not halted:
    Instruction = MEM.getData(PC)  # Get current instruction
    IM.imgx.append(cycle)
    IM.imgy.append(PC.PC)
    halted, new_PC, new_regs = EE.execute(Instruction, RF.asdct(), IM, cycle)
    # Update RF compute new_PC
    RF.update(new_regs, new_PC)
    PC.dump()
    # Print PC
    RF.dump()
    # Print RF state
    PC.update(new_PC)
    # Update PC
    cycle += 1

MEM.dump()  # Print memory state

# plotting
plot(plt, IM)
