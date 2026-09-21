import sys


# Bits      12-15   8-11    4-7     0-3
# R-Type    opcode  dest    src1    src2
# I-Type    opcode  dest    src1    imm
# Load Imm  opcode  dest    imm     imm


mnemoics = {    
    'and': 0, #and dest, src1, src2
    'or': 1, # or dest, src1, src2
    'add': 2, # add dest, src1, src2
    'sub': 3, # sub dest, src1, src2
    'slt': 4, # slt dest, src1, src2
    'not': 5, # not dest, src1
    'lshft': 6, # lshft dest, src1
    'rshft': 7, # rshft dest, src1
    'andi': 8, # andi dest, src1, imm
    'ori': 9, # ori dest, src1, imm
    'addi': 10, # addi dest, src1, imm
    'slti': 11, # slti dest, src1, imm
    'li': 12, # li dest, imm
    'beq': 13, # beq src1, src2, dest
    'bne': 14, # bne src1, src2, dest
    'j': 15 # j dest
}

registers = {
    '$zero': 0,
    '$r01': 1,
    '$r02': 2,
    '$r03': 3,
    '$r04': 4,
    '$r05': 5,
    '$r06': 6,
    '$r07': 7,
    '$r08': 8,
    '$r09': 9,
    '$r10': 10,
    '$r11': 11,
    '$r12': 12,
    '$r13': 13,
    '$r14': 14,
    '$r15': 15
}

file = sys.argv[1]

if len(sys.argv) > 2:
    print("Too many args, please only provide one file")
    exit()
elif len(sys.argv) == 1:
    print("Too few args, please only provide one file")
    exit()
elif not (file.endswith(".asm")):
    print("Wrong file extension, please use .asm")
    exit()


output = file.strip('.asm')

try:
    out_bin = open(output + '.bin.txt', 'x')
except:
    out_bin = open(output + '.bin.txt', 'w')

try:
    out_prog = open(output + '.prog.txt', 'x')
except:
    out_prog = open(output + '.prog.txt', 'w')

out_prog.write('v2.0 raw\n')

#todo: add more error checking into this
with open(file) as f:
    for line in f:
        if line.startswith('#') or line == '\n':
            continue
        line = line.split()
        for i in range(len(line)):
            line[i] = line[i].strip(',')

        opcode = line[0]
        op_bin = f'{mnemoics[opcode]:04b}'
        match(opcode):
            case 'li':
                field1 = f'{registers[line[1]]:04b}'
                # field2 = f'{int(line[2]):08b}'
                field2 = format(int(line[2]) & (2**8 - 1), f'08b')
                field3 = ''
            case 'beq':
                field1 = f'{registers[line[3]]:04b}'
                field2 = f'{registers[line[1]]:04b}'
                field3 = f'{registers[line[2]]:04b}'
            case 'bne':
                field1 = f'{registers[line[3]]:04b}'
                field2 = f'{registers[line[1]]:04b}'
                field3 = f'{registers[line[2]]:04b}'
            case 'j':
                field1 = f'{registers[line[1]]:04b}'
                field2 = '0000'
                field3 = '0000'
            case 'lshft' | 'rshft':
                field1 = f'{registers[line[1]]:04b}'
                field2 = f'{registers[line[2]]:04b}'
                field3 = '0000'
            case _:
                if op_bin[0] == '1':
                    # field3 = f'{int(line[3]):04b}'
                    field3 = format(int(line[3]) & (2**4 - 1), f'04b')
                else:
                    field3 = f'{registers[line[3]]:04b}'
                field1 = f'{registers[line[1]]:04b}'
                field2 = f'{registers[line[2]]:04b}'
        instruction_bin = op_bin + field1 + field2 + field3
        out_bin.write(instruction_bin + '\n')

        instruction_hex = f'{int(instruction_bin, base=2):04x}'
        out_prog.write(instruction_hex + ' ')

out_prog.close()

        
out_bin.close()