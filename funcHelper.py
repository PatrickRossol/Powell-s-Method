import re

replace = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

allowed = {
    'x',
    'y',
    'sin',
    'cos',
    'sqrt',
    'exp',
}

def getFunction(funcString : str):
    for expr in re.findall('[a-zA-Z_]+', funcString):
        if(expr not in allowed):
            raise Exception(f'{expr} is not allowed in function')

    funcString = re.sub(r"([\d]+)([a-zA-Z_])",r"\1*\2",funcString)
    print(funcString)
    for toReplace, newValue in replace.items():
        funcString = funcString.replace(toReplace, newValue)

    def func(x,y):
        return eval(funcString)

    return func