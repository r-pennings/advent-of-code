groups = [line.split('\n') for line in open("input.txt").read().split('\n\n')]

nr_of_questions = 0
for group in groups:
    answers = {}
    for answer in group:
        for c in answer:
            if c not in answers:
                answers[c] = 1
            else:
                answers[c] += 1
    nr_of_questions += len([a for a in answers.values() if a == len(group)])
print("# of questions", nr_of_questions)
