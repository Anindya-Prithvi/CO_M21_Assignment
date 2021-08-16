import sys
from parsets import IMACC
from parsets import PROGC
from parsets import REGFLPC
from parsets import ExecE


MEM = IMACC(sys.stdin.read()) # Load memory from stdin
PC = PROGC(0) # Start from the first instruction
RF = REGFLPC() #initialize register and flags
EE = ExecE(MEM)
halted = False
cycle = 1

while(not halted):
	Instruction = MEM.getData(PC); # Get current instruction
	halted, new_PC, new_regs = EE.execute(Instruction, RF.asdct()); # Update RF compute new_PC
	RF.update(new_regs, new_PC)
	PC.dump(); # Print PC
	RF.dump(); # Print RF state
	PC.update(new_PC); # Update PC
	cycle+=1

MEM.dump() # Print memory state