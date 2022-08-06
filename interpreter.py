# TODO:
#   - random [doing]
#   - if 
#   - functions
#   - f strings
#   - finish comments 
#   - type conversion in input

import random as rand
import numpy
from sys import *
import re
from unittest import TextTestResult

variables = {}

keywords = [
    "PRINT",
    "VAR",
    "INPUT",
    "CALL"
]

NONE = "none"
INT = "int"
STR = "str"
BOOL = "bool"
ANY = "any"

functions = {
    "random": {
        "args": [INT, INT],
        "return": INT,
        "description": "Generate random number"
    },
    "randint": {
        "args": [INT, INT],
        "return": INT,
        "description": "Picks random ints from arguments"
    }
}

################
# INTERPRETER
################

class Interpreter:
    def __init__(self, filecontent: list, filename: str) -> None:
        self.filecontent = filecontent
        self.filename = filename

    def __run__(self) -> None:
        data = self.filecontent
        for x in data:
            if self._keyword(x, keywords[keywords.index("PRINT")]):
                txt = x.replace("PRINT", '')
                if '"' in txt: 
                    txt = txt.replace('"', '').strip()
                    print(txt)
                elif txt.strip() in variables:
                    var_name = txt.strip()
                    if variables[var_name]['type'] == STR:
                        print(variables[var_name]['value'].replace('"', '').strip())
                    else: 
                        print(variables[var_name]['value'])
                else: 
                    raise SyntaxError("Invalid syntax: expected a string or a variable to print")   
            
            if self._keyword(x, keywords[keywords.index("VAR")]):
                var = x.replace("VAR", '')
                try:
                    equals_pos = var.index("=")
                except ValueError:
                    raise SyntaxError("Invalid syntax: mising equals symobol (=)")
                var_name = var[:equals_pos]
                var_name = var_name.replace(' ', '')
                var_value = var[equals_pos+1:].strip()
                var_type = NONE

                if bool(re.search(r'\d', var_value)) and not bool(re.search(r'[a-zA-Z]', var_value)):
                    var_type = INT
                elif bool(re.match(var_value, "true")) or bool(re.match(var_value, "true")):
                    var_type = BOOL
                elif bool(re.search(r'[a-zA-Z]', var_value)) and var_value not in ["true", "false"]:
                    var_type = STR
                else: 
                    raise ValueError("The type doesn't exist")

                variables[var_name] = {
                    "value": var_value,
                    "type": var_type
                } 
                # print(variables)
            if self._keyword(x, keywords[keywords.index("INPUT")]):
                dt = x.replace("INPUT", '').strip()
                try:
                    in_symbol_pos = dt.index(">>")
                except ValueError:
                    raise SyntaxError("Invalid syntax: mising in symbol (>>)")
                    
                txt = dt[:in_symbol_pos].strip()
                txt = txt.replace('"', '')  
                var_to_write = dt[in_symbol_pos+2:].strip()
                var_to_write_type = NONE

                if not var_to_write in variables:
                    raise NameError("The variable that you are trying to access doesn't exist")
                else:
                    value_to_write = input(txt)

                    if bool(re.search(r'\d', type)) and not bool(re.search(r'[a-zA-Z]', type)):
                        value_to_write = int(value_to_write)
                        var_to_write_type = INT
                    elif bool(re.match(type, "true")) or bool(re.match(type, "true")):
                        var_to_write_type = BOOL
                    elif bool(re.search(r'[a-zA-Z]', type)) and type not in ["true", "false"]:
                        var_to_write_type = STR
                    
                    if variables[var_to_write]['type'] != var_to_write_type:
                        raise ValueError("The input type and the variable type aren't the same")

                    variables[var_to_write]['value'] = value_to_write
                    # print(variables)
            if self._keyword(x, ":/"):
                pass # do nothing
            if self._keyword(x, "CALL"):
                func = x.replace("CALL", '').strip()
                func_name = func[0:func.index("(")].strip()

                if not func_name in functions:
                    raise NameError("The called function doesn't exist")

                func_args_type = functions[func_name]['args']  
                func_return_type = functions[func_name]['return']       
                func_description = functions[func_name]['description']

                try:
                    in_symbol_pos = func.index(">>")
                except ValueError:
                    raise SyntaxError("Invalid syntax: mising in symbol (>>)")

                var_to_write = func[in_symbol_pos+2:].strip()

                if not var_to_write in variables:
                    raise NameError("The variable that you are trying to write doesn't exist")

                var_to_write_type = variables[var_to_write]['type']

                if var_to_write_type != func_return_type:
                    raise TypeError("The variable to write and the return type aren't the same")

                user_func_args = func[func.index("(")+1:func.index(")")]
                user_func_args = user_func_args.split(',')
                user_func_args_type = []

                for i in range(len(user_func_args)):
                    user_argument = user_func_args[i].strip().replace('"', '')
                    if bool(re.search(r'\d', user_argument)) and not bool(re.search(r'[a-zA-Z]', user_argument)):
                        user_func_args_type.append(INT)
                    if bool(re.match(user_argument, "true")) or bool(re.match(user_argument, "true")):
                        user_func_args_type.append(BOOL)
                    if bool(re.search(r'[a-zA-Z]', user_argument)) and user_argument not in ["true", "false"]:
                        user_func_args_type.append(STR)

                if not numpy.array_equal(func_args_type, user_func_args_type):
                    raise TypeError("The arguments of the function aren't the good type")

                if func_name == "random":
                    func_return = rand.randrange(int(user_func_args[0]), int(user_func_args[1]))
                elif func_name == "randint":
                    func_return = rand.choice([int(user_func_args[0]), int(user_func_args[1])])

                variables[var_to_write]['value'] = func_return
                                   

    def _keyword(self, x, key: str) -> bool:
        if x[0:len(key)] == key:
            return True
        else:
            return False

def open_file(filename):
    dt = open(filename).read()
    dt = dt.replace("\n", '')
    dt = dt.split(";")
    dt = dt[:-1]
    
    # print(dt)

    return dt

def run() -> None:
    filename = argv[1]
    if not filename.endswith(".ted"):
        raise RuntimeError("Can't open file that doesn't finish with .ted")
    else:
        file_contents = open_file(filename)
        interpreter = Interpreter(file_contents, filename)
        interpreter.__run__()
        

if __name__ == "__main__":
    run()