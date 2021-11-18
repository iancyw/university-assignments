# Ian_Wong_30612616
# 18/08/2019
# This program reads a list from the user, and prints out the minimum number in that list
	
	.data
	
size_prompt:	.asciiz "Enter list size: "
element_prompt:	.asciiz "Enter element "
colon_str:	.asciiz ": "
newline_str:	.asciiz "\n"

.globl main
.globl get_minimum
.globl read_list

	.text

main:	# copy $sp into $fp
	addi $fp, $sp, 0
	
	# allocate 4 bytes for local variable the_list and result
	addi $sp, $sp, -8
	
	# calls read_list function
	jal read_list
	
	# stores return value in the_list
	sw $v0, -4($fp)
	
	# allocate 4 bytes for arguments
	addi $sp, $sp, -4
	
	# arg = the_list
	lw $t0, -4($fp)
	sw $t0, 0($sp)
	
	jal get_minimum
	
	# remove argument
	addi $sp, $sp, 4
	
	# stores return value in result
	sw $v0, -8($fp)
	
	# print result
	lw $a0, -8($fp)
	addi $v0, $0, 1
	syscall
	
	# prints the newline_str
	la $a0, newline_str
	addi $v0, $0, 4
	syscall
	
	# removes local variables for main
	addi $sp, $sp, 8
	
exit:	# exits the program
	addi $v0, $0, 10
	syscall

read_list:	# save $ra and $fp
		addi $sp, $sp, -8
		sw $ra, 4($sp)
		sw $fp, 0($sp)
		
		# copy $sp into $fp
		addi $fp, $sp, 0
	
		# allocate 4 bytes for local variable size, the_list and i
		addi $sp, $sp, -12
		
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
    		sw $v0, -4($fp)
    		
    		# this block determines the size of the array
    		lw $t0, -4($fp)	
    		addi $t1, $0, 4
    		mult $t1, $t0
    		mflo $t2
    		
    		# this block allocates memory for the array
    		add $a0, $t2, $t1
    		addi $v0, $0, 9
    		syscall
    
    		# stores the length of the list and the array address
    		sw $v0, -8($fp)
    		sw $t0, ($v0)
    		
    		# sets i to 0
    		addi $t0, $0, 0
    		sw $t0, -12($fp)

	list_loop:	# exit loop if i == size, as range(size) is not inclusive of size
			lw $t0, -4($fp)
			lw $t1, -12($fp)
			beq $t1, $t0, list_endif
	
			# prints the element prompt
			la $a0, element_prompt
			addi $v0, $0, 4
			syscall
	
			# prints the current iteration number
			lw $a0, -12($fp)
			addi $v0, $0, 1
			syscall
	
			# prints a colon after the iteration number
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
			lw $t1, -8($fp) 	# loads the address of the array; $t1 = the_list
			lw $t2, -12($fp)	# loads the current iteration number
			addi $t3, $0, 4 	# $t3 = 4
			mult $t2, $t3 		# multiplies i by 4
			mflo $t4 		# $t4 = i*4
			add $t4, $t4, $t3 	# $t4 = 4 + (i*4)
			add $t4, $t4, $t1	# points to the next location in the list; $t4 = array_address + 4 + (i*4)
			sw $t0, ($t4)		# stores the read integer into the array; the_list[i] = $t0
			addi $t2, $t2, 1	# increases i by 1; $t2 = i + 1
			sw $t2, -12($fp)	# stores the new i number
		
			# jumps back to the beginning of the list_loop
			j list_loop

	list_endif:	# return result
			lw $v0, -8($fp)

			# destroys local variables (size and the_list)
			addi $sp, $sp, 12

			# function exit
			lw $fp, 0($sp) # loads the saved frame pointer
			lw $ra, 4($sp) # loads the saved return address
			addi $sp, $sp, 8 # destroys the saved $fp and $ra
			jr $ra # jumps back to caller main()


get_minimum:	# save $ra and $fp
		addi $sp, $sp, -8
		sw $ra, 4($sp)
		sw $fp, 0($sp)
		
		# copy $sp into $fp
		addi $fp, $sp, 0
	
		# allocate 16 bytes for local variables
		addi $sp, $sp, -16

		# sets size as len(the_list)
		lw $t0, 8($fp)
		lw $t1, 0($t0)
		sw $t1, -4($fp)
		
		# this block exits if size < 0 (therefore not size > 0), jumping directly to the exit syscall
		lw $t0, -4($fp)
		slti $t1, $t0, 0
		bne $t1, $0, size_endif
		
		# this block of codes sets the min as the contents in the first index of the array
		lw $t0, 8($fp)		# sets $t0 as the array address
		lw $t1, 4($t0) 		# loads from address stored in the_list + 4 (the_list[0])
		sw $t1, -8($fp) 	# sets the contents of $t1 into min; min = $t1
		
		# this block of code sets the i to 1, when entering the loop for the first time, as its from 1 to size - 1
		addi $t0, $0, 1
		sw $t0, -12($fp)
		
		
	min_loop:	# this for loop exits if i == size, with i beginning at 1
			lw $t0, -4($fp)
			lw $t1, -12($fp)
			beq $t0, $t1, min_endif
		
			# this block of codes sets item as the the current iteration index
			lw $t0, 8($fp) 		# loads the array address into $t0; $t0 = array_address
			lw $t1, -12($fp)	# loads the current iteration number; $t1 = i
			addi $t2, $0, 4		# $t2 = 4
			mult $t1, $t2		# $t1 * $t2 = i * 4
			mflo $t3 		# $t3 = i*4
			add $t3, $t3, $t2 	# $t3 = 4 + (i*4)
			add $t3, $t0, $t3	# loads the next location on the array; $t3 = array_address + 4 + (i*4)
			lw $t4, ($t3)		# loads the contents at array_address + 4 + (i*4) into $t4
			sw $t4, -16($fp)	# sets the contents at the_list[i] as the current item
		
			# this block of code checks if min > item
			lw $t0, -16($fp) 	# $t0 = item
			lw $t1, -8($fp)		# $t1 = min
			lw $t2, -12($fp)
			slt $t3, $t0, $t1	# $t3 = 1 if item < min, else $t3 = 0
			bne $t3, $0, set_min	# branches only if item < min; else continues the loop
			addi $t2, $t2, 1	# increases i by 1; $t2 = i + 1
			sw $t2, -12($fp)	# stores the new i number
		
			j min_loop
		
	set_min:	# this block of code sets min as item
			lw $t0, -16($fp)
			sw $t0, -8($fp)
			lw $t1, -12($fp)
			addi $t1, $t1, 1	# increases i by 1; $t2 = i + 1
			sw $t1, -12($fp)	# stores the new i number
		
			j min_loop

	size_endif:	# return result
			lw $v0, -8($fp)
			
			# destroys local variables (size and the_list)
			addi $sp, $sp, 16
			
			# function exit
			lw $fp, 0($sp) # loads the saved frame pointer
			lw $ra, 4($sp) # loads the saved return address
			addi $sp, $sp, 8 # destroys the saved $fp and $ra
			jr $ra # jumps back to caller main()
	
	min_endif:	# return result
			lw $v0, -8($fp)
			
			# destroys local variables (size and the_list)
			addi $sp, $sp, 16
			
			# function exit
			lw $fp, 0($sp) # loads the saved frame pointer
			lw $ra, 4($sp) # loads the saved return address
			addi $sp, $sp, 8 # destroys the saved $fp and $ra
			jr $ra # jumps back to caller main()
