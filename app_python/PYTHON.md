# Python best practices

The following is a list of best practices for Python that are being followed in this project:

## Coding

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

## Testing

- Use [pytest](https://docs.pytest.org/en/latest/) to test the application.
- Create a `tests` directory and a `test_` file for each test, mimicking the directory structure of the application.
- Follow the [Given-When-Then](https://martinfowler.com/bliki/GivenWhenThen.html) style of writing tests.
- Separate between unit and functional tests.
- Use fixtures to provide common setup and teardown code.
- Try to maximize test code coverage to ensure that the application is tested thoroughly.
- Do not modify the application code in tests.
- Do not modify fixtures in other fixtures.
- Prefer `tmpdir` over global test artifacts
- Use yield fixtures.
- Parametrize when asserting the same behavior with various inputs and expected outputs (do not depend on global state).
- Never manually create `Response` objects for tests.
- Try to use Test-Driven Development (TDD).

### References

- https://flask.palletsprojects.com/en/2.0.x/testing/
- https://testdriven.io/blog/flask-pytest/
- https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/
