"""
sdfds
"""

if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        operation, *values = input().split()

        try:
            if values:
                values = list(map(int, values))
                getattr(my_list, operation, None)(*values)
            else:
                getattr(my_list, operation)()
        except AttributeError:
            print(my_list)

        # if operation == 'insert':
        #     my_list.insert(int(values[0]), int(values[1]))
        # elif operation == 'remove':
        #     my_list.remove(int(values[0]))
        # elif operation == 'append':
        #     my_list.append(int(values[0]))
        # elif operation == 'print':
        #     print(my_list)
        # elif operation == 'sort':
        #     my_list.sort()
        # elif operation == 'pop':
        #     my_list.pop()
        # elif operation == 'reverse':
        #     my_list.reverse()

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print