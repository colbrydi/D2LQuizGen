from d2lquizgen import quiz
from d2lquizgen import latex

import random
from random import randint
from random import randrange
import numpy as np

includePython=True

#####################
## 2x2 Determinant ##
#####################
 
def determinant2x2(M):
    return M[0,0]*M[1,1] - M[0,1]*M[1,0]

def determinant2x2_wrong1(M):
    return M[0,0]*M[1,0] - M[1,1]*M[1,0] + M[0,0]*M[1,1]

def determinant2x2_wrong2(M):
    return M[0,1]*M[1,0] - M[0,0]*M[1,1]

def determinant2x2_wrong3(M):
    return M[0,0]*M[0,1] + M[1,0]*M[1,1] +1

def random_int_matrix(m,n,minval=-10,maxval=10):
    return [ [randint(minval,maxval) for i in range(n)] for i in range(m)]

def random_float_matrix(m,n,minval=-10,maxval=10):
    return [ [random.uniform(minval,maxval) for i in range(n)] for i in range(m)]

def random_singular_matrix(n):
    raise NotImplementedError()

def quick_shuffle(it):
    it2 = it.copy()
    for i in range(len(it2)):
        j = randrange(len(it2))
        it2[i], it2[j] = it2[j], it2[i]
    return it2



class determinat_question(quiz.question):
    
    def __init__(self, M = None, points=1, difficulty=1):
        quiz.question.__init__(self)

        if M is None:
            print("making random matrix")
            M = random_int_matrix(2,2)
        M = np.matrix(M)
        tex = latex.latex(M)
        
        self.Title='DeterminateQuestion'
        self.QuestionText=f'<p>Find the determinant of the matrix below.</p> {tex}\n\n'
        if(includePython):
            self.QuestionText +=f'np.matrix([[{M[0,0]},{M[0,1]},[{M[1,0]}, {M[1,1]}]])'
            
        self.points = points
        self.difficulty = difficulty
        self.Options = [f'determinant = {determinant2x2(M)}',
                        f'determinant = {determinant2x2_wrong1(M)}',
                        f'determinant = {determinant2x2_wrong2(M)}',
                        f'determinant = {determinant2x2_wrong3(M)}']
        self.Answers = [100,0,0,0]
        
###########################
## solve_system_question ##
###########################
            
class solve_system_question(quiz.question):
    
    def __init__(self,M=None,b=None,
                 wrong_sols=[],
                 points=1,
                 difficulty=1):
        quiz.question.__init__(self)

        if M is None:
            print("making random matrix")
            M = random_int_matrix(2,2)
        M = np.matrix(M)
        
        if b is None:
            print("making random matrix")
            b = random_int_matrix(2,1)
        b = np.matrix(b)
        
        correct_sol = np.linalg.solve(M,b)
        print(f"Solution = {correct_sol}")
        #correct_sol = list(correct_sol)
        

        while len(wrong_sols) < 3:
            err = random_float_matrix(2,1)
            if not (np.matrix(err)==np.matrix(correct_sol)).all():
                err = list(err)
                wrong_sols.append(err)
                
        sys = latex.mat2system(M,b)
        
        self.Title=f'SolveSystemQ'
        self.QuestionText=f'Solve the following system of equations.{sys}\n\n'
            
        self.points = points
        self.difficulty = difficulty
        
        self.Options = []
        self.Answers = []
        if isinstance(correct_sol,str):
            if correct_sol == "No Solution":
                self.Options.append('{correct_sol}')
                self.Answers.append(100)
        else:
            solution = latex.sol2str(correct_sol)
            self.Options.append(f'{solution}')
            self.Answers.append(100)
            
        for bad in wrong_sols:
            solution = latex.sol2str(bad)
            self.Options.append(f'{solution}')
            self.Answers.append(0)
        
        c = list(zip(self.Options, self.Answers))
        random.shuffle(c)
        self.Options, self.Answers = zip(*c)

###########################
## solve_system_question ##
###########################

class vector_in_nullspace_question(quiz.question):
    
    def __init__(self, q_ind,M,v,is_true,im_name='test',points=1,difficulty=1):
       
        quiz.question.__init__(self)
        
        mat_tex = latex.latex(M,'A=', '')
        vect_tex = latex.latex(v,'v=', '')
        
        self.Title=f'NullspaceQ{str(q_ind)}'
        self.QuestionText=f'Is the vector v in the nullspace of the matrix A?. {mat_tex} {vect_tex}'
        self.points = points
        self.difficulty = difficulty
        
        self.Options = ['Yes','No']

        if is_true:
            self.Answers = [100,0]
        else:
            self.Answers = [0,100]
