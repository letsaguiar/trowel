import pytest

from src.trowel_core.template.builders import TemplateBuilderMake
from src.trowel_core.config.models import ConfigModel

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
def make_builder():
    return TemplateBuilderMake()


class TestTemplateBuilderMake:
    def test_build_should_return_a_valid_output_for_libraries(
        self, library_model: ConfigModel, make_builder: TemplateBuilderMake
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
    
        assert make_builder.build(library_model) == expected_output

    def test_build_should_return_a_valid_output_for_executables(
        self, executable_model: ConfigModel, make_builder: TemplateBuilderMake
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
    
        assert make_builder.build(executable_model) == expected_output