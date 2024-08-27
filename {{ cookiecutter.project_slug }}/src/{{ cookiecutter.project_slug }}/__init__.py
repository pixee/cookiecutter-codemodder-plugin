from codemodder.registry import CodemodCollection

from .custom_codemod import CustomCodemod
from .semgrep_codemod import CustomSemgrepCodemod

# This name is used by the entry point in pyproject.toml to register the codemods
registry = CodemodCollection(
    origin="{{ cookiecutter.project_slug }}",
    codemods=[
        CustomCodemod,
        CustomSemgrepCodemod,
    ],
)
