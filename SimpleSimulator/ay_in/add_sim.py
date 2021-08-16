#add reg1 reg2 reg3=00000 00 001 010 011
def add_instruction(instruct,reg):
    if instruct[:5]!="00000":
        return "ERROR:ILLEGAL INSTRUCTION"
    
    register = {
        "R0": "000",
        "R1": "001",
        "R2": "010",
        "R3": "011",
        "R4": "100",
        "R5": "101",
        "R6": "110",
        "FLAGS":"111"
    }
    if instruct[7:10]==register["FLAGS"] or instruct[10:13]==register["FLAGS"] or instruct[13:]==register["FLAGS"]:
        return "ERROR:FLAG REGISTER WAS ACCESSED"
    
    reg["FLAGS"] = "0"*16 
    
    cx,cy,cz=0,0,0
    
    for key in register:
        if register[key]==instruct[7:10]:
            cx=1
            key1=key
        elif register[key]==instruct[10:13]:
            cy=1
            key2=key
        elif register[key]==instruct[13:]:
            cz=1
            key3=key
    if cx==0 or cy==0 or cz==0:
        return "ERROR:INVALID REGISTER"
    x = int(reg[key2],2)
    y = int(reg[key3],2)
    z = x+y
    if z>int ("1111111111111111",2):
        z=0
        reg["FLAGS"]="0000000000001000"
        reg[key1] = format(z,"016b")
        reg["PC"] = reg["PC"]+1
        return reg
    
    reg[key1] = format(z,"016b")
    reg["PC"] = reg["PC"]+1
    return reg

#test
# rpc = {
#         "R0": "0000000000000000",
#         "R1": "0000000000000000",
#         "R2": "0000000000000001",
#         "R3": "0000000000000010",
#         "R4": "0000000000000000",
#         "R5": "0000000000000000",
#         "R6": "0000000000000000",
#         "FLAGS":"0000000000000000",
#         "PC": 10
#     }

# print(add_instruction("0000000001010011",rpc))
