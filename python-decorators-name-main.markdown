# Understanding Python Decorators

A **decorator** in Python is a function that takes another function as input, enhances it with additional functionality, and returns the modified function without altering its original code.

Think of it as wrapping a gift: the core function remains unchanged, but you add a decorative layer to enhance its behavior.

## Basic Concept

Decorators are a powerful way to modify or extend the behavior of functions or methods. They are commonly used for tasks like logging, authentication, or performance measurement.

### How Decorators Work

1. A decorator is a function that accepts another function as an argument.
2. It defines a **wrapper** function that adds extra behavior before and/or after calling the original function.
3. The decorator returns the wrapper function, which replaces the original function when called.

## Simple Decorator Example

Here’s a basic example to illustrate how a decorator works:

```python
# Define the decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Define a normal function
def say_hello():
    print("Hello!")

# Apply the decorator manually
decorated_function = my_decorator(say_hello)

# Call the decorated function
decorated_function()
```

### Output

```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

### Explanation

| Step | Code | Description |
| --- | --- | --- |
| 1 | `my_decorator(func)` | The decorator function takes a function `func` as input. |
| 2 | `wrapper()` | A new function that adds behavior before and after calling `func()`. |
| 3 | `return wrapper` | The decorator returns the wrapper function, which replaces the original function. |
| 4 | `decorated_function = my_decorator(say_hello)` | The `say_hello` function is passed to the decorator, which returns the wrapped version. |
| 5 | `decorated_function()` | Executes the wrapped function, running the extra behavior and the original function. |

## Using the `@` Syntax (Shortcut)

Python provides a concise way to apply decorators using the `@` symbol, which is equivalent to manually wrapping the function.

```python
def my_decorator(func):
    def wrapper():
        print("Before function runs.")
        func()
        print("After function runs.")
    return wrapper

# Apply decorator using @
@my_decorator
def greet():
    print("Hi there!")

greet()
```

### Output

```
Before function runs.
Hi there!
After function runs.
```

The `@my_decorator` syntax is shorthand for `greet = my_decorator(greet)`.

## Real-World Use Case: Logging Decorator

Decorators are often used for practical purposes, such as logging function calls. Here’s an example of a logging decorator:

```python
def log_decorator(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        func()
        print(f"Function {func.__name__} finished.")
    return wrapper

@log_decorator
def process_data():
    print("Processing data...")

process_data()
```

### Output

```
Calling function: process_data
Processing data...
Function process_data finished.
```

## Key Points

- **Decorators enhance functionality** without modifying the original function’s code.
- Use the `@decorator_name` syntax for a clean and readable way to apply decorators.
- Common use cases include:
  - **Logging**: Track function calls and their execution.
  - **Authentication**: Restrict access to functions based on user permissions.
  - **Timing**: Measure how long a function takes to execute.
- Decorators can also accept arguments and be stacked for more complex behavior.
- Decorators are a powerful feature in Python that allow you to wrap functions with additional functionality in a clean, reusable way.
- By using the `@` syntax, you can easily apply decorators to enhance your code without modifying the original function logic.

# What is `__name__`?

In every Python file, there’s a built-in variable called `"__name__"`. This variable gets **set automatically** by Python when the file is run and `"__main__"` is a string name given by Python to the script being **run directly**.

---

### Two Common Cases:

| Case | Description | Value of `__name__` |
| --- | --- | --- |
| When the file is **run directly** | You're running the script with `python script.py` | `'__main__'` |
| When the file is **imported as a module** | The file is imported into another script | The name of the file/module (e.g. `'my_module'`) |
