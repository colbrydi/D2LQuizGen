class question():
    
    def __init__(self, Title="Default Question", 
                 QuestionText="What is the meaning of life",
                 qtype = "MC",
                 Options = ['True', 'False'],
                 Answers = [0, 100],
                 points=1,
                 difficulty = 1,
                 hint = None,
                 randomize_answers = False):

        self.Title = Title
        self.QuestionText = QuestionText
        self.points = points
        self.difficulty = difficulty
        self.type = qtype
        if randomize_answers:
            new_opts, new_ans = zip(*quick_shuffle(zip(Options,Answers)))
            self.Options = new_opts
            self.Answers = new_ans
        else:
            self.Options = Options
            self.Answers = Answers
        self.Hint = hint
        
    def __str__(self):
        s = f"## {self.Title}\n"
        s += f"{self.QuestionText}\n"
        s += "\n"
        for opt,val in zip(self.Options,self.Answers):
            if val > 0:
                s += f" - {opt} **_(CORRECT ANSWER)_** \n"                
            else:
                s += f" - {opt}\n"
        s += '\n'
        return s
   
    def preview(self):
        from IPython.display import Markdown
        return Markdown(str(self))
    
    def export(self):
        q = []
        q.append(f'NewQuestion,{self.type},')
        q.append(f'Title,{self.Title},')
        q.append(f'QuestionText,{encapsulate_commas(self.QuestionText)},HTML,')
        q.append(f'Points,{self.points},')
        q.append(f'Difficulty,{self.difficulty},')
        for opt,val in zip(self.Options, self.Answers):
            q.append(f'Option,{val},{opt},HTML,')
        if not self.Hint is None:
            q.append(f'Hint,{self.Hint}')
        return q
    
    def widget(self):
        import ipywidgets as widgets
        x = widgets.Box(
            [
                widgets.Label(self.QuestionText),
                widgets.RadioButtons(
                    options=self.Options,
                    layout={'width': 'max-content'}
                )
            ]
        )
        return x
    
def quick_shuffle(it):
    from random import randrange
    it2 = list(it).copy()
    for i in range(len(it2)):
        j = randrange(len(it2))
        it2[i], it2[j] = it2[j], it2[i]
    return it2

def encapsulate_commas(string):
    return string.replace(',', '\",\"')
