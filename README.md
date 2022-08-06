
# Teddy Programming Langage



## Disclamer

This programming language is very basic and doesn't have the main features of a real programming language


## Features

- Print
- Variable declaration
- Input
- Call functions (only 2)



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

## Functions
Function Name | Arguments    | Description
---           | ---          | ---
random        | `1`: int     | Generate number between [1] and [2] 
---           | `2`: int     |

Function Name | Arguments    | Description
---           | ---          | ---
random        | `1`: int     | Picks random number between [1] and [2] 
---           | `2`: int     |
