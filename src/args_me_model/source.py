from pydantic import BaseModel, Field, model_validator
from pydantic.networks import HttpUrl

class Source(BaseModel):
    text: str | None = Field(
            default = None,
            description = "Original text in or from the source"
        )
    url: HttpUrl | None = Field(
            default = None,
            description = "URL from which the text or argument was taken"
        )
    method: str | None = Field(
            default = None,
            description = "Identifier of the method that generated the text or connected the argument"
        )

    @model_validator(mode="after")
    def _validate(self):
        if not self.url and not self.method:
            raise ValueError("At least one of 'url' and 'method' must be specified")
        return self

