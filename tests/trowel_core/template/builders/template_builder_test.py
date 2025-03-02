import pytest

from src.trowel_core.template.builders import TemplateBuilder
from src.trowel_core.config.models import ConfigModel

@pytest.fixture
def config_model():
    return ConfigModel(
        name="test",
        sources=["main.c"]
    )

@pytest.fixture
def template_builder():
    return TemplateBuilder()


class TestTemplateBuilder:
    def test_build_should_raise_exception(
        self, config_model: ConfigModel, template_builder: TemplateBuilder
    ):
        with pytest.raises(Exception):
            template_builder.build(config_model)