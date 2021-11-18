from assignment1 import radix_sort, time_radix_sort, find_rotations

if __name__ == '__main__':
    radix_sort_number_list_inputs = [
    #Place lists of integers for radix sort to test here
        
    [],      #empty list
    [1,2,3,4,5],     #single digits, sorted
    [4,3,2,1],       #single digits, reverse sorted
    [23,1,2,67,23,4,2],      #repeated numbers

    #
        ]

    radix_sort_base_inputs = [
    #Place the corresponding base numbers for radix sort here

    7,
    2,
    5,
    9,

    #
        ]

    radix_sort_expected_results = [
    #Place the corresponding expected results - the sorted list in base 10 display- here

    [],
    [1,2,3,4,5],
    [1,2,3,4],
    [1,2,2,4,23,23,67],

    #
        ]

    find_rotations_string_list_inputs = [
    #Place the list of strings for find_rotations here

    [],      #empty list
    ['abc','defg','hij','klmnop','qrstuvw'],        #result should be an empty list
    ['qwertyui','wertyuiq','rtyuiqwe','asdfgh','dfghas'],        #p = 2
    ['abcdefgh','ghabcdef','qwerty','qwerty','ertyqw'],      #p = -2
    ['zxcvbnm','abcde','blahblah','ahblahbl','vbnmzxc'],      #p > length of largest string

    #
        ]

    find_rotations_p_value_inputs = [
    #Place the corresponding p values for p rotations

    3,
    1,
    2,
    -2,
    10,

    #
        ]

    find_rotations_expected_results = [
    #Place the corresponding expected results here

    [],
    [],
    ['asdfgh','wertyuiq'],
    ['abcdefgh','ertyqw'],
    ['zxcvbnm','abcde','blahblah','ahblahbl'],

    #
        ]

#ignore everything else below here


class Test():
    
    def __init__(self):
        self.failures = []
        self.failed = False
        self.tests_ran_RS = 0
        self.tests_ran_FR = 0
        
    def test_radix_sort(self,input_list,base_list,result_list):
        for i in range(min(len(result_list),len(base_list),len(input_list))):
            self.test_function_radix_sort(input_list[i],base_list[i],result_list[i])
            self.tests_ran_RS += 1
        if len(result_list) != len(base_list) or len(result_list) != len(input_list) or len(input_list) != len(base_list):
            print("warning: there is a difference in the number of inputs, bases, and results supplied for radix sort")
        
    def test_find_rotations(self,input_list,base_list,result_list):
        for i in range(min(len(result_list),len(base_list),len(input_list))):
            self.test_function_find_rotations(input_list[i],base_list[i],result_list[i])
            self.tests_ran_FR += 1
        if len(result_list) != len(base_list) or len(result_list) != len(input_list) or len(input_list) != len(base_list):
            print("warning: there is a difference in the number of inputs, bases, and results supplied for find rotations")


    def test_function_radix_sort(self,inpt,base,result):
        try:
            res = radix_sort(inpt,base)
            if res != result:
                self.failures.append("Failure for radix_sort{0}: returned {1}, expected {2}".format((inpt,base),res,result))
                self.failed = True
        except Exception as e:
            self.failed = True
            self.failures.append("Error occured when running radix_sort{0}: {1}".format((inpt,base),e))
            
    def test_function_find_rotations(self,inpt,p,result):
        try:
            lis = find_rotations(inpt,p)
            flag = True
            for i in lis:
                if i not in result:
                    self.failures.append("Failure for find_rotations{0}: returned {1}, expected {2}".format((inpt,p),lis,result))
                    flag = False
                    self.failed = True
                    break
            if flag:
                for i in result:
                    if i not in lis:
                        self.failures.append("Failure for find_rotations{0}: returned {1}, expected {2}".format((inpt,p),lis,result))
                        self.failed = True
                        break
        except Exception as e:
            self.failed = True
            self.failures.append("Error occured when running find_rotations{0}: {1}".format((inpt,p),e))


    def print_results(self):
        print("ran {0} tests for radix_sort and {1} tests for find_rotations".format(self.tests_ran_RS,self.tests_ran_FR))
        if self.failed:
            print("\nSome tests failed:\n")
            for i in self.failures:
                print(i)
                print('')
        else:
            print("\nAll tests passed :)")

if __name__ == '__main__':
    test = Test()
    print("running tests...")
    test.test_radix_sort(radix_sort_number_list_inputs,radix_sort_base_inputs,radix_sort_expected_results)
    test.test_find_rotations(find_rotations_string_list_inputs,find_rotations_p_value_inputs,find_rotations_expected_results)
    test.print_results()
