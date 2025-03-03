import pytest

from src.trowel_core.builder.strategies import BuilderStrategy

@pytest.fixture
def builder_strategy():
	return BuilderStrategy()


class TestBuilderStrategy:
	def test_build_should_raise_an_exception(self, builder_strategy: BuilderStrategy):
		with pytest.raises(Exception):
			builder_strategy.build("")