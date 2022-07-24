import csv

with open('../resources/report.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



f = csv.DictReader('resources/report.csv', 'r')
print(f.line_num())
