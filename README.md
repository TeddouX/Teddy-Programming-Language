
# Teddy Programming Langage



## Disclamer

This programming language is very basic and doesn't have the main features of a real programming language. </br>
Since it's very basic it needs semi_colons at the end of each line


## Features

- Print
- Variable declaration
- Input
- Call functions (only 2)

## How to use it

For python 3.0+
```bash
  python3 interpreter.py (name of your file).ted
```
For other versions
```bash
  python interpreter.py (name of your file).ted
```

## Basic syntax

### To print something in the console

```ted
  PRINT [data]
```
  
`data`: Can be a variable or a string 

### To get user input

```ted
  INPUT [txt] >> [var_to_write]
```
`txt`: The text that will appear in the console
`var_to_write`: The variable that will be written by the users input

### To declare a variable

```ted
  VAR [name] = [value]
```
`name`: The name of the variable
`value`: The value of the variable

### To call a function

```ted
  CALL [function] [args] >> [var_to_write]
```
`function`: The name of the function
`args`: The argument of the function
`var_to_write`: The variable to write (if it has a return)

### To make a comment
```ted
  :/ Your comment here ; <- Mandatory else your code breaks (will remove that later)
```

## Functions
Function Name | Arguments    | Description
---           | ---          | ---
random        | `1`: int     | Generate number between [1] and [2] 
---           | `2`: int     |

Function Name | Arguments    | Description
---           | ---          | ---
random        | `1`: int     | Picks random number between [1] and [2] 
---           | `2`: int     |

## Future add ons
 - That you don't need to put semicolons at the end of each line
 - "f" strings (will be the same as python)
 - function declaration (not sure)
 - if statement (not sure)
