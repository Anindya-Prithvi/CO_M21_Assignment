def jgt(instr, rfpc):
	if instr[:5]!="10001":
		return "ERROR NOT JGT"

	if rfpc["FLAGS"][-2] == 1: #GT?
		rfpc["PC"] = int(instr[8:],2)
	else:
		rfpc["PC"] += 1
	rfpc["FLAGS"] = "0"*16 #flag reset
	return rfpc