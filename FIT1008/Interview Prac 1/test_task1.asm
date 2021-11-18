    		.data
	
x:		.word 4
y:		.word 5
result:		.word 0
    
    
    		.text

test:
    # test a = 11, b = 50, result should be 4 (b//a)
    addi $t0, $0, 11   # $t0 = 11
    sw $t0, x          # a = 11
    addi $t0, $0, 50   # $t0 = 50
    sw $t0, y          # b = 50
    jal if              # execute the if and come back
    
    # test a = -1, b = -1, result should be 1 (a*b)
    addi $t0, $0, -1   # $t0 = -1
    sw $t0, x          # a = -1
    sw $t0, y          # b = -1
    jal if              # execute the if and come back
    
    # test a = 20, b = 13, result should be 6 (b//2)
    addi $t0, $0, 20   # $t0 = 20
    sw $t0, x          # a = 20
    addi $t0, $0, 13   # $t0 = 13
    sw $t0, y          # b = 13
    jal if             # execute the if and come back
    
    j exit             # finish the program

		# this block of code are the first set of if conditions (if a > 0 and a <= b)
if:		lw $t0, x
		lw $t1, y
		slti $t2, $t0, 0 	# if not a > 0 (a < 0), $t2 = 1; else $t2 = 0
		bne $t2, $0, elif 	# if $t2 != 0, goto elif
		slt $t3, $t1, $t0 	# if not a <= b (b < a), set $t3 - 1; else $t3 = 0
		bne $t3, $0, elif  	# if $t3 != 0, goto elif; else continue to 'if_result' block
	
		# this block of code only runs if all conditions in the 'if' block are true; sets result = b//a
if_result:	lw $t0, x
		lw $t1, y
		div $t1, $t0 	# divides b by a, moving the quotient to lo register and the overflow/remainder to hi register
		mflo $t3 	# moves the quotient from lo register to $t3 register
		sw $t3, result 	# stores the contents of $t3 into the memory address at label 'result'
		j print 	# jumps to 'print' label
		
		# this block of code is the 'elif' block of code, with conditions a == b or b < 0
elif:		lw $t0, x
		lw $t1, y
		beq $t0, $t1, elif_result 	# if a == b is true, goto elif_result
		slt $t2, $0, $t1 		# if not b < 0 (0 < b), set $t2 = 1; else $t2 = 0
		beq $t2, $0, elif_result 	# if $t2 == 0, goto elif_result
		j else 				# jump to 'else' label, as no conditions in this block were met
		
		# this block of code runs if at least one condition in the 'elif' block is satisfied
elif_result:	lw $t0, x 
		lw $t1, y
		mult $t0, $t1 			# multiplies a by b, and moves the result to lo register and over flow to hi register
		mflo $t0 			# $t0 = lo
		sw $t0, result 			# stores the contents of $t0 to the memory address with label 'result'
		j print				# jumps to 'print' label

		# this block runs if the 'if' and 'elif' blocks are not satisfied; sets result = b//2
else:		lw $t0, y
		addi $t1, $0, 2 # # t1 = 2
		div $t0, $t1 			# divides b by 2, storing the quotient in lo register and remainder in hi register
		mflo $t0 			# $t0 = lo
		sw $t0, result 			# stores the contents of $t0 to the memory address with label 'result'
		j print 			# jumps to 'print' label

		# this block of code is used to print the result
print:		lw $a0, result			# loads the contents at 'result' into $a0; $a0 = result
		addi $v0, $0, 1			# calls the service code for printing out an integer; $v0 = 1
		syscall				# issues the system call; prints out result
		
jr $ra

exit:		# exits program
		addi $v0, $0, 10
		syscall
