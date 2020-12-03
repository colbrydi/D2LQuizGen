import sympy as sym
import numpy as np
import re
    


class latex():
    usefiles = False
    useMarkdown = False
    
    def __init__(self, inputval, preamble='',post=''):
        self.formula = ''
        if isinstance(inputval,str):
            self.formula = inputval
        if isinstance(inputval,list):
            inputval = np.array(inputval)
        if isinstance(inputval,np.matrix):
            inputval = np.array(inputval)
        if isinstance(inputval, np.ndarray):
            self.formula = sym.latex(sym.Matrix(inputval))
        self.formula = preamble+self.formula+post
    
    def __str__(self):
        if latex.usefiles:
            return self.renderLatex()
        else:
            return f'${self.formula}$'

    def renderLatex(self, file='', fontsize=12, dpi=300, display=False):
        """Renders LaTeX formula and prints to file.
            Do not add $ or \[\]. 
            The display option is False for inline $ $ and True for displaystyle latex.
        """
        
        #Make unique filname from formula string
        if file == '':
            file = re.sub('[\W_]', '', self.formula)
            if file == '':
                print(f'filename for {self.formula} is empty')
            file = f'./images/{file}.png'
        
        print(f'File = {file}')
        import matplotlib
        import matplotlib.pyplot as plt

        matplotlib.rcParams['text.usetex'] = True
        matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

        fig = plt.figure(figsize=(.01, .01))
        if not display:
            s = f"${self.formula}$"
        else:
            s = f"\\[{self.formula}\\]"
        fig.text(0, 0, s, fontsize=fontsize)
        fig.savefig(file,dpi=dpi,bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)

        if latex.useMarkdown:
            return f'![{str(self.formula)}]({file})'
        else:
            return f'<img src=\"{file}\" alt=\"$${str(self.formula)}$$\">'
    
def sol2str(it):
    '''Turns a list [1,2,3] into latex string for x1=1 x2=2 x3=3'''
    ret = ''
    for i,j in enumerate(it):
        ret+= f"x_{i}={float(j[0]):.2f} \\quad "
    return latex(ret)

def sol2alt(it):
    '''Turns a list [1,2,3] into a readable string for the alt option incase the image doesn't load.'''
    ret = ''
    for i,j in enumerate(it):
        ret+= f"x{i}={float(j[0]):.2f}"
    return latex(ret)

def mat2system(M,b):
    '''Turns a system of equations into latex array'''
    import numpy as np
    M = np.matrix(M)
    m,n = M.shape
    sys = '\\begin{array}{rl}'
    for i in range(m):
        s = '' 
        for j in range(n):
            if M[i,j] > 0:
                if s == '':
                    s += f'{M[i,j]}x_{j}'
                else:
                    s += f'+{M[i,j]}x_{j}'
            elif M[i,j] < 0:
                if s == '':
                    s += f'{M[i,j]}x_{j}'
                else:
                    s += f'-{-M[i,j]}x_{j}'
        s+=f'&={b[i,0]:.2f} \\\\'
        sys+=s
    sys += ' \\end{array}'
    return latex(sys)