from pathlib import Path
from codemodder.codemods.api import BaseCodemod, SimpleCodemod as _SimpleCodemod
from codemodder.codemods.base_codemod import Metadata
from codemodder.codemods.base_detector import BaseDetector
from codemodder.codemods.base_transformer import BaseTransformerPipeline
from codemodder.context import CodemodExecutionContext


class CustomCodemod(BaseCodemod):
    """
    Base class for all codemods provided by this package.
    """

    @property
    def origin(self):
        return "{{ cookiecutter.project_slug }}"

    @property
    def docs_module_path(self):
        return "{{ cookiecutter.project_slug }}"


class SASTCodemod(CustomCodemod):
    requested_rules: list[str]

    def __init__(
        self,
        *,
        metadata: Metadata,
        detector: BaseDetector | None = None,
        transformer: BaseTransformerPipeline,
        requested_rules: list[str] | None = None,
    ):
        super().__init__(metadata=metadata, detector=detector, transformer=transformer)
        self.requested_rules = [self.name]
        if requested_rules:
            self.requested_rules.extend(requested_rules)

    def apply(
        self,
        context: CodemodExecutionContext,
        files_to_analyze: list[Path],
    ) -> None:
        self._apply(context, files_to_analyze, self.requested_rules)


class SimpleCodemod(_SimpleCodemod):
    """
    Base class for all codemods in this package with a single detector and transformer.
    """

    codemod_base = CustomCodemod
