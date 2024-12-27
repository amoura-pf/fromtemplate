# Python Template: A Streamlined Development Environment

This repository provides a comprehensive foundation for setting up a well-structured and efficient Python development environment. It guides you through creating a virtual environment, installing essential tools, and configuring automated code formatting and linting.

# Getting Started

## 1. Clone this Repository:

Begin by cloning this repository using Git:
```bash
git clone https://github.com/your-username/python-template.git
cd python-template
```
Replace https://github.com/your-username/python-template.git with the actual URL of your repository.


## 2. Create a Virtual Environment:

A virtual environment isolates project dependencies, preventing conflicts with system-wide packages. To create one, run the following command:

```bash
python -m venv .venv 
```

## 3. Activate the Virtual Environment:

Activate the virtual environment to use the isolated packages you'll install. The activation command depends on your operating system:

**Windows:**
```bash
.\.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```
Your terminal prompt will now typically indicate that the virtual environment is active (e.g., `(.venv)your_username@your_machine:~/project$`).


## 4. Install Poetry (Package Manager):

Poetry is a powerful dependency management tool that simplifies package installation and version control. Install it within the activated virtual environment using:

```bash
pip install poetry
```

## 5. Initialize a `pyproject.toml` File:

This file serves as Poetry's configuration center. Create a basic `pyproject.toml` file in your project directory using:

```bash
poetry init
```
This command prompts you for basic project information and generates a starting `pyproject.toml` file.



## 6. Install Development Dependencies:

These tools enhance your development experience by automating code formatting, linting (static code analysis), and testing:

```bash
poetry add pylint --dev  # Code linting
poetry add black --dev   # Code formatting
poetry add isort --dev   # Code import sorting
poetry add pytest --dev  # Unit testing
poetry add pre-commit --dev  # Manage pre-commit hooks
poetry add python-semantic-release  # Automated versioning & release management
```
The `--dev` flag indicates these packages are for development purposes only and won't be included in your project's distribution.


## 7. Configure Pylint (Optional):

Pylint helps identify potential errors and coding style issues. To create a basic Pylint configuration file (`.pylintrc`), run:

```bash
poetry run pylint --generate-rcfile > .pylintrc
```
You can customize the `.pylintrc` file to tailor Pylint's behavior to your project's coding standards.



## Additional Notes

Remember to deactivate the virtual environment when you're finished with development:

```bash
deactivate
```

- This template provides a solid foundation. You can customize it further by adding your project-specific dependencies, code style preferences, and testing frameworks.

**Benefits of Using This Template:**

- **Improved Efficiency:** Streamlines the development setup process.
- **Enhanced Code Quality:** Promotes consistent formatting and identifies potential issues.
- **Isolated Environment:** Prevents conflicts with system-wide packages.
- **Flexibility:** Customizable to fit your project's needs.

By following these steps, you'll have a well-structured development environment ready to take on your Python projects!


# Requirements

## 1. **Update `pyproject.toml`:**

**Change `name`:** Modify the `name` field in the `[tool.poetry]` section of `pyproject.toml` to the actual name of your library. For example, if your library is named "my_awesome_library", the line would look like:

```toml
name = "my_awesome_library" 
```

## 2. **Rename the `src` Folder:**

Rename the `src/python-template` folder to the actual name of your library. For example, if your library is named "my_awesome_library", rename the folder to `src/my_awesome_library`.

These steps ensure that your project is properly configured with the correct library name and that Poetry can correctly locate and package your library code.