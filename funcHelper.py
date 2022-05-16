import re
import numpy as np

replace = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

allowed = {
    'x1', 'x2', 'x3', 'x4', 'x5',
    'sin',
    'cos',
    'sqrt',
    'exp',
}


def getFunction(funcString: str):
    for expr in re.findall('[a-zA-Z_]+\D', funcString):
        if(expr not in allowed):
            raise Exception(f'{expr} is not allowed in function')

    funcString = re.sub(r"([\d]+)([a-zA-Z_])", r"\1*\2", funcString)
    for toReplace, newValue in replace.items():
        funcString = funcString.replace(toReplace, newValue)
    print(funcString)
    def func(x1=0, x2=0, x3=0, x4=0, x5=0):
        return eval(funcString)

    return func
