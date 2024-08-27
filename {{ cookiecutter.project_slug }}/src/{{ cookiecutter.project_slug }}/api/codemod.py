from abc import ABCMeta

from codemodder.codemods.api import (
    FindAndFixCodemod,
    RemediationCodemod,
    SimpleCodemod as _SimpleCodemod,
)


class CustomCodemodDocsMixin:
    """
    Mixin for all codemods with docs provided by this package.
    """

    @property
    def docs_module_path(self):
        return "{{ cookiecutter.project_slug }}.docs"


class CustomCodemod(CustomCodemodDocsMixin, FindAndFixCodemod):
    """
    Base class for all find-and-fix codemods provided by this package.
    """

    @property
    def origin(self):
        return "{{ cookiecutter.project_slug }}"


class SASTCodemod(CustomCodemodDocsMixin, RemediationCodemod, metaclass=ABCMeta):
    """
    Base class for all SAST codemods provided by this package.

    Child classes must define the origin attribute, which must be a string that corresponds to the tool that generated the findings.
    """


class SimpleCodemod(_SimpleCodemod):
    """
    Convenience base class for all custom codemods with a single detector and transformer.
    """

    codemod_base = CustomCodemod
