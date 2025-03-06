import enum
import pydantic

class ConfigType(enum.Enum):
    LIBRARY = 'library'
    EXECUTABLE = 'executable'

class ConfigModel(pydantic.BaseModel):
    name: str
    sources: list[str] = pydantic.Field(min_length=1)
    type: str = "executable"

    @pydantic.field_validator('type', mode='after')
    @staticmethod
    def validate_type(value: str) -> str:
        if value in [item.value for item in ConfigType]:
            return value
        else:
            raise ValueError("Valid options for project type: library, executable")