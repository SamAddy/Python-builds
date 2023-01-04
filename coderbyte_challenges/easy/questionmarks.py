def questions_marks(strparam):
    count_q = 0
    a = 0
    start_count = False
    true_exist = False
    for i in strparam:
        if start_count and i == '?':
            count_q += 1
        if i.isdigit():
            a += int(i)
            if a==10 and count_q == 3:
                true_exist = True
            if start_count and a == 10 and count_q != 3:
                return 'false'
            a = int(i)
            count_q = 0
            start_count = True
    return 'true' if true_exist else 'false'


print(questions_marks("aa6?9"))
