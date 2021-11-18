# Ian_Wong_30612616
# 15/08/2019
# This program checks conditions against two numbers a and b, and prints a result depending on what conditions it fulfills

		.data
	
x:		.word 4
y:		.word 5
result:		.word 0

		.text
	
if:		# this block of code are the first set of if conditions (if a > 0 and a <= b)
		lw $t0, x
		lw $t1, y
		slti $t2, $t0, 0 	# if not a > 0 (a < 0), $t2 = 1; else $t2 = 0
		bne $t2, $0, elif 	# if $t2 != 0, goto elif
		slt $t3, $t1, $t0 	# if not a <= b (b < a), set $t3 - 1; else $t3 = 0
		bne $t3, $0, elif  	# if $t3 != 0, goto elif; else continue to 'if_result' block
	
if_result:	# this block of code only runs if all conditions in the 'if' block are true; sets result = b//a
		lw $t0, x
		lw $t1, y
		div $t1, $t0 	# divides b by a, moving the quotient to lo register and the overflow/remainder to hi register
		mflo $t3 	# moves the quotient from lo register to $t3 register
		sw $t3, result 	# stores the contents of $t3 into the memory address at label 'result'
		j print 	# jumps to 'print' label
		
elif:		# this block of code is the 'elif' block of code, with conditions a == b or b < 0
		lw $t0, x
		lw $t1, y
		beq $t0, $t1, elif_result 	# if a == b is true, goto elif_result
		slt $t2, $0, $t1 		# if not b < 0 (0 < b), set $t2 = 1; else $t2 = 0
		beq $t2, $0, elif_result 	# if $t2 == 0, goto elif_result
		j else 				# jump to 'else' label, as no conditions in this block were met
		
elif_result:	# this block of code runs if at least one condition in the 'elif' block is satisfied
		lw $t0, x 
		lw $t1, y
		mult $t0, $t1 			# multiplies a by b, and moves the result to lo register and over flow to hi register
		mflo $t0 			# $t0 = lo
		sw $t0, result 			# stores the contents of $t0 to the memory address with label 'result'
		j print				# jumps to 'print' label

else:		# this block runs if the 'if' and 'elif' blocks are not satisfied; sets result = b//2
		lw $t0, y
		addi $t1, $0, 2 # # t1 = 2
		div $t0, $t1 			# divides b by 2, storing the quotient in lo register and remainder in hi register
		mflo $t0 			# $t0 = lo
		sw $t0, result 			# stores the contents of $t0 to the memory address with label 'result'
		j print 			# jumps to 'print' label

print:		# this block of code is used to print the result
		lw $a0, result			# loads the contents at 'result' into $a0; $a0 = result
		addi $v0, $0, 1			# calls the service code for printing out an integer; $v0 = 1
		syscall				# issues the system call; prints out result
		
exit:		# exits program
		addi $v0, $0, 10
		syscall
