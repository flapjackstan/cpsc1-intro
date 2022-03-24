# Gabbys Intro to CPSC Vocab and Notes 

## Primative Data Types

**integers**/`int`: 0, -1, 5, 800, -100000

**floating point values**/`float`: 0.006, 1.98, -890.0000000006

**booleans**/`bool`: `True`, `False` or 0, 1

**strings**/`str`: 'hello', 'I know kung-fu', '139887', '.019'

note: look for the single or double quotes to indicate non-numeric data types

## Collections

**list**/`list`: [0, 2, 4], [1, 'hello', `True`]
- Anything goes
- Mixed data types
- Elements are mutable (can be reassigned and extended)

**tuple**/`tuple`: (2, 9, 0), ('he', 5), ('is', ), (1, )
- Are imutable (cannot be reassigned and extended)
- Require at least 2 elements

**set**/`set`:
- No duplicates
- Mixed data type
- are mutable (can be reassigned and extended)

**dictionary**/`dict`: {'key':'value'}, {21:'hello', 'world': 3.1}, {'pwd':'my password'}
- No duplicate keys
- Mixed data types
- Keys and values are mutable (can be reassigned and extended)  


## Input/Output (I/O)

`print()` - handy and easy output method

`input()` - handy and easy input method

Another useful I/O method are through files objects.

**File Input**
```
with open('example_data/example_input_file.txt', 'r') as example_file_obj:
    lines = example_file_obj.read()

example_file_obj.close()
```

**File Output**
```
with open('example_data/example_output_file.txt', 'w') as example_file_obj:
    example_file_obj.write("Hello World")

example_file_obj.close()
```


## Vidoes

https://www.youtube.com/watch?v=dtRtvY7mqN8