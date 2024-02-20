import libcst as cst

from .api import SimpleCodemod, Metadata, ReviewGuidance


class CustomCodemod(SimpleCodemod):
    metadata = Metadata(
        name="custom-codemod",
        summary="Custom codemod",
        review_guidance=ReviewGuidance.MERGE_AFTER_REVIEW,
    )

    def on_result_found(self, original_node: cst.CSTNode, updated_node: cst.CSTNode) -> cst.CSTNode:
        return updated_node
