# Sierpinski Triangle

This project is a Python implementation of the Sierpinski Triangle fractal pattern. It demonstrates the recursive and self-similar structure of the Sierpinski Triangle using Python.


## Features

- Generates the Sierpinski Triangle pattern based on recursion.
- Visualizes the Sierpinski Triangle with adjustable depth levels, allowing exploration of fractal complexity.

## Installation

**Prerequisite:** Ensure [Poetry](https://python-poetry.org/docs/#installation) is installed on your system.

1. Clone the repository:
   ```bash
   git clone https://github.com/PetrFridrich/SierpinskiTriangle.git
   ```
2.  Navigate to the project directory:
    ```bash
    cd SierpinskiTriangle
    ```
3. Install the dependencies with Poetry:
    ```bash 
    poetry install
    ```
This will install all required dependencies as defined in pyproject.toml.

## Project Structure

The project is organized as follows:

<pre>
SierpinskiTriangle/
├── src/                     # Folder with source codes
│   ├── __main__.py          # Main script to run the Sierpinski Triangle
│   └── sierpinski.py        # Implementation of the Sierpinski fractal pattern
├── .gitignore               # Git ignore file
├── pyproject.toml           # Poetry project configuration and dependencies
├── poetry.lock              # Poetry lock file to ensure consistent dependencies
├── LICENSE                  # License file for the project
└── README.md                # This README file
</pre>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

