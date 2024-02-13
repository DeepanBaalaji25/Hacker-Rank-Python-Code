if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
  # first sum the total marks of the student and the divide with the total length of the student_marks
    print(format(sum(student_marks[query_name])/len(student_marks[query_name]), ".2f"))
