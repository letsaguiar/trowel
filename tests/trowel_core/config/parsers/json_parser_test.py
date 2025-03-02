import click
import json
import pathlib
import pytest

from src.trowel_core.config.parsers import ConfigParserJson

@pytest.fixture
def json_parser():
    return ConfigParserJson()

class TestConfigParserJson:
    def test_should_parse_json_files(
        self, json_parser: ConfigParserJson, tmp_path: pathlib.PosixPath
    ):
        test_data = { "name": "test" }
        test_file = tmp_path / "trowel.json"
        test_file.write_text(json.dumps(test_data))

        assert json_parser.parse(test_file) == test_data

    def test_should_throw_when_file_not_found(
        self, json_parser: ConfigParserJson, tmp_path: pathlib.PosixPath
    ):
        test_data = { "name": "test" }
        test_file = tmp_path / "trowel.json"

        with pytest.raises(click.Abort):
            json_parser.parse(test_file)