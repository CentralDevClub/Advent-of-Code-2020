answers = []

with open('input.txt') as file:
    answer = {'person':0,'answer':{}}
    for i in file.readlines():
        if i != '\n':
            answer['person'] += 1
            for q in i[:-1]:
                if q not in answer['answer']:
                    answer['answer'][q] = 1
                else:
                    answer['answer'][q] += 1
        else:
            answers.append(answer)
            answer = {'person':0,'answer':{}}
    answers.append(answer)

total_valid = 0
for i in answers:
    valid = []
    for key,val in i['answer'].items():
        if val == i['person']:
            valid.append(val)
    total_valid += len(valid)
print(total_valid)
