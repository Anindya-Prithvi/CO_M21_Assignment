import sys
import re
from parser import parser

variables = []
def varproc(string):
	inst = string.split()
	if not (len(inst)==2): return "ERROR: INVALID VARIABLE DECLARATION"
	#first part of string has var
	if re.match(".*[^A-Za-z0-9_]+",inst[1]): return "ERROR: INVALID VARIABLE NAME"
	#second needs to be regexed
	#append to variable storage(address after instruction mem is made)
	variables.append([inst[1],0]) #stored variable (not addressed)
	return None

# files have been read to input stream using < command
# hence using stdin.read to read the whole stream together
assembly = sys.stdin.read()


# process each line of assembly
lines_assembly = assembly.split("\n")

# ignore blank lines
proc1 = [l for l in lines_assembly if not re.match("^\s*$", l)]

while True:
	if proc1==[]: break
	if proc1[0].split()[0]=="var":
		if (e:=varproc(ln:=proc1.pop(0))) is not None:
			print(f"ln: {lines_assembly.index(ln)} --> " + e)
			break
	else:
		break

#now proc1 is free of variables (hopefully)
if any((j:=re.match("\s*var.*",i)) for i in proc1):
	print(f"ln: {lines_assembly.index(j.string)} --> " + "ERROR: VARIABLE NOT DECLARED AT START")

#guaranteed proc1 only has instructions

inst_len = len(proc1)
for i in variables:
	i[1] = inst_len
	inst_len+=1

#all variables now have address

#now process for labels
labels=[]

def labelproc(string):
	#here string is always a valid label

	if string[:string.index(":")].strip() in {"add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"}:
		return "ERROR: LABEL NAME SAME AS MNENOMIC"
	labels.append([string[:string.index(":")].strip(), proc1.index(string)])
	ninst = string[string.index(":"):].lstrip(":")
	proc1[proc1.index(string)] = ninst
	return None



for i in proc1:
	if re.match("\s*[A-Za-z0-9_]+:.*",i):
		if (e:=labelproc(i)) is not None:
			print(f"ln: {lines_assembly.index(i)} --> " + e)



# WHEN PRINTING ERROR, GET THE LINE NUMBER, proc1.index(the_string.split())
# process vars, delete empty allocate instruction memory, alocate
# variable in memory

parsed = [parser(i.strip()) for i in proc1]

## if non_binary in parsed: print error
## else: create for loop and print binaries

print("\n".join(parsed))
print(*labels)
print(*variables)
