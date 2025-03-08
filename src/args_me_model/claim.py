from typing import Annotated, List
from pydantic import BaseModel, Field, model_validator

from .claim_id import claim_id_pattern
from .argument import Argument
from .source import Source


class Claim(BaseModel):
    id: Annotated[str, Field(pattern=claim_id_pattern)] = Field(
            description="The claim's unique identifier",
        )
    text: str = Field(
            description="The claim's text"
        )
    counter: Annotated[str, Field(pattern=claim_id_pattern)] | None = Field(
            default=None,
            description="ID of the counter claim to this claim",
        )
    arguments: List[Argument] = Field(
            default=[],
            description="Arguments that support this claim"
        )
    sources: List[Source] = Field(
            description="Sources for this claim",
            min_length=1
        )

    @model_validator(mode="after")
    def _validate_sources(self):
        for source in self.sources:
            if not source.text:
                raise ValueError("Sources for a claim must contain the text attribute")
        return self
