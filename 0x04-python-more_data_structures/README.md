# 0x04-python-more_data_structures

This repository contains Python programs that demonstrate various concepts related to more data structures.

## 0. Squared simple

Write a function that computes the square value of all integers in a matrix.

- Prototype: `def square_matrix_simple(matrix=[])`
- `matrix` is a 2-dimensional array
- Returns a new matrix with each value squared
- The initial matrix should not be modified
- No module imports are allowed

## 1. Search and replace

Write a function that replaces all occurrences of an element in a list with another element in a new list.

- Prototype: `def search_replace(my_list, search, replace)`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element
- No module imports are allowed

## 2. Unique addition

Write a function that adds all unique integers in a list, only once for each integer.

- Prototype: `def uniq_add(my_list=[])`
- No module imports are allowed

## 3. Present in both

Write a function that returns a set of common elements in two sets.

- Prototype: `def common_elements(set_1, set_2)`
- No module imports are allowed

## 4. Only differents

Write a function that returns a set of all elements present in only one set.

- Prototype: `def only_diff_elements(set_1, set_2)`
- No module imports are allowed

## 5. Number of keys

Write a function that returns the number of keys in a dictionary.

- Prototype: `def number_keys(a_dictionary)`
- No module imports are allowed

## 6. Print sorted dictionary

Write a function that prints a dictionary by ordered keys.

- Prototype: `def print_sorted_dictionary(a_dictionary)`
- Keys are sorted alphabetically
- Only sort keys of the first level, not inner dictionaries
- No module imports are allowed

## 7. Update dictionary

Write a function that replaces or adds key/value pairs in a dictionary.

- Prototype: `def update_dictionary(a_dictionary, key, value)`
- `key` argument will always be a string
- `value` argument can be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist, it will be created
- No module imports are allowed

## 8. Simple delete by key

Write a function that deletes a key in a dictionary.

- Prototype: `def simple_delete(a_dictionary, key="")`
- `key` argument will always be a string
- If a key doesn’t exist, the dictionary won't change
- No module imports are allowed

## 9. Multiply by 2

Write a function that returns a new dictionary with all values multiplied by 2.

- Prototype: `def multiply_by_2(a_dictionary)`
- All values are integers
- Returns a new dictionary
- No module imports are allowed

## 10. Best score

Write a function that returns a key with the biggest integer value.

- Prototype: `def best_score(a_dictionary)`
- All values are integers
- If no score is found, return None
- No module imports are allowed

## 11. Multiply by using map

Write a function that returns a list with all values multiplied by a number without using loops.

- Prototype: `def multiply_list_map(my_list=[], number=0)`
- Returns a new list with values multiplied by `number`
- Initial list should not be modified
- No module imports are allowed
- You must use `map`
- The code should be maximum 3 lines

## 12. Roman to Integer

Create a function `def roman_to_int(roman_string)` that converts a Roman numeral to an integer.

- The number will be between 1 to 3999
- The function must return an integer
- If `roman_string` is not a string or None, return 0
- No module imports are allowed

