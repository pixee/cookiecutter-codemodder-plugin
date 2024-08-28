import libcst as cst

from codemodder.codemods.api import Metadata, RemediationCodemod, ReviewGuidance
from codemodder.codemods.semgrep import SemgrepSarifFileDetector
from codemodder.codemods.libcst_transformer import (
    LibcstResultTransformer,
    LibcstTransformerPipeline,
)

from .api import SASTCodemod


class SemgrepCodemod(SASTCodemod):
    """Base class for all custom codemods that remediate Semgrep findings."""

    @property
    def origin(self):
        """
        Remediation codemods must define an origin that corresponds to the tool that generated the findings.
        """
        return "semgrep"


class CustomSemgrepCodemodTransformer(LibcstResultTransformer):
    def on_result_found(
        self,
        original_node: cst.CSTNode,
        updated_node: cst.CSTNode,
    ) -> cst.CSTNode:
        """
        This method is called for each result found by the detector.

        It should return the updated node, which will be used to replace the original node in the file.
        It is intended to support relatively simply transformations that can be applied to a single node at a time.
        It applies to a limited subset of CST nodes and is not intended to be used for more complex transformations.
        The `LibcstResultTransformer` also exposes the entire LibCST visitor API for more complex transformations.
        In those cases, the `visit_*` methods should be overridden instead of this method.

        Examples of codemods using both APIs can be found in the `codemodder` project:
            https://github.com/pixee/codemodder-python/tree/main/src/core_codemods
        """
        return updated_node


CustomSemgrepCodemod = SemgrepCodemod(
    metadata=Metadata(
        # The name should be a unique identifier for the codemod
        # The origin and language are automatically added to the name by the framework to generate the full ID
        name="custom-semgrep-codemod",
        # The summary should be a single line that describes the purpose of the codemod
        summary="Custom Semgrep codemod",
        # The description should provide more detailed information about the codemod
        # Longer-form descriptions can be provided in the docs/ directory
        description="This is a custom Semgrep codemod.",
        # Review guidance should reflect the level of review that the changes made by the codemod require
        review_guidance=ReviewGuidance.MERGE_AFTER_CURSORY_REVIEW,
        references=[],
    ),
    transformer=LibcstTransformerPipeline(CustomSemgrepCodemodTransformer),
    # This is the detector that will be used to process Semgrep SARIF files in the project
    # It automatically processes Semgrep sarif files given by the --sarif CLI flag
    detector=SemgrepSarifFileDetector(),
    # Modify this to match the file extensions of your project
    default_extensions=[".py"],
    # Update this with fully qualified Semgrep rule IDs that this codemod remediates
    requested_rules=[
        "python.framework.security.problem.fake-rule-id",
    ],
)
