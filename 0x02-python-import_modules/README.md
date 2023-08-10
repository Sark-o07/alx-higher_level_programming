# 0x02-python-import_modules

This repository contains Python scripts that demonstrate various tasks related to importing modules and using functions from external files.

## Task 0: Import a simple function from a simple file

### Description
The script imports a function `add` from the file `add_0.py` and prints the result of the addition of two variables `a` and `b`.

### Instructions
1. Assign the value 1 to a variable called `a`.
2. Assign the value 2 to a variable called `b`.
3. Use the `add` function to calculate the sum of `a` and `b`.
4. Use the `print` function with string formatting to display the values of `a`, `b`, and the result of the addition.
5. The output should be in the format: `<a value> + <b value> = <add(a, b) value>`

## Task 1: My first toolbox!

### Description
The script imports functions from the file `calculator_1.py`, performs mathematical operations using the variables `a` and `b`, and prints the results.

### Instructions
1. Define the value 10 to a variable called `a`.
2. Define the value 5 to a variable called `b`.
3. Use the imported functions to perform mathematical operations involving `a` and `b`.
4. Use the `print` function to display the results of the operations.
5. Limit the use of the `print` function with string formatting to 4 times.
6. The output should include the results of each operation.

## Task 2: How to make a script dynamic!

### Description
The script prints the number of arguments passed to the script and lists the values of the arguments.

### Instructions
1. Print the number of arguments passed to the script.
2. If at least one argument is passed, print each argument along with its position (starting at 1).
3. Use the `argv` variable to access the arguments passed to the script.
4. The output should be in the format: `<Number of arguments>: <argument 1>, <argument 2>, ...`

## Task 3: Infinite addition

### Description
The script prints the result of the addition of all the arguments passed to the script.

### Instructions
1. Cast each argument to an integer using the `int()` function.
2. Calculate the sum of all the integer arguments.
3. Print the result of the addition.

## Task 4: Who are you?

### Description
The script prints the names defined by the compiled module `hidden_4.pyc`.

### Instructions
1. Download the `hidden_4.pyc` module locally.
2. Print each name defined by the module, one name per line.
3. Print only names that do not start with double underscores (`__`).

Note: Make sure you run the code in Python 3.8.x, as `hidden_4.pyc` has been compiled with this version.
