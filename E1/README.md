# Episode 1
- Type
- Variable
- Operators
- IO -> Input / Output -> File / Network

# Model
- Operation
- Flow control
- Variable / Memory
- Execution
- IO -> Input / Output -> File / Network


# Type
Everythings is an object.

## Difference of literal and variable
- Literal -> 1, "s", True, None
- Variable -> x, y, z, a, b, c

## Primitive
- Number -> Integer / Float / Complex / Fraction
- char -> alphabet / number / symbol ...
- String -> some char together (0 or more)
- Boolean -> True / False
- Null -> None

## Non-primitive
- List -> [1, 2, 3, 4, 5] , list() == [] , list([1, 2, 3]) == [1, 2, 3]
- Dictionary -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} , dict() == {} , dict([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
- Set -> {1, 2, 3, 4, 5} , set() == set() , set([1, 2, 3, 4, 5]) == {1, 2, 3, 4, 5}
- Tuple -> (1, 2, 3, 4, 5) , tuple() == () , tuple([1, 2, 3, 4, 5]) == (1, 2, 3, 4, 5) -> immutable


### Number
- Integer -> 1, 2, 3, 4, 5
- Float -> 1.0, 2.0, 3.0, 4.0, 5.0
- Complex -> 1j, 2j, 3j, 4j, 5j, 1+1j, 2+2j, 3+3j, 4+4j, 5+5j
- Fraction -> Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5), Fraction(5, 6)

### Char
char is inside of single quote. -> 'a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '.', '<', '>', '/', '?', '`', '~'

### String
string is inside of double quote. -> "aa", "", "bsaasdfa", "123123", "asdfasdfasd", "asdfa313", "asdfa!@#", "asdfa$%^", "asdfa&*(", "asdfa)=-", "asdfa_+", "asdfa[]", "asdfa{}", "asdfa|\\", "asdfa;:", "asdfa'", "asdfa\"", "asdfa,.", "asdfa<>", "asdfa/?", "asdfa`~"

### Boolean
can be True or False.

### Null
can be None.

## Type conversion
- int() -> convert to integer, if can't convert, will raise ValueError, input -> string, float, complex, fraction, boolean, null
- float() -> convert to float, if can't convert, will raise ValueError, input -> string, integer, complex, fraction, boolean, null
- complex() -> convert to complex, if can't convert, will raise ValueError, input -> string, integer, float, fraction, boolean, null
- str -> convert to string, input -> integer, float, complex, fraction, boolean, null
- bool -> convert to boolean, input -> integer, float, complex, fraction, string, null
- list -> convert to list, input -> integer, float, complex, fraction, string, boolean, null
- dict -> convert to dictionary, input -> integer, float, complex, fraction, string, boolean, null
- set -> convert to set, input -> integer, float, complex, fraction, string, boolean, null

### int()
- int() -> 0
- int(1) -> 1
- int(1.0) -> 1
- int(1.1) -> 1
- int(1.9) -> 1
- int(1/2) -> 0
- int(True) -> 1
- int(False) -> 0
- int(None) -> 0
- int("1") -> 1
- int("222") -> 222

### float()
- float() -> 0.0
- float(1) -> 1.0
- float(1.0) -> 1.0
- float(1.1) -> 1.1
- float(1.9) -> 1.9
- float(1/2) -> 0.5
- float(True) -> 1.0
- float(False) -> 0.0
- float(None) -> 0.0
- float("1") -> 1.0
- float("222") -> 222.0
- float("222.0") -> 222.0
- float("222.1") -> 222.1

### str()
- str() -> ""
- str(1) -> "1"
- str(1.0) -> "1.0"
- str(1.1) -> "1.1"
- str(1.9) -> "1.9"
- str(1/2) -> "0.5"
- str(True) -> "True"
- str(False) -> "False"
- str(None) -> "None"
- str("1") -> "1"

### bool()
- bool() -> False
- bool(1) -> True
- bool(1.0) -> True
- bool(1.1) -> True
- bool(0) -> False
- bool("1") -> True
- bool("") -> False
- bool("0") -> True
- bool("False") -> True
- bool("True") -> True
- bool(None) -> False

# Variable
variables are defined by two thing -> name and address of memory (value).

        --------
a   ->  | 1    | -> 0x0000000000000001
        --------

## Variable name (identifier) rules in python
- can be alphabet, number(non-negetive integer), underscore (_)
- can't be keyword -> python keyword list -> https://docs.python.org/3/reference/lexical_analysis.html#keywords -> these are reserved words.
- can't be start with number -> 1a, 2b, 3c, 4d, 5e, 121, 0asavasdvas

### Correct examples
- a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
- man, count, ...
- a1, b2, c3, d4, e5, f6, g7, h8, i9, j0, k11, l22, m33, n44, o55, p66, q77, r88, s99, t00, u111, v222, w333, x444, y555, z666
- V2, v2paafsn2

### Incorrect examples
- 1a, 2b, 3c, 4d, 5e, 6f, 7g, 8h, 9i, 0j, 11k, 22l, 33m, 44n, 55o, 66p, 77q, 88r, 99s, 00t, 111u, 222v, 333w, 444x, 555y, 666z
- False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

## Variable name (identifier) convention in python
In python, there are two convention of variable name (identifier) -> snake_case and camelCase, but snake_case is more popular.

### snake_case
snake_case -> all lower case, and use underscore (_) to separate words.
#### examples
snake_case, snake_case_is_good, snake_case_is_good_for_python, snake_case_is_good_for_python_programming, snake_case_is_good_for_python_programming_language, snake_case_is_good_for_python_programming_language_so_you_should_use_it

### camelCase
camelCase -> first word is lower case, and use upper case for first letter of each word.
#### examples
camelCase, camelCaseIsGood, camelCaseIsGoodForPython, camelCaseIsGoodForPythonProgramming, camelCaseIsGoodForPythonProgrammingLanguage, camelCaseIsGoodForPythonProgrammingLanguageSoYouShouldUseIt


## Variable definition and assignment
variable_name = value

### Examples
- a = 1
- b = 2
- count = 2 + 3
- visited = True
- animal_names = ["dog", "cat", "bird", "fish"]
- animal_name = "dog"
- cc = b + 1
- cc2 = b * a

## Variable usage
we can use variable name to get value of variable after definition and it's not possible to use variable name before definition.

# Operators
## Operators types
- unary -> +, -
- binary -> +, -, *, /, //, %, **

## Operators precedence
for operators with same precedence, it's evaluated from left to right.
1 - ()
2 - **
3 - *, /, //, %
4 - +, -
5 - not
6 - and, or
7 - <, <=, >, >=, ==, !=

### Examples
- 2 + 3 * 4 -> 14
- 2 ** 3 ** 2 -> 512
- 2 ** 3 * 2 -> 16
- 2 ** (3 * 2) -> 64
- 2 * 3 ** 2 -> 18

## Operands types
- lhs -> left hand side
- rhs -> right hand side

### Examples
- 2 + 3 -> 2 is lhs, 3 is rhs
- 3 - 2 -> 3 is lhs, 2 is rhs
- 1 * 2 -> 1 is lhs, 2 is rhs
- 0 / 1 -> 0 is lhs, 1 is rhs
- -2 -> 2 is rhs

## Arithmetic operators
- + -> addition
- - -> subtraction
- * -> multiplication
- / -> division -> 2 / 3 -> 0.6666666666666666
- // -> floor division -> 2 // 3 -> 0 , -2 // 3 -> -1
- % -> modulo -> 2 % 3 -> 2 , -2 % 3 -> 1
- ** -> exponentiation -> 2 ** 3 -> 8 , 2 ** 0.5 -> 1.4142135623730951
- + -> unary plus -> +2 -> 2, +b(-1) -> b(-1), +b(1) -> b(1)
- - -> unary minus -> -2 -> -2, -b(-1) -> 1, -b(1) -> -1

## Logical operators
- and -> -----------------
         |A | B | A and B |
         -----------------
         |T | T |    T    |
         |T | F |    F    |
         |F | T |    F    |
         |F | F |    F    |
         -----------------
- or -> -----------------
        |A | B | A or B |
        -----------------
        |T | T |    T    |
        |T | F |    T    |
        |F | T |    T    |
        |F | F |    F    |
        -----------------
- not -> -----------------
         |A | not A |
         -----------------
         |T |   F   |
         |F |   T   |
         -----------------

## Comparison operators
copmarison operators are used to compare two values and return boolean value every time.
- == -> equal -> 2 == 3 -> False, 2 == 2 -> True
- != -> not equal -> 2 != 3 -> True, 2 != 2 -> False
- > -> greater than -> 2 > 3 -> False, 2 > 2 -> False, 2 > 1 -> True
- < -> less than -> 2 < 3 -> True, 2 < 2 -> False, 2 < 1 -> False
- >= -> greater than or equal to -> 2 >= 3 -> False, 2 >= 2 -> True, 2 >= 1 -> True
- <= -> less than or equal to -> 2 <= 3 -> True, 2 <= 2 -> True, 2 <= 1 -> False

## Assignment operators
- = -> assignment -> a = 1
- += -> addition assignment -> a += 1 -> a = a + 1
- -= -> subtraction assignment -> a -= 1 -> a = a - 1
- *= -> multiplication assignment -> a *= 2 -> a = a * 2
- /= -> division assignment -> a /= 2 -> a = a / 2
- //= -> floor division assignment -> a //= 2 -> a = a // 2
- %= -> modulo assignment -> a %= 2 -> a = a % 2
- **= -> exponentiation assignment -> a **= 2 -> a = a ** 2


# IO
IO is abbreviation of input and output, and it's used to get input from user and show output to user.

## STDIN
STDIN is abbreviation of standard input, and it's used to get input from user and mostly used input from terminal.

## STDOUT
STDOUT is abbreviation of standard output, and it's used to show output to user and mostly used output to terminal.

## Input
We can get input from user, file, or other source.
for getting input from user, we can use input() function.

### input() function
input() function is used to get input from user, and it returns string value.
input() function has one optional parameter, and it's used to show message to user before getting input.
Note: input() using STDIN to get input from user by default.

#### Examples
- input() -> get input from user
- input("Enter your name: ") -> get input from user and show message "Enter your name: " to user before getting input

## Output
We can show output to user, file, or other destination.

### print() function
print() function is used to show output to user, and it's using STDOUT to show output to user by default.
print() function has one or more parameters, and it's used to show output to user.
print() returns None value.

#### Key Parameters
- sep -> separator -> it's used to separate values, and it's default value is " " (space) -> it's string value
- end -> end -> it's used to end output, and it's default value is "\n" -> it's string value

Note: sep and end parameters are optional, end mostly used to end output with specific character or not goin to new line.

#### Output usage
You can send different values to print() function, and print will concat them together with sep parameter and at the end it will add end parameter.

#### Examples
- print("Hello World") -> show output "Hello World" to user
- print("Hello", "World") -> show output "Hello World" to user
- print("Hello", "World", sep="") -> show output "HelloWorld" to user
- print("Hello", "World", "!", sep="***") -> show output "Hello***World***!" to user
- print("Hello", "World", end="!") -> show output "Hello World!" to user
- print("Hello", "World", sep="***", end="!") -> show output "Hello***World!" to user