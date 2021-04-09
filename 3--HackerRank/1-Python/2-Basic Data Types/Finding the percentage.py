if __name__ == '__main__':
    student_marks = {}
    for n in range(int(input())):

        name, *line = input().split()

        scores = list(map(float, line))

        student_marks[name] = scores
    query_name = input()

    all_f_number = student_marks[query_name]
    result = sum(all_f_number)/len(all_f_number)
    print('%.2f'%result)
