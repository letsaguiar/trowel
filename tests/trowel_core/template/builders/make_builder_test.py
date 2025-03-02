import pytest

from src.trowel_core.template.builders import TemplateBuilderMake
from src.trowel_core.config.models import ConfigModel

@pytest.fixture
def config_model():
    return ConfigModel(
        name="test",
        sources=["main.c"]
    )

@pytest.fixture
def make_builder():
    return TemplateBuilderMake()


class TestTemplateBuilderMake:
    def test_build_should_raise_exception(
        self, config_model: ConfigModel, make_builder: TemplateBuilderMake
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
    
        assert make_builder.build(config_model) == expected_output