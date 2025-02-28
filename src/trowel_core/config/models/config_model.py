import pydantic

class ConfigModel(pydantic.BaseModel):
    name: str
    sources: list[str] = pydantic.Field(min_length=1)