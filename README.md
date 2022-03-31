
---

- https://stackoverflow.com/questions/9090079/in-python-how-to-import-filename-starts-with-a-number
- https://stackoverflow.com/questions/147507/how-does-one-do-the-equivalent-of-import-from-module-with-pythons-import

dynamic import hacks, importlib

---

> Some objects have neither attributes nor methods, but they could. Not all objects are subclassable. But everything is an object in the sense that it can be assigned to a variable or passed as an argument to a function.

---

> In Python, functions are first-class objects. You can pass a function as an argument to another function. Modules are first-class objects. You can pass an entire module as an argument to a function. Classes are first-class objects, and individual instances of a class are also first-class objects.

> everything in Python is an object. Strings are objects. Lists are objects. Functions are objects. Classes are objects. Class instances are objects. Even modules are objects.

---

> The only delimiter is a colon (:) and the indentation of the code itself.

---

> Python uses carriage returns to separate statements
> C++, Java use explicit semicolon ';'

---

> Some programming languages encourage the use of error return codes, which you check. Python encourages the use of exceptions, which you handle.

---

> Unlike Java, Python functions don’t declare which exceptions they might raise. It’s up to you to determine what possible exceptions you need to catch

> Python uses try...except blocks to handle exceptions, and the raise statement to generate them. Java and c++ use try...catch blocks to handle exceptions, and the throw statement to generate them.

> you don’t need to handle an exception in the function that raises it. If one function doesn’t handle it, the exception is passed to the calling function, then that function’s calling function, and so on “up the stack.” If the exception is never handled, your program will crash, Python will print a “traceback” to standard error, and that’s the end of that. Again, maybe that’s what you want; it depends on what your program does.

---

> What Python will not let you do is reference a variable that has never been assigned a value. Trying to do so will raise a NameError exception.

---

> Unlike c, Python does not support in-line assignment, so there’s no chance of accidentally assigning the value you thought you were comparing

---

> modules are objects, and all modules have a built-in attribute \__name__. A module’s \__name__ depends on how you’re using the module. If you import the module, then \__name__ is the module’s filename, without a directory path or file extension.

> But you can also run the module directly as a standalone program, in which case \__name__ will be a special default value, \__main__.

---

```py
module.__name__
function.__doc__
```

---

> Floating point numbers are accurate to 15 decimal places.
```py
>>> 1.12345678901234567890
1.1234567890123457
```

---

> In Python3, value of an integer is not restricted by the number of bits and can expand to the limit of the available memory

```py
print(100**100)
```

---

> Remember, -1 is a valid list index

---

> None is a special constant in Python. It is a null value. None is not the same as False. None is not 0. None is not an empty string. Comparing None to anything other than None will always return False.

> None is the only null value. It has its own datatype (NoneType).

> In a boolean context, None is false and not None is true

---

