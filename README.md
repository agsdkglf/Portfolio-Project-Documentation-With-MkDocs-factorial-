# Project Documentation With MkDocs
The project contains documentation of the code counting a factorial, which follows the Diátaxis documentation framework. It has a widespread adoption in the Python community and is used by large projects such as Django and NumPy.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [License](#license)


## General Information
The aim of the code in "factorial.py" is to count a factorial of any given number, as long as the number is equal or greater than 0. The value of the factorial of 0 is 1 according to the convention for an empty product in mathematics. The code uses recursion because it is simpler and shorter than using an iterative code. Some users may prefer iteration though, and in that case the result is the same as using recursion.


## Technologies Used
Three Python packages are used in the project:
- MkDocs 1.4.2
- mkdocstrings 0.19.0
- mkdocs-material 8.5.8


## Setup
The project's requirements are listed in a requirements.txt file.

Download the code from this GitHub repository and place the "factorials/" folder in the same directory as your Python script:

    your_project/
    │
    ├── factorials/
    │   ├── __init__.py
    │   └── factorial.py
    │
    └── your_script.py

Inside of "your_script.py" you can now import the `number_factorial(n)` function from the "factorials.factorial" module:

    # your_script.py
    from factorials.factorial import number_factorial


## Usage
After you've imported the function, you can use it to find the factorial of a number that you need:

    # your_script.py
    from factorials.factorial import number_factorial

    result = number_factorial(4)
    print(result)  # OUTPUT: 24

You are now able to count the factorial, and you'll always get an integer as a result.


## Project Status
The project's status is _complete_.


## Acknowledgements
This project was based on "Build Your Python Project Documentation With MkDocs" (https://realpython.com/python-project-documentation-with-mkdocs/).


## Contact
Created by Adam Hoppe (adhoppe@poczta.fm) - feel free to contact me!


## License
This project is open source and available under the MIT License.
