from sys import stdin
import sys



Mem = []       # input list
const = 0
for line in stdin:                          # input
    Mem.append(line.replace("\n",""))
    const = const + 1

while const < 256 :                # filling rest 0b
    Mem.append("0000000000000000")
    const = const + 1
        
reg = {"000":"0000000000000000","001":"0000000000000000","010":"0000000000000000","011":"0000000000000000","100":"0000000000000000","101":"0000000000000000","110":"0000000000000000","111":"0000000000000000"}

def bti(a):
    return str(int(a,2))

def itb(b):
    return str(format(int(b),'016b'))

def ity(d):
    return str(format(int(d),'08b'))

def itz(c):
    return str(format(int(c),'032b'))


Pclist =[]       
Pc = 0
halted = False
while (not halted):
    Pclist.append(Pc)    # for bonus
    instruction = Mem[Pc]  # single instruction input
    if (instruction[0:5] == "00000"):                                                 # add
        c = int(bti(reg[instruction[10:13]])) + int(bti(reg[instruction[13:].replace("\r","")]))
        if(c > 65535 ):
            reg[instruction[7:10]] = itz(str(c))[16:]
            reg["111"] = "0000000000001000"            # overflow
        else:
            reg[instruction[7:10]] = itb(str(c))
            reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "00001"):                                                # subtract
        c = int(bti(reg[instruction[10:13]])) - int(bti(reg[instruction[13:].replace("\r","")]))
        if(c < 0 ):
            reg[instruction[7:10]] = itb("0")
            reg["111"] = "0000000000001000"        # overflow
        else:
            reg[instruction[7:10]] = itb(str(c))
            reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1
    
    elif(instruction[0:5] == "00110"):                                              # multiply
        c = int(bti(reg[instruction[10:13]])) * int(bti(reg[instruction[13:].replace("\r","")]))
        if(c > 65535 ):
            reg[instruction[7:10]] = itz(str(c))[16:]
            reg["111"] = "0000000000001000"      # overflow
        else:
            reg[instruction[7:10]] = itb(str(c))
            reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "01010"):                                                          # XOR
        c = itb(str(int(bti(reg[instruction[10:13]])) ^ int(bti(reg[instruction[13:].replace("\r","")]))))
        reg[instruction[7:10]] = c
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1
    
    elif(instruction[0:5] == "01011"):                                                          # or
        c = itb(str(int(bti(reg[instruction[10:13]])) | int(bti(reg[instruction[13:].replace("\r","")]))))
        reg[instruction[7:10]] = c
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "01100"):                                                               # and
        c = itb(str(int(bti(reg[instruction[10:13]])) & int(bti(reg[instruction[13:].replace("\r","")]))))
        reg[instruction[7:10]] = c
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "00010"):                       # move immediate
        reg[instruction[5:8]] = itb(bti(instruction[8:].replace("\r","")))
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "01000"):          # right shift
        a = int(bti(reg[instruction[5:8]]))
        a = a >> int(bti(instruction[8:].replace("\r","")))
        reg[instruction[5:8]] = itb(str(a))
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1
    
    elif(instruction[0:5] == "01001"):          # left shift
        a = int(bti(reg[instruction[5:8]]))
        a = a << int(bti(instruction[8:].replace("\r","")))
        reg[instruction[5:8]] = itb(str(a))
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "00011"):               # mov reg
        reg[instruction[10:13]] = reg[instruction[13:].replace("\r","")]
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "00111"):              # divide
        reg["000"] = itb(str(int(bti(reg[instruction[10:13]])) / int(bti(reg[instruction[13:].replace("\r","")]))))
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "01101"):          # not
        a = int(bti(reg[instruction[13:].replace("\r","")]))
        a = ~a
        reg[instruction[10:13]] = itb(str(a))
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "01110"):          # compare
        a = int(bti(reg[instruction[10:13]]))
        b = int(bti(reg[instruction[13:].replace("\r","")]))
        if(a < b):
            reg["111"] = "0000000000000100"
        elif(a > b):
            reg["111"] = "0000000000000010"
        elif(a == b):
            reg["111"] = "0000000000000001"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1
    
    elif(instruction[0:5] == "00100"):                   # load
        reg[instruction[5:8]] = itb(Mem[int(bti(instruction[8:].replace("\r","")))])
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "00101"):                         # store
        Mem[int(bti(instruction[8:].replace("\r","")))] = reg[instruction[5:8]]
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc = Pc + 1

    elif(instruction[0:5] == "01111"):    # unconditional jump
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
        Pc =  int(bti(instruction[8:].replace("\r","")))

    elif(instruction[0:5] == "10000"):                     # less than jump
        if reg["111"] == "0000000000000100":
            reg["111"] = "0000000000000000"
            sys.stdout.write("\n" + ity(str(Pc))+ " ")
            for i in reg.values():
                sys.stdout.write(i + " ")
            Pc =  int(bti(instruction[8:].replace("\r","")))
        else:
            reg["111"] = "0000000000000000"
            sys.stdout.write("\n" + ity(str(Pc))+ " ")
            for i in reg.values():
                sys.stdout.write(i + " ")
            Pc = Pc + 1

    elif(instruction[0:5] == "10001"):    # greater than jump
        if reg["111"] == "0000000000000010":
            reg["111"] = "0000000000000000"
            sys.stdout.write("\n" + ity(str(Pc))+ " ")
            for i in reg.values():
                sys.stdout.write(i + " ")
            Pc =  int(bti(instruction[8:].replace("\r","")))
        else:
            reg["111"] = "0000000000000000"
            sys.stdout.write("\n" + ity(str(Pc))+ " ")
            for i in reg.values():
                sys.stdout.write(i + " ")
            Pc = Pc + 1

    elif(instruction[0:5] == "10001"):                      # equal jump 
        if reg["111"] == "0000000000000001":
            reg["111"] = "0000000000000000"
            sys.stdout.write("\n" + ity(str(Pc))+ " ")
            for i in reg.values():
                sys.stdout.write(i + " ")
            Pc =  int(bti(instruction[8:].replace("\r","")))
        else:
            reg["111"] = "0000000000000000"
            sys.stdout.write("\n" + ity(str(Pc))+ " ")
            for i in reg.values():
                sys.stdout.write(i + " ")
            Pc = Pc + 1

    elif(instruction[0:5] == "10011"):                      # hlt
        halted = True
        reg["111"] = "0000000000000000"
        sys.stdout.write("\n" + ity(str(Pc))+ " ")
        for i in reg.values():
            sys.stdout.write(i + " ")
    
    
for i in Mem:              # Memory dump
    sys.stdout.write("\n" + i)

  
    

    
    

        

        



    
 