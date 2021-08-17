import sys
import time
import warnings

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from parsets import IMACC, IMG, PROGC, REGFLPC, ExecE

warnings.filterwarnings("ignore")

MEM = IMACC(sys.stdin.read())  # Load memory from stdin
PC = PROGC(0)  # Start from the first instruction
RF = REGFLPC()  # initialize register and flags
EE = ExecE(MEM)
IM = IMG()
halted = False
cycle = 1

if MEM.inst_mem == ["0" * 16 for i in range(256)]:
    halted = True

while not halted:
    Instruction = MEM.getData(PC)
    # Get current instruction
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
plt.scatter(IM.imgx, IM.imgy)
plt.title("Memory access trace")
plt.xlabel("Cycle")
plt.axes().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.ylabel("Memory Address")
plt.axes().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig(fname=f"plots/time_{time.time()}.png", dpi=600, bbox_inches="tight")
