from enum import Enum

class Projects(Enum):
	VALID_BASE_OMIT_TYPE = "valid_base_omit_type"
	VALID_GLOB_SOURCES = "valid_glob_sources"
	INVALID_UNDEFINED_NAME = "invalid_undefined_name"
	INVALID_UNDEFINED_SOURCES = "invalid_undefined_sources"
	INVALID_EMPTY_SOURCES = "invalid_empty_sources"
	INVALID_GLOB_SOURCES = "invalid_glob_sources"