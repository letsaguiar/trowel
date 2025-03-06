import pytest

from src.trowel_core.config.models import ConfigModel
from src.trowel_core.template.builders import TemplateBuilderMake
from src.trowel_core.template.services import TemplateService

@pytest.fixture
def library_model():
    return ConfigModel(
        name="test",
        sources=["main.c"],
		type="library"
    )

@pytest.fixture
def executable_model():
    return ConfigModel(
        name="test",
        sources=["main.c"]
    )

@pytest.fixture
def template_service():
	return TemplateService(TemplateBuilderMake())


class TestTemplateService:
	def test_build_should_return_a_valid_output(
		self, executable_model: ConfigModel, template_service: TemplateService
	):
		expected_output = """CC := gcc

SRC_FILES := main.c
OBJ_FILES := $(subst .c,.o,$(SRC_FILES))

NAME := test

.PHONY: all

all: $(NAME)

$(NAME): $(OBJ_FILES)
	$(CC) $^ -o $@

%.o: %.c
	$(CC) -c $< -o $@"""
    
		assert template_service.build(executable_model) == expected_output

	def test_build_should_return_a_valid_output(
		self, library_model: ConfigModel, template_service: TemplateService
	):
		expected_output = """CC := gcc

SRC_FILES := main.c
OBJ_FILES := $(subst .c,.o,$(SRC_FILES))

NAME := test.a

.PHONY: all

all: $(NAME)

$(NAME): $(OBJ_FILES)
	ar rcs $@ $^

%.o: %.c
	$(CC) -c $< -o $@"""
    
		assert template_service.build(library_model) == expected_output
