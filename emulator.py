import sys

registers = {
    '$zero': 0,
    '$r01': 0,
    '$r02': 0,
    '$r03': 0,
    '$r04': 0,
    '$r05': 0,
    '$r06': 0,
    '$r07': 0,
    '$r08': 0,
    '$r09': 0,
    '$r10': 0,
    '$r11': 0,
    '$r12': 0,
    '$r13': 0,
    '$r14': 0,
    '$r15': 0
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

#in actuality the pc will get updated by 2, but for this itll only be one
pc = 0

with open(file) as f:
    lines = [line for line in f.readlines() if line.strip() and not line.startswith('#')]
    file_len = len(lines)
    while pc < file_len:
        pc_shift = 1
        line = lines[pc]
        line = line.split()
        line_len = len(line)
        for i in range(line_len):
            line[i] = line[i].strip(',')
        
        opcode = line[0]
        dest = line[1]
        field2 = line[2] if line_len >= 3 else None
        field3 = line[3] if line_len == 4 else None

        match (opcode):
            case 'and':
                src1 = registers[field2]
                src2 = registers[field3]
                if dest != "$zero":
                    registers[dest] = src1 & src2
            case 'or':
                src1 = registers[field2]
                src2 = registers[field3]
                if dest != "$zero":
                    registers[dest] = src1 | src2
            case 'add':
                src1 = registers[field2]
                src2 = registers[field3]
                if dest != "$zero":
                    registers[dest] = src1 + src2
            case 'sub':
                src1 = registers[field2]
                src2 = registers[field3]
                if dest != "$zero":
                    registers[dest] = src1 - src2
            case 'slt':
                src1 = registers[field2]
                src2 = registers[field3]
                if dest != "$zero":
                    registers[dest] = 1 if src1 < src2 else 0
            case 'not':
                src1 = registers[field2]
                if dest != "$zero":
                    registers[dest] = ~src1
            case 'lshft':
                src1 = registers[field2]
                if dest != "$zero":
                    registers[dest] = src1 << 1
            case 'rshft':
                src1 = registers[field2]
                if dest != "$zero":
                    registers[dest] = src1 >> 1
            case 'andi':
                src1 = registers[field2]
                imm = int(field3)
                if dest != "$zero":
                    registers[dest] = src1 & imm
            case 'ori':
                src1 = registers[field2]
                imm = int(field3)
                if dest != "$zero":
                    registers[dest] = src1 | imm
            case 'addi':
                src1 = registers[field2]
                imm = int(field3)
                if dest != "$zero":
                    registers[dest] = src1 + imm
            case 'slti':
                src1 = registers[field2]
                imm = int(field3)
                if dest != "$zero":
                    registers[dest] = 1 if src1 < imm else 0
            case 'li':
                imm = int(field2)
                if dest != "$zero":
                    registers[dest] = imm

            #all 3 of these will use relative addressing
            #where the dest reg has the number of instructions to move over
            #negative being backwards in the execution, and positive being forwards
            #basically the line numbers of the program
            case 'beq':
                field2 = line[1]
                field3 = line[2]
                dest = line[3]

                if registers[field2] == registers[field3]:
                    pc_shift = registers[dest]
            case 'bne':
                field2 = line[1]
                field3 = line[2]
                dest = line[3]

                if registers[field2] != registers[field3]:
                    pc_shift = registers[dest]

            case 'j':
                pc_shift = registers[dest]
        pc += pc_shift

print(registers)