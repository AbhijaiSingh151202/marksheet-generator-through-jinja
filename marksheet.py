import csv
from re import template
from jinja2 import Environment, FileSystemLoader

a = []
with open('student_marks.csv', 'r') as f:
    content = csv.reader(f, delimiter=',')
    for line_number, line in enumerate(content):
        if line_number == 0:
            continue
        else:
            # print(line)
            a.append(line)

print(a)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('marksheet.html')

for i in range(0,5):
    with open(a[i][0] + '.html', 'w') as f:
        msg = template.render(a=a[i])
        f.write(msg)