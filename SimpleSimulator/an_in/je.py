def je(instr, rfpc):
	if instr[:5]!="10010":
		return "ERROR NOT JE"

	if rfpc["FLAGS"][-1] == 1: #ET?
		rfpc["PC"] = int(instr[8:],2)
	else:
		rfpc["PC"] += 1
	rfpc["FLAGS"] = "0"*16 #flag reset
	return rfpc