#!/usr/bin/python3
class ListADT:
    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == len(self.the_array)

    def __contains__(self, item):
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False
 
    def append(self, item):
        if not self.is_full():
            self.the_array[self.length] = item
            self.length +=1
        else:
            raise Exception('List is full')

    def unsafe_set_array(self,array,length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        if 'test' not in __name__:
            raise Exception('Not runnable')
			
        self.the_array = array
        self.length = length
