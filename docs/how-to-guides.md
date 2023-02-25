## How Can The Guides Help You?

You have a number and you need to find its factorial.
These guides show you how the `factorials` package will do it for you.

## The First Steps

Download the code from this GitHub repository and place
the `factorials/` folder in the same directory as your
Python script:

    your_project/
    │
    ├── factorials/
    │   ├── __init__.py
    │   └── factorial.py
    │
    └── your_script.py

## Necessary Import

Inside of `your_script.py` you can now import the
`number_factorial(n)` function from the `factorials.factorial`
module:

    # your_script.py
    from factorials.factorial import number_factorial

## What To Do Next?

After you've imported the function, you can use it
to find the factorial of a number that you need:

    # your_script.py
    from factorials.factorial import number_factorial

    result = number_factorial(4)
    print(result)  # OUTPUT: 24

You are now able to count the factorial, and you'll
always get an `integer` as a result.
