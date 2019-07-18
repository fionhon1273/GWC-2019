# friends = {
#     "Christina":16,
#     "Alana":17,
#     "Chris":12,
#     "Eyton":13,
#     "Rachel":15,
#     "Gigi":20
#     }
# print(friends)
# print(friends["Gigi"])hjghjgh
#
import json

def takesurvey(questions, answers):
    answer = {}
    for q in questions:
        answer[q] = input(q)
    answers.append(answer)


answers = []
questions = ["What is your name? ",
"What month were you born in? ",
"What is your favorite color? ",
"How many siblings do you have? ",
"What is your favorite animal? "]

for i in range(5):
    takesurvey(questions, answers)


# json.dumps(answers)
f = open("survey.json","w")
f.write(json.dumps(answers))
f.close()
