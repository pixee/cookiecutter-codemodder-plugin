from codemodder.registry import CodemodCollection

from .custom_codemod import CustomCodemod

# This name is used by the entry point in pyproject.toml to register the codemods
registry = CodemodCollection(
    origin="custom", # TODO: Change this to your own project name
    docs_module="custom_codemods.docs",
    semgrep_config_module="custom_codemods.semgrep",
    codemods=[
        CustomCodemod,
    ],
)
