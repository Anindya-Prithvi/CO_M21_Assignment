def mov(mov_instruction):
    register = {'R0':'000',
                'R1':'001',
                'R2':'010',
                'R3':'011',
                'R4':'100',
                'R5':'101',
                'R6':'110',
                }
    list = mov_instruction.split(" ")
    if (len(list)<3):
        return "ERROR:INCOMPLETE INSTRUCTION"
    if list[0]!="mov":
        return "ERROR:ILLEGAL ARGUMENT";
    if list[2] in register:
        c=0
        bin_string = "0011100000"
        for j in range(1,3):
            for i in register:
                if i==list[j]:
                    bin_string=bin_string+register[i]
                    c=0
                    break
                else:
                    c=1
            if c==1:
                return "ERROR:INVALID REGISTER CODE"
        return bin_string
    
    else:
        c=0
        bin_string="00010"
        list[2]=list[2][1:]
        num = int (list[2])
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

# instruct="mov R1 $1"
# print(mov(instruct))

# instruct="mov R1 R2"
# print(mov(instruct))