from typing import Annotated, List
from pydantic import BaseModel, Field

from .claim_id import claim_id_pattern
from .source import Source


class Argument(BaseModel):
    premises: List[Annotated[str, Field(pattern=claim_id_pattern)]] = Field(
            description="Claims that provide linked support for the conclusion",
            min_length=1
        )
    sources: List[Source] = Field(
            description="Sources for this argument",
            min_length=1
        )
