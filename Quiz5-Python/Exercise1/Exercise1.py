import csv

students = []
with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['age'] = int(row['age'])
        row['grade'] = int(row['grade'])
        students.append(row)

totalGrades = sum(s['grade'] for s in students)
averageGrades = totalGrades / len(students)

highestGrade = max(students, key=lambda s: s['grade'])
print(highestGrade)

with open('top_students.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for s in students:
        if s['grade'] >80:
            writer.writerow([s['name'], s['grade']])

with open('students_updated.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'grade', 'status']) ## for the header
    for s in students:
        if s['grade'] > 80:
            status = 'passed'
        else:
            status = 'failed'
        writer.writerow([s['name'], s['grade'], status])

