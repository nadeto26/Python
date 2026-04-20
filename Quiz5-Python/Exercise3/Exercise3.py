import json

try:
    salary = 0
    with open('data.json') as f:
        data = json.load(f)
        for employee in data['employees']:
            print(employee['name'])
            salary += employee['salary']

except FileNotFoundError:
    print('File not found')

with open('newData.json', 'w') as f:
    new_data = {
        'name': 'Nade',
        'salary': 5000
    }
    data['employees'].append(new_data)
    json.dump(data, f)


