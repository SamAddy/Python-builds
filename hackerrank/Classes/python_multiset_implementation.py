"""
Python: Multiset Implementation
A multiset is the same as a set except that an element might occur more than once in a multiset. Implement a multiset data structure in Python. Given a template for the Multiset class, implement 4 methods:
• add(self, val) adds val to the multiset
2
﻿﻿remove(self, val), if valis in the multiset, removes va/from the multiset: otherwise, do nothing
﻿﻿_contains_(self, val): returns True if val is in the multiset: otherwise, it returns False
﻿_len_ (self): returns the number of elements in the multiset
Additional methods are allowed as necessary.
The implementations of the 4 required methods will be tested by a provided code stub on several input files. Each input file contains several operations, each of one of the below types. Values returned by query and size operations are appended to a result list, which is printed as the output by the provided code stub.
﻿﻿add val: calls add(val) on the Multiset instance
﻿﻿remove val: calls remove(val) on the Multiset instance
﻿﻿query val: appends the result of expression val in m, where mis an instance of Multiset, and appends the value of that expression to the result list
﻿﻿size: calls len(m), where mis an instance of Multiset, and appends the returned value to the result list
Complete the class Multiset in the editor below with the 4 methods given above (add. remove, _contains__ and __len_.
Constraints
﻿﻿1 ≤ number of operations in one test file $ 105
﻿﻿If valis a parameter of operation, then val is an integer and 1 ≤ val $ 109
+ Input Format Format for Custom Testing
In the first line, there is a single integer, q, denoting the number of queries.
Then, q lines follow. In the th of them, there is a string denoting an operation and
"""
#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:
    def __init__(self):
        self.my_store = []

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        return self.my_store.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        return self.my_store.remove(val) if self.__contains__(val) else False

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.my_store

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.my_store)


if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result


    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()