# Python best practices

The following is a list of best practices for Python that are being followed in this project:

- Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) coding style guide.
- Use a linter/formatter such as [black](https://pypi.python.org/pypi/black) to enforce consistent, PEP8-conforming styles.
- Follow The Zen of Python (found by writing `import this` in the Python REPL)
- Use docstrings for all public functions, classes, and modules.
- Use `if __name__ == "__main__":` to ensure that the code is only executed when the module is run directly.
- Follow the appropriate design patterns to avoid repetitions and tight-coupling.
- Use virtual enviroments (created using `python -m venv`) to isolate dependencies.
- Use [pylint](https://www.pylint.org/) to check for style issues.
- Save the dependencies in a `requirements.txt` file (using the output from `pip freeze`).
- Use lowercase (snake_case) for all identifiers.
- Do NOT use `from module import *` imports.
- Be consistent with the style of the rest of the codebase.
- Avoid using legacy syntax (such as `%`-formatting).
- Order imports as follows (and separate them with a single line):
  - Standard library imports
  - Third-party library imports
  - Local application/library specific imports
- Dockerize the application.
