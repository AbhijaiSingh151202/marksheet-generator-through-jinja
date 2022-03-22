import csv
with open('student_marks.csv', 'r') as f:
    content = csv.reader(f, delimiter=',')
    for line_number, line in enumerate(content):
        if line_number == 0:
            continue
        else:
            print(line)
