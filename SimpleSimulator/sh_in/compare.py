def cmp(s ,rpc):
   
    rpc["FLAGS"]= "0"*16
    flag = "0"*12
    s = s[5::]
    R_a = s[:3]
    R_b = s[3:6]
    
    register = {
        "000" : "R0",
        "001" : "R1",
        "010" : "R2",
        "011" : "R3",
        "100" : "R4",
        "101" : "R5",
        "110" : "R6",
    }

    R_a = register[R_a]
    R_b = register[R_b]

    R_a = int(rpc[R_a],2)
    R_b = int(rpc[R_b],2)

    if R_a > R_b:
        flag = flag + "0010"
    elif R_a < R_b:
        flag = flag + "0100"
    elif R_a == R_b:
        flag = flag + "0001"

    rpc["FLAGS"] = flag

    rpc["PC"] = rpc["PC"]+1

    return rpc

# TEST

rpc = {
        "R0": "0001010101010000",
        "R1": "0000000000101000",
        "R2": "0000000010011000",
        "R3": "0000000000000010",
        "R4": "0000000000000000",
        "R5": "0000000000000000",
        "R6": "0000000000000000",
        "FLAGS":"0000000000000000",
        "PC": 10
    }

rpc = cmp("0100000100001100",rpc)

for key,value in rpc.items():
	print(key, ':', value)

# OUTPUT:

# R0 : 0000000000000000
# R1 : 0000000000000010
# R2 : 0000000010011000
# R3 : 0000000000000010
# R4 : 0000000000000000
# R5 : 0000000000000000
# R6 : 0000000000000000
# FLAGS : 0000000000000000
# PC : 11