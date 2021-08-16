#IMACC

class IMACC:
	def __init__(self, stdin):
		self.inst_mem = stdin.split("\n")
		self.inst_mem = [i.strip() for i in self.inst_mem]
		for i in range(256-len(self.inst_mem)):
			self.inst_mem.append("0000000000000000")
	def getData(self, PC):
		return self.inst_mem[PC.PC]
	def maintainvar(self, addr, value):
		# called by execution engine incase of ld,st
		self.inst_mem[addr] = value
	def dump(self):
		return "\n".join(self.inst_mem)

class PROGC:
	PC = 0
	def __init__(self,val):
		self.PC = val
	def update(self, new_PC):
		self.PC = new_PC
	def dump(self):
		return bin(PC)[2:].zfill(8)

class REGFLPC:
	rfpc = {"R0":"00000000","R1":"00000000","R2":"00000000","R3":"00000000","R4":"00000000","R5":"00000000","R6":"00000000","FLAGS":"00000000","PC":0}
	def __init__(self):
		pass
	def asdct(self):
		return self.rfpc
	def update(self, new_regs, new_PC):
		self.rfpc.update(new_regs)
		self.rfpc.update({"PC":new_PC})
	def dump(self):
		temp = [[i,a[i]] for i in rfpc]
		temp.sort()
		temp.pop(0)
		temp.pop(0)
		temp1 = [i[1] for i in temp]
		return " ".join(temp1)