# DUMPREPL

A Python REPL that will allow you to develop your programs *much faster*.

## Main features

It will allow you to restore any plain expression and, most importantly, push the stuff from your REPL to your stable code, providing for quick iterations.

## Usage notes

After every expression entered, a `\{number}` will appear in the console below the output. This is the number you will be able to use later.

To use the saved object, type `\{number}` with its number in the place where you want it to appear.

Any user input is considered ended only when the last line of that input has no characters in it (except the newline).

## Example usage

```python
>>> a = 123
... 
>>> a
... 
123
\0
>>> \0
... 
123
\1
>>> \1
... 
123
\2
>>> def a():
...   print("I love Python!")
... 
>>> a            
... 
<function a at 0x74716a61ccc0>
\3
>>> \3()
... 
I love Python!
\4
>>> 
```
