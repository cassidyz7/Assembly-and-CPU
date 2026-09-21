li $r01, 6
li $r03, 3
li $r04, -2

#start of loop
#r2 is updated reg, r1 is bounds, r3 is jump amount
beq $r02, $r01, $r03
addi $r02, $r02, 1
j $r04
