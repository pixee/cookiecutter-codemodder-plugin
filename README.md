# 🔌 cookiecutter-codemodder-plugin

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for generating custom [Python Codemodder](https://github.com/pixee/codemodder-python) plugins

## Setup

Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and then generate a new plugin project:
```
$ pip install cookiecutter
$ cookiecutter https://github.com/pytest-dev/cookiecutter-codemodder-plugin
```

You will be prompted for various pieces of metadata about your project.

## Usage

The template generates a fully-installable Codemodder plugin. Once the project is generated, you can install it using `pip`:
```
$ cd <new-project-name>
$ pip install -e .
```

Using an editable install (`-e`) is recommended for development purposes.

To test whether it worked, you can run `codemodder`:
```
$ codemodder --list`
```

This should produce output that includes a custom codemod that is prefixed with your project name:
```
<new-project-name>:python/custom-codemod
pixee:python/add-requests-timeouts
pixee:python/bad-lock-with-statement
pixee:python/combine-startswith-endswith
pixee:python/django-debug-flag-on
pixee:python/django-json-response-type
pixee:python/django-receiver-on-top
pixee:python/django-session-cookie-secure-off
pixee:python/enable-jinja2-autoescape
```

**NOTE** The results are alphabetized by codemod ID so depending on your package name your codemod may not be at the top of the list.

The `<new-project-name>:python/custom-codemod` represents a no-op codemod that is included as part of the template. The source code for this codemod can be found under `src/<new-project-name>/custom_codemod.py` in your project directory.

You can begin by renaming and editing this file, or deleting and creating a new one.

Good luck and secure coding!
