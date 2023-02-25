## What Is The Aim Of The Code?

The aim of the code in factorial.py is as its name suggests to count a factorial of any given number, as long as the number is equal or greater than 0. The value of the factorial of 0 is 1 according to the convention for an empty product in mathematics.

## Why The Recursion Is Used?

The code uses recursion because it is simpler and shorter than using an iterative code. Some users may prefer iteration though, and in that case the result is the same as using recursion.

## How Does The User Work With The Code?

The user works with the code as follows:

- An input is taken from the user.
- The number_factorial(n) function is called, where n is the user's input.
- Inside the function n is checked whether its value is less or greater than zero. If n is less than zero ValueError is raised.
- If n equals 0 or 1, the function returns 1.
- In any other cases a recursive call to the function is done, the estimated value is returned and printed for the user.
