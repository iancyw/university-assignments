# Ian_Wong_30612616 
# 15/08/2019
# This program creates a list of a certain size with elements, and the determines the element with the minimum value 

	.data
    	
size_prompt:	.asciiz "Enter list size: "
element_prompt:	.asciiz "Enter element "
min_str:	.asciiz "The minimum element in this list is "
colon_str:	.asciiz ": "
newline_str:	.asciiz "\n"
size:		.word 0
the_list:	.word 0
i:		.word 0
min:		.word 0
item:		.word 0

    	.text
    		# ignore this line, it is for later testing
    		# la $ra, test
    		
		# prints the size_prompt
		la $a0, size_prompt
		addi $v0, $0, 4
		syscall

		# prints the newline_str
		la $a0, newline_str
		addi $v0, $0, 4
		syscall

		# reads an integer from the user
    		addi $v0, $0, 5
    		syscall
    		sw $v0, size
    		
    		# this block determines the size of the array
    		lw $t0, size 	
    		addi $t1, $0, 4
    		mult $t1, $t0
    		mflo $t2
    		
    		# this block allocates memory for the array
    		add $a0, $t2, $t1
    		addi $v0, $0, 9
    		syscall
    
    		# stores the length of the list and the array address
    		sw $v0, the_list
    		sw $t0, ($v0)

list_loop:	# exit loop if i == size, as range(size) is not inclusive of size
		lw $t0, size
		lw $t1, i
		beq $t1, $t0, compute_min
	
		# prints the element prompt
		la $a0, element_prompt
		addi $v0, $0, 4
		syscall
	
		# prints the current iteration number
		lw $a0, i
		addi $v0, $0, 1
		syscall
	
		# prints a oclon after the iteration number
		la $a0, colon_str
		addi $v0, $0, 4
		syscall
	
		# prints a new line
		la $a0, newline_str
		addi $v0, $0, 4
		syscall

		# read the integer from user, put into $t0
		addi $v0, $0, 5
		syscall
		add $t0, $0, $v0
	
		# this block of code is used insert the integer into the array
		lw $t1, the_list 	# loads the address of the array; $t1 = the_list
		lw $t2, i		# loads the current iteration number
		addi $t3, $0, 4 	# $t3 = 4
		mult $t2, $t3 		# multiplies i by 4
		mflo $t4 		# $t4 = i*4
		add $t4, $t4, $t3 	# $t4 = 4 + (i*4)
		add $t4, $t4, $t1	# points to the next location in the list; $t4 = array_address + 4 + (i*4)
		sw $t0, ($t4)		# stores the read integer into the array; the_list[i] = $t0
		addi $t2, $t2, 1	# increases i by 1; $t2 = i + 1
		sw $t2, i		# stores the new i number
		
		# jumps back to the beginning of the list_loop
		j list_loop

compute_min:	# this block exits if size < 0 (therefore not size > 0), jumping directly to the exit syscall
		lw $t0, size
		slti $t1, $t0, 0
		bne $t1, $0, exit
		
		# this block of codes sets the min as the contents in the first index of the array
		lw $t0, the_list	# sets $t0 as the array address
		lw $t1, 4($t0) 		# loads from address stored in the_list + 4 (the_list[0])
		sw $t1, min 		# sets the contents of $t1 into min; min = $t1
		
		# this block of code sets the i to 1, when entering the loop for the first time, as its from 1 to size - 1
		addi $t0, $0, 1
		sw $t0, i
		
		
min_loop:	# this for loop exits if i == size, with i beginning at 1
		lw $t0, size
		lw $t1, i
		beq $t0, $t1, print
		
		# this block of codes sets item as the the current iteration index
		lw $t0, the_list 	# loads the array address into $t0; $t0 = array_address
		lw $t1, i		# loads the current iteration number; $t1 = i
		addi $t2, $0, 4		# $t2 = 4
		mult $t1, $t2		# $t1 * $t2 = i * 4
		mflo $t3 		# $t3 = i*4
		add $t3, $t3, $t2 	# $t3 = 4 + (i*4)
		add $t3, $t0, $t3	# loads the next location on the array; $t3 = array_address + 4 + (i*4)
		lw $t4, ($t3)		# loads the contents at array_address + 4 + (i*4) into $t4
		sw $t4, item		# sets the contents at the_list[i] as the current item
		
		# this block of code checks if min > item
		lw $t0, item 		# $t0 = item
		lw $t1, min		# $t1 = min
		lw $t2, i
		slt $t3, $t0, $t1	# $t3 = 1 if item < min, else $t3 = 0
		bne $t3, $0, set_min	# branches only if item < min; else continues the loop
		addi $t2, $t2, 1	# increases i by 1; $t2 = i + 1
		sw $t2, i		# stores the new i number
		
		j min_loop
		
set_min:	# this block of code sets min as item
		lw $t0, item
		sw $t0, min
		lw $t1, i
		addi $t1, $t1, 1	# increases i by 1; $t2 = i + 1
		sw $t1, i		# stores the new i number
		
		j min_loop
		
print:		# this block prints out the min_str
		la $a0, min_str
		addi $v0, $0, 4
		syscall
		
		# this block of code prints out the min of the array
		lw $a0, min
		addi $v0, $0, 1
		syscall
		
		# this block prints a new line
		la $a0, newline_str
		addi $v0, $0, 4
		syscall
		
exit:    	# Exit the program
    		addi $v0, $0, 10
    		syscall
