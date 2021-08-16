def hlt_instruction(instruct,reg):
    if instruct!="1001100000000000":
        return "ERROR:ILLEGAL INSTRUCTION"
    reg["PC"]=reg["PC"]+1
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
# print(hlt_instruction("1001100000000000",rpc))