import sys
from parser import parser

# files have been read to input stream using < command
# hence using stdin.read to read the whole stream together
assembly = sys.stdin.read()

# process each line of assembly
lines_assembly = assembly.split("\n")

proc1 = [i.split() for i in lines_assembly]

while [] in proc1:
	proc1.remove([])

clean_inst = [" ".join(i) for i in proc1]

#print("\n".join(clean_inst))

# WHEN PRINTING ERROR, GET THE LINE NUMBER, proc1.index(the_string.split())
# process vars, delete empty allocate instruction memory, alocate
# variable in memory

parsed = [parser(i.strip()) for i in clean_inst]

## if non_binary in parsed: print error
## else: create for loop and print binaries

print("\n".join(parsed))
