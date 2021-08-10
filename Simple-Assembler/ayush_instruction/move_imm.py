def imm (imm_instruction,num):
    register = {'R0':'000',
                'R1':'001',
                'R2':'010',
                'R3':'011',
                'R4':'100',
                'R5':'101',
                'R6':'110',
                }
    list=imm_instruction.split(" ")
    if list[0]!="mov":
        return "ERROR:ILLEGAL ARGUMENT";
    else:
        c=0
        bin_string="00010"
        for i in register:
            if i==list[1]:
                bin_string=bin_string+register[i]
                c=0
                break
            else:
                c=1
        if c==1:
            return "ERROR:INVALID REGISTER CODE"

    bin_string=bin_string+format(num,'08b')    
    return bin_string
                       


instruct="mov R1"
print(imm(instruct,1))
