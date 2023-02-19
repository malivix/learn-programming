# Episode 2
- Logical Operators composition
- Logical Operators precedence and output
- Block in python
- Flow control
- String manipulation

# Logical Operators composition
you can compose different together.
For example:

```python
True and True or False
```

# Logical Operators precedence and output
The base precedence of logical operators is:
1 - not
2 - and
3 - or
and for same precedence is left to right.

In and operator the first false will be the output and the rest will be ignored.
In or operator the first true will be the output and the rest will be ignored.

Note: in logical operators the operands can be any type of data but for evaluation will be converted to boolean on the behind.

for example:
- True and False ->  False
- False and b -> False
- 1 and 2 -> 2
- "" or 2 -> 2
- "Mahdi" or 2 -> "Mahdi"
- 1.2 or 2 -> 1.2
- "Mahdi" or 2 and "SH" -> "Mahdi"

# Block in python
In python each block is defined by indentation.
Each block should be indented with the same number of spaces or tabs.
Global block is defined by the first line of the file.

# Flow control
- if / elif / else
- for
- while
- break
- continue

## if / elif / else
if we want to decide between some different operations based on some conditions we can use if/elif/else.

Precedence of if/elif/else is from top to bottom and if one condition is true the rest will be ignored.
Else is optional and can be used only once when all conditions are false.

### example if
```python
if condition1:
    # do something
```

### example if/else
```python
if condition1:
    # do something
else:
    # do something
```

### example if/elif

``` python
if condition1:
    # do something
elif condition2:
    # do something
```

```python
if condition1:
    # do something
elif condition2:
    # do something
elif condition3:
    # do something
```

### example if/elif/else
```python
if True or False and condition1:
    # do something
elif condition2:
    # do something
elif condition3:
    # do something
else:
    # do something
```

## for
for is used to iterate over a sequence (list, tuple, string) or other iterable objects.

### Iterable objects
Iterable objects are objects that can return their members one at a time.
Some examples of iterable objects are list, tuple, string, dictionary and set.

### range function
range function is used to generate a sequence of numbers. in something like a list but in reality is generator and we will talk about it in future.

```python
range(10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
```python
range(1, 10) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
```python
range(1, 10, 2) -> [1, 3, 5, 7, 9]
```

### example for with in
```python
for i in range(10):
    print(i)
```
is equal to
```python
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i)
```

```python
for i in (1, 2, 3, 4, 5):
    print(i)
```

```python
for i in "Mahdi":
    print(i)
```

```python
for i in {"Mahdi", "SH"}: # set is unordered
    print(i)
```

```python
for i in {"name": "Mahdi", "family": "SH"}: # dictionary is unordered and only keys will be printed
    print(i)
```

## while
while is used to iterate over a block of code as long as a condition is true.
when interpreter reach to while it will check the condition and if it is true it will execute the block and then check the condition again and so on.

### example while
```python
i = 0
while i < 10:
    print(i)
    i += 1
print("end")
```

## break
break is used to break the loop and continue to the next line after the loop.

### example break
```python
i = 0
while i < 10:
    print(i)
    i += 1
    if i == 5:
        break
print("end")
```

## continue
continue is used to skip the rest of the block and continue to the next iteration.

### example continue
In this example we want to print numbers from 1 to 10 but skip 5.
```python
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
print("end")
```

# String manipulation
Strings are immutable in python.
it's mean we can't change a character in a string.
```python
x = "Mahdi"
x[0] = "m" # error
x = "m" + x[1:] # correct
```

We can use + operator to concatenate strings.
```python
"Mahdi" + " " + "SH" # "Mahdi SH"
```

We can use * operator to repeat a string.
```python
"Mahdi" * 3 # "MahdiMahdiMahdi"
```

We can use [] operator to access to a character in a string, index starts from 0.
Mahdi -> 0, 1, 2, 3, 4
```python
"Mahdi"[0] # "M"
"Mahdi"[1] # "a"
"Mahdi"[2] # "h"
"Mahdi"[3] # "d"
"Mahdi"[4] # "i"
```

We can use [s:e] operator to access to a substring in a string from s to e, e is excluded.
```python
"Mahdi"[0:2] # "Ma"
"Mahdi"[1:3] # "ah"
"Mahdi"[2:4] # "hd"
"Mahdi"[3:5] # "di"
```

We can use [s:e:step] operator to access to a substring in a string with a step from s to e. e is excluded.
```python
"Mahdi"[0:5:2] # "Mhi"
"Mahdi"[0:5:3] # "Md"
```


We can use [:e] operator to access to a substring from start to e.
```python
"Mahdi"[:2] # "Ma"
"Mahdi"[:3] # "Mah"
"Mahdi"[:4] # "Mahd"
"Mahdi"[:5] # "Mahdi"
```

We can use [s:] operator to access to a substring from s to end.
```python
"Mahdi"[0:] # "Mahdi"
"Mahdi"[1:] # "ahdi"
"Mahdi"[2:] # "hdi"
"Mahdi"[3:] # "di"
"Mahdi"[4:] # "i"
```

We can use [:] operator to access to a substring from start to end.
```python
"Mahdi"[:] # "Mahdi"
```

We can use len() function to get the length of a string.
```python
len("Mahdi") # 5
len("Mahdi SH") # 9
len(["Mahdi", "SH"]) # 2
```

We can use in operator to check if a character is in a string.
```python
"M" in "Mahdi" # True
"m" in "Mahdi" # False
"a" in "Mahdi" # True
"i" in "Mahdi" # True
"S" in "Mahdi" # False
```

We can use not in operator to check if a character is not in a string.
```python
"M" not in "Mahdi" # False
"m" not in "Mahdi" # True
"a" not in "Mahdi" # False
"i" not in "Mahdi" # False
"S" not in "Mahdi" # True
```

We can use str() function to convert any type of data to string.
```python
str(1) # "1"
str(1.1) # "1.1"
str(True) # "True"
str(False) # "False"
str([1, 2, 3]) # "[1, 2, 3]"
str((1, 2, 3)) # "(1, 2, 3)"
str({"name": "Mahdi", "family": "SH"}) # "{'name': 'Mahdi', 'family': 'SH'}"
str({"Mahdi", "SH"}) # "{'SH', 'Mahdi'}"
```

We can use negative index to access to a character from end of string.
```python
"Mahdi"[-1] # "i"
"Mahdi"[-2] # "d"
"Mahdi"[-3] # "h"
"Mahdi"[-4] # "a"
"Mahdi"[-5] # "M"
```

We can use negative index to access to a substring from end of string.
```python
"Mahdi"[-5:-1] # "Mahd"
"Mahdi"[-4:-1] # "ahd"
"Mahdi"[-3:-1] # "hd"
"Mahdi"[-2:-1] # "d"
"Mahdi"[-1:-1] # ""
```

We can use negative index to access to a substring from end of string with a step.
```python
"Mahdi"[-5:-1:2] # "Mhd"
"Mahdi"[-4:-1:2] # "ad"
"Mahdi"[-3:-1:2] # "h"
"Mahdi"[-2:-1:2] # ""
"Mahdi"[-1:-1:2] # ""
```