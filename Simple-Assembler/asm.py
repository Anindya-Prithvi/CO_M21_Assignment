import sys
from parser import parser

# files have been read to input stream using < command
# hence using stdin.read to read the whole stream together
assembly = sys.stdin.read()

# process each line of assembly
lines_assembly = assembly.split("\n")

# process vars, delete empty allocate instruction memory, alocate
# variable in memory

parsed = [parser(i.strip()) for i in lines_assembly]

## if non_binary in parsed: print error
## else: create for loop and print binaries

print(*parsed)
