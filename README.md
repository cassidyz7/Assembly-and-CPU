Custom CPU and Assembly Language

This was created to become more familiar with the process of designing and implementing a CPU based on specifications for an assembly language. The assembly language used was also created for this, as I wanted a simplified and more stripped down version of MIPS, which was being used in my CSCI 250: Concepts of Computer Systems course.

This was a way for me to both work on an interesting and fun project while also studying for the exam on this material.

The circuits were built in Logisim 2.3.1 and the assembler and emulators were written in python.

HOW TO USE:
Write your program in a file with the `.asm` extension.
Run the emulator program with your file as a command line input.
Example: `assembler.py {file_name}.asm`

This will output 2 files, `{file_name}.prog.txt` and `{file_name}.bin.txt`

`{file_name}.bin.txt` is a file that contains the actual binary strings that correspond to the instruction that was written.
`{file_name}.prog.txt` is a file that contains the instructions written in hexadecimal so that they can be pasted into the program memory of the CPU in logisim and then ran.

To use the emulator, run `emulator.py {file_name}.asm` to directly interpret the text and run the program. I would reccomend doing this first so you know what to expect the outputs of the CPU to look like


LANGUAGE SPECIFICATIONS
This lanauge uses 16, 16-bit registers and has 16 different instructions.

| Bits | 15-12 | 11-8 | 7-4 | 3-0 |
| -------- | -------- | -------- | -------- | -------- |
| R-Type | opcode | dest | scr1 | src2 |
| I-Type | opcode | dest | src1 | imm |
| Load Imm | opcode | dest | imm | imm |

The Load Immediate instruction having a larger immediate field is so that you can have larger numbers loaded in than just using the I-type instructions.
Is this a weird workaround because I chose such a small instruction length and kept everything 16? Yes. Does it still work fine for doing basic programs which was the intented use of this? Yes.

INSTRUCTIONS

Any line with a hashtag (#) at the beginning will be considered a comment. This is the only way to do comments.

Each line can have at most one instruction.

| Opcode (decimal) | Opcode (binary) | Assembly instruction
| -------- | -------- | -------- |
|0| 0000 |and dest, src1, src2
|1| 0001|or dest, src1, src2
|2|0010|add dest, src1, src2
|3|0011|sub dest, src1, src2
|4|0100|slt dest, src1, src2
|5|0101|not dest, src1
|6|0110|lshft dest, src1
|7|0111|rshft dest, src1
|8|1000|andi dest, src1, imm
|9|1001|ori dest, src1, imm
|10|1010| addi dest, src1, imm
|11|1011| slti dest, src1, imm
|12|1100| li dest, imm
|13|1101| beq src1, src2, dest
|14|1110| bne src1, src2, dest
|15|1111| j dest

