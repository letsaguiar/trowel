import pytest

from src.trowel_core.config.models import ConfigModel
from src.trowel_core.template.builders import TemplateBuilderMake
from src.trowel_core.template.services import TemplateService

@pytest.fixture
def config_model():
    return ConfigModel(
        name="test",
        sources=["main.c"]
    )

@pytest.fixture
def template_service():
	return TemplateService(TemplateBuilderMake())


class TestTemplateService:
	def test_build_should_return_a_valid_output(
		self, config_model: ConfigModel, template_service: TemplateService
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
    
		assert template_service.build(config_model) == expected_output