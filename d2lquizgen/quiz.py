class question():
    
    def __init__(self, Title="Default Question", 
                 QuestionText="What is the meaning of life",
                 qtype = "MC",
                 Options = ['True', 'False'],
                 Answers = [0, 100],
                 points=1,
                 difficulty = 1):

        self.Title = Title
        self.QuestionText = QuestionText
        self.points = points
        self.difficulty = difficulty
        self.type = qtype
        self.Options = Options
        self.Answers = Answers
        
    def __str__(self):
        s = f"# {self.Title}\n"
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
        q.append(f'QuestionText,{self.QuestionText},HTML,')
        q.append(f'Points,{self.points},')
        q.append(f'Difficulty,{self.difficulty},')
        for opt,val in zip(self.Options, self.Answers):
            q.append(f'Option,{val},{opt},HTML,')
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
