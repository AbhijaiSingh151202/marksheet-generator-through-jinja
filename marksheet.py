import csv
with open('student_marks.csv', 'r') as f:
    content = csv.reader(f, delimiter=',')
    for i in content:
        print(content[2][1])
