# Notes and ressources

## Second workshop step by step
### Datatypes
  - Strings => "This is a string".
  - Lists => ["This", "is", "a", "list"].
  - Numbers (integers and floats) => 123 (int) or 123.45 (float).
  - Dictionaries => {"first_name": "Ajo", "last_name": "Borgvold"}.

### Conversion of data types
  - String to integer => int("123") gives you the integer 123.
  - Integer to string => str(123) gives you the string "123".
  - Important: The int() function only works if the value can be converted to an integer! E.g. int("abc") will cause an error.

### Accessing specific items in lists and dictionaries
  - Lists: the index (an integer) in square brackets (e.g. list[0]).
  - Dictionaries: the key in square brackets (e.g. dict["key"]) => gives you the corresponding value.

### Iterating through lists and dictionaries
  - Lists: `for item in list` => Gives you each item.
  - Dictionaries:
    a. `for key in dictionary` => Gives you each key.
    b. `for key in dictionary.keys()` => Gives you each key.
    c. `for value in dictionary.values()` => Gives you each value.
    d. `for key, value in dictionary.items()` => Gives you both key and value.

### Python operators
  - Comparison/relational operators: equal to, not equal to, greater/smaller than etc. => compares numbers and returns True/False.
  - Logical operators: `and`, `or`, `not` => combines conditional statements, i.e. "if this is true `and` that is true then do the following".

### While loops
  - Repeat some code while (= as long as) some condition applies (i.e. is either `True` or `False`).
  - The `continue` keyword: Skip the rest of the code in the current iteration and start over from the top.
  - The `break` keyword: Break out of the loop entirely.


## Resources
[How to set up a virtual environment in Python](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)