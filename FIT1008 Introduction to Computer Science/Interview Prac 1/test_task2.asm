    jr $ra
test:   
    # the_list = [2,4,-1] 
    # Allocate the required bytes on the heap via syscall and put the address in the_list
    addi $a0, $t0, 16  # 3 elements plus size = 16 bytes
    addi $v0, $0, 9    # allocate the bytes
    syscall
    sw $v0, the_list   # put start address in the_list
    # set global variable size to 3
    addi $t0, $0, 3    # $t0 = 3
    sw $t0, ($v0)      # start of the_list has correct size (3)
    sw $t0, size       # set the global variable size to the correct value so that the rest works
    # write the value of the elements 2, 4, -1
    addi $t0, $0, 2    # $t0 = 2
    sw $t0, 4($v0)     # the_list[0] = 2
    addi $t0, $0, 4    # $t0 = 4
    sw $t0, 8($v0)     # the_list[1] = 4
    addi $t0, $0, -1   # $t0 = -1
    sw $t0, 12($v0)    # the_list[2] = -1

    # go to compute the minimum of the_list = [2,4,-1] and come back
    jal compute_min    # should print -1

    # the_list = [2] 
    # Allocate the required bytes on the heap via syscall and put the address in the_list
    addi $a0, $t0, 8   # 1 elements plus size = 8 bytes
    addi $v0, $0, 9    # allocate the bytes
    syscall
    sw $v0, the_list   # put start address in the_list
    # set global variable size to 1
    addi $t0, $0, 1    # $t0 = 1
    sw $t0, ($v0)      # start of the_list has correct size (1)
    sw $t0, size       # set the global variable size to the correct value so that the rest works
    # write the value of the element 2
    addi $t0, $0, 2    # $t0 = 2
    sw $t0, 4($v0)     # the_list[0] = 2
    
    # go to compute the minimum of the_list = [2] and come back
    jal compute_min    # should print 2
    
    # the_list = [0,5] 
    # Allocate the required bytes on the heap via syscall and put the address in the_list
    addi $a0, $t0, 12  # 2 elements plus size = 12 bytes
    addi $v0, $0, 9    # allocate the bytes
    syscall
    sw $v0, the_list   # put start address in the_list
    # set global variable size to 2
    addi $t0, $0, 2    # $t0 = 2
    sw $t0, ($v0)      # start of the_list has correct size (2)
    sw $t0, size       # set the global variable size to the correct value so that the rest works
    # write the value of the elements  0,5
    sw $0, 4($v0)      # the_list[0] = 0
    addi $t0, $0, 5    # $t0 = 5
    sw $t0, 8($v0)     # the_list[1] = 5

    # go to compute the minimum of the_list = [0,5] and come back
    jal compute_min    # should print 0

    # the_list = [] 
    # Allocate the required bytes on the heap via syscall and put the address in the_list
    addi $a0, $t0, 4   # 0 elements plus size = 4 bytes 
    addi $v0, $0, 9    # allocate the bytes
    syscall
    sw $v0, the_list   # put start address in the_list
    # set global variable size to 0
    sw $0, ($v0)       # start of the_list has correct size (0)
    sw $0, size        # set the global variable size to the correct value so that the rest works
    
    # go to compute the minimum of the_list = [] and come back
    jal compute_min    # should print nothing
