from enum import Enum

class Projects(Enum):
	VALID_EXECUTABLE = "valid_executable"
	INVALID_UNDEFINED_NAME = "invalid_undefined_name"
	INVALID_UNDEFINED_SOURCES = "invalid_undefined_sources"
	VALID_GLOB_SOURCES = "valid_glob_sources"
	VALID_LIBRARY = "valid_library"