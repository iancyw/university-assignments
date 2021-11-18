# Ian_Wong_30612616
# 19/08/2019
# This program reads a list from the user, sorts it using the bubble sort algorithm, and prints out the numbers of the array

	.data

size_prompt:	.asciiz "Enter list size: "
element_prompt:	.asciiz "Enter element "
colon_str:	.asciiz ": "
newline_str:	.asciiz "\n"

.globl main
.globl read_list
.globl bubble_sort

	.text

main:	# set frame pointer as stack pointer
	addi $fp, $sp, 0
	
	# allocate 4 bytes of memory for local variable the_list
	addi $sp, $sp, -4
	
	jal read_list
	
	# stores return value in the_list
	sw $v0, -4($fp)
	
	# allocate 4 bytes for arguments
	addi $sp, $sp, -4
	
	# arg = the_list
	lw $t0, -4($fp)
	sw $t0, 0($sp)
	
	jal bubble_sort
	
	jal print_list
	
	# destroys local variable and argument
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
			lw $fp, 0($sp) 		# loads the saved frame pointer
			lw $ra, 4($sp) 		# loads the saved return address
			addi $sp, $sp, 8 	# destroys the saved $fp and $ra
			jr $ra 			# jumps back to caller main()
	
print_list:	# save $ra and $fp
		addi $sp, $sp, -8
		sw $ra, 4($sp)
		sw $fp, 0($sp)
		
		# copy $sp into $fp
		addi $fp, $sp, 0
	
		# allocate 4 bytes for local variable size and i
		addi $sp, $sp, -8
		
		# sets n as len(the_list)
		lw $t0, 8($fp) 		# retrives the array address; $t0 = array address
		lw $t1, 0($t0) 		# takes the len(array); $t1 = len(the_list)
		sw $t1, -4($fp) 	# stores it in n, at -4($fp)
		
		# sets i to 0
		addi $t0, $0, 0
		sw $t0, -8($fp)
		
	p_loop:	# exits if i == size
		lw $t0, -4($fp) # size
		lw $t1, -8($fp) # i
		beq $t0, $t1, p_end
		
		lw $t0, -8($fp)		# i
		addi $t1, $0, 4		# $t1 = 4
		mult $t0, $t1		# i*4
		mflo $t2		# $t2 = i*4
		add $t2, $t2, $t1	# $t2 = (i*4) + 4
		lw $t3, 8($fp)		# $t3 = array address
		add $t2, $t2, $t3	# $t2 = array address + (i*4) + 4
		lw $a0, ($t2)		
		
		# prints the current number
		addi $v0, $0, 1
		syscall
		
		# prints the newline_str
		la $a0, newline_str
		addi $v0, $0, 4
		syscall
		
		lw $t0, -8($fp)
		addi $t0, $t0, 1
		sw $t0, -8($fp)
		j p_loop
	
	p_end:	# destroys local variables
		addi $sp, $sp, 8
		
		# loads saved ra and fp
		lw $fp, 0($sp)
		lw $ra, 4($sp)
		addi $sp, $sp, 8
		jr $ra	
		
bubble_sort:	# stores ra and fp
		addi $sp, $sp, -8
		sw $ra, 4($sp)
		sw $fp, 0($sp)
	
		# sets fp to sp
		addi $fp, $sp, 0
		
		# allocates 20 bytes of memory for local variables
		addi $sp, $sp, -20
		
		# sets n as len(the_list)
		lw $t0, 8($fp) 		# retrives the array address; $t0 = array address
		lw $t1, 0($t0) 		# takes the len(array); $t1 = len(the_list)
		sw $t1, -4($fp) 	# stores it in n, at -4($fp)
		
		# sets a to 0
		addi $t0, $0, 0
		sw $t0, -8($fp)
	
	a_loop:	# exits if a == n - 1
		lw $t0, -4($fp) # loads n
		addi $t0, $t0, -1 # $t0 = n - 1
		lw $t1, -8($fp) # loads a
		beq $t1, $t0, a_loopend # if a == n - 1, goto a_loopend
		
		# sets i to 0
		addi $t0, $0, 0
		sw $t0, -12($fp)

		i_loop:	# exits if i == n - 1
			lw $t0, -4($fp) # loads n
			addi $t0, $t0, -1 # $t0 = n - 1
			lw $t1, -12($fp) # loads i
			beq $t1, $t0, i_loopend # if i == n - 1, goto i_loopend
			
			# sets item to the_list[i]
			lw $t0, -12($fp) 	# $t0 = i
			lw $t1, 8($fp) 		# $t1 = array address
			addi $t2, $0, 4 	# $t1 = 4
			mult $t0, $t2 		# i*4
			mflo $t3 		# $t2 = i*4
			add $t3, $t3, $t2 	# $t3 = (i*4) + 4
			add $t3, $t3, $t1 	# $t3 = array address + (i*4) + 4
			lw $t4, ($t3) 		# loads the contents at array
			sw $t4, -16($fp) 	# stores the contents into item
			
			# sets item_to_right to the_list[i+1]
			lw $t0, -12($fp) 	# $t0 = i
			lw $t1, 8($fp) 		# $t1 = array address
			addi $t2, $0, 4 	# $t1 = 4
			mult $t0, $t2 		# i*4
			mflo $t3 		# $t2 = i*4
			addi $t3, $t3, 8 	# $t3 = (i*4) + 8
			add $t3, $t3, $t1 	# $t3 = array address + (i*4) + 8
			lw $t4, ($t3) 		# loads the contents at array
			sw $t4, -20($fp) 	# stores the contents into item_to_right
			
			# checks if item > item_to_right
			lw $t0, -16($fp) 	# item
			lw $t1, -20($fp) 	# item_to_right
			slt $t2, $t0, $t1	# sets $t2 to 1 if item < item_to_right; else 0
			beq $t2, $0, swap
			
			# increases i by 1
			lw $t0, -12($fp)
			addi $t0, $t0, 1
			sw $t0, -12($fp)
			
			# jumps back into loop
			j i_loop
			
			swap:	# sets the_list[i] to item_to_right
				lw $t0, -12($fp) 	# $t0 = i
				lw $t1, 8($fp) 		# $t1 = array address
				addi $t2, $0, 4 	# $t1 = 4
				mult $t0, $t2 		# i*4
				mflo $t3 		# $t2 = i*4
				add $t3, $t3, $t2 	# $t3 = (i*4) + 4
				add $t3, $t3, $t1 	# $t3 = array address + (i*4) + 4
				lw $t4, -20($fp) 	# loads the contents of item_to_right
				sw $t4, ($t3) 		# stores the contents of item_to_right at array[i]
				
				# sets the_list[i+1] to item
				lw $t0, -12($fp) 	# $t0 = i
				lw $t1, 8($fp) 		# $t1 = array address
				addi $t2, $0, 4 	# $t1 = 4
				mult $t0, $t2 		# i*4
				mflo $t3 		# $t2 = i*4
				addi $t3, $t3, 8	# $t3 = (i*4) + 8
				add $t3, $t3, $t1 	# $t3 = array address + (i*4) + 8
				lw $t4, -16($fp) 	# loads the contents of item
				sw $t4, ($t3) 		# stores the contents of item at array[i+1]
			
				# increases i by 1
				lw $t0, -12($fp)
				addi $t0, $t0, 1
				sw $t0, -12($fp)
			
				# jumps back into loop
				j i_loop
		
		i_loopend:
			# increases a by 1
			lw $t0, -8($fp)
			addi $t0, $t0, 1
			sw $t0, -8($fp)
			
			# jumps back into loop
			j a_loop
			
	a_loopend:	
		# destroys local variables
		addi $sp, $sp, 20

		# function exit
		lw $fp, 0($sp) 		# loads the saved frame pointer
		lw $ra, 4($sp) 		# loads the saved return address
		addi $sp, $sp, 8 	# destroys the saved fp and ra
		jr $ra 			# jumps back to the return address
