class A0Paper:
    def canBuild(self,A):
        '''
        A_type: Tuple(Int)
        rtype: String
        '''
        if A[0] >= 1:
            return "Possible"
        n = len(A) - 1
        total = 0
        while n > 0:
            total += A[n]/2**n
            n -= 1
        if total >= 1:
            return "Possible"
        return "Impossible"

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

def array_queries(S):
    lst = S.split("\n")
    length = lst[0]
    array = lst[1].split(' ')
    n_queries = lst[2]
    for query in lst[3:]:
        if query
    return(lst)

if __name__ == '__main__':
    array_queries("10\n"
                  "0 3 3 8 0 6 9 3 2 8\n"
                  "5\n"
                  "Increment 3\n"
                  "Increment 1\n"
                  "Left\n"
                  "Increment 5\n"
                  "Right")