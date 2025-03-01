import pytest

from src.trowel_core.config.parsers import ConfigParser

@pytest.fixture
def config_parser():
    return ConfigParser()

class TestConfigParser:
    def test_should_raise_exception_on_parse(self, config_parser: ConfigParser):
        with pytest.raises(Exception):
            config_parser.parse("foo")