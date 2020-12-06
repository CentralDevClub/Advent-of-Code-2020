answers = []

with open('input.txt') as file:
    answer = []
    for i in file.readlines():
        if i != '\n':
            for q in i[:-1]:
                if q not in answer:
                    answer.append(q)
        else:
            answers.append(len(answer))
            answer = []
    answers.append(len(answer))

print(sum(answers))
