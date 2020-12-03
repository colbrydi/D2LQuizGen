import csv
from d2lquizgen import quiz


def read(quizfile = 'test_question_1.csv'):

    thisquiz = []
    q = None
    with open(quizfile, newline='') as csvfile:
        datafile = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in datafile:
            if len(row) > 0:
                if row[0] == 'NewQuestion':
                    print("new question")
                    if q:
                        thisquiz.append(q)
                    q = quiz.question(Title='',QuestionText='',Options=[],Answers=[])
                if row[0] == 'Title':
                    q.Title = row[1]
                if row[0] == 'QuestionText':
                    q.QuestionText = row[1]
                if row[0] == 'Option':
                    q.Answers.append(float(row[1]))
                    q.Options.append(row[2])
        if q:
            thisquiz.append(q)
        return thisquiz
    
def write(questions, filename='quizfile.csv'):
    with open(filename,"w") as quizfile:
        for q in questions:
            print(f'Exporting question {q.Title}')
            for j in q.export():
                quizfile.write(j+'\n')
            quizfile.write('\n')
    
