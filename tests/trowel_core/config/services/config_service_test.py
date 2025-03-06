import contextlib
import json
import pytest
import pathlib

from src.trowel_core.config.models import ConfigModel
from src.trowel_core.config.parsers import ConfigParserJson
from src.trowel_core.config.services import ConfigService

@pytest.fixture
def config_service():
    return ConfigService(ConfigParserJson())

class TestConfigService:
    def test_getConfig_should_return_a_model(
        self, config_service: ConfigService, tmp_path: pathlib.PosixPath
    ):
        test_data = { "name": "test", "sources": ["main.c"] }
        test_file = tmp_path / "trowel.json"
        test_file.write_text(json.dumps(test_data))

        test_model = ConfigModel(name="test", sources=["main.c"])
        assert config_service.getConfig(test_file).model_dump() == test_model.model_dump()
        
    def test_should_throw_when_data_has_no_name(
        self, config_service: ConfigService, tmp_path: pathlib.PosixPath
	):
        test_data = { "sources": ["main.c"] }
        test_file = tmp_path / "trowel.json"
        test_file.write_text(json.dumps(test_data))

        with pytest.raises(Exception):
            config_service.getConfig(test_file)
    
    def test_should_throw_when_data_has_no_sources(
        self, config_service: ConfigService, tmp_path: pathlib.PosixPath
	):
        test_data = { "name": "test" }
        test_file = tmp_path / "trowel.json"
        test_file.write_text(json.dumps(test_data))

        with pytest.raises(Exception):
            config_service.getConfig(test_file)
    
    def test_should_throw_when_data_has_no_sources(
        self, config_service: ConfigService, tmp_path: pathlib.PosixPath
	):
        test_data = { "name": "test", "sources": [] }
        test_file = tmp_path / "trowel.json"
        test_file.write_text(json.dumps(test_data))

        with pytest.raises(Exception):
            config_service.getConfig(test_file)

    def test_should_expand_glob_sources(
        self, config_service: ConfigService, tmp_path: pathlib.PosixPath
    ):
        test_data = { "name": "test", "sources": ['*.c'] }
        test_file = tmp_path / "trowel.json"
        test_file.write_text(json.dumps(test_data))

        for i in range (1, 4):
            glob_file = tmp_path / f"main{i}.c"
            glob_file.touch()
        
        test_model = ConfigModel(name="test", sources=["main1.c", "main2.c", "main3.c"])
        with contextlib.chdir(tmp_path):
            assert config_service.getConfig(test_file).__dict__ == test_model.__dict__

    def test_should_not_duplicate_sources(
        self, config_service: ConfigService, tmp_path: pathlib.PosixPath
    ):
        test_data = { "name": "test", "sources": ['*.c', '*.c'] }
        test_file = tmp_path / "trowel.json"
        test_file.write_text(json.dumps(test_data))

        for i in range (1, 4):
            glob_file = tmp_path / f"main{i}.c"
            glob_file.touch()
        
        test_model = ConfigModel(name="test", sources=["main1.c", "main2.c", "main3.c"])
        with contextlib.chdir(tmp_path):
            assert config_service.getConfig(test_file).__dict__ == test_model.__dict__

    def test_should_raise_error_when_glob_data_has_no_sources(
        self, config_service: ConfigService, tmp_path: pathlib.PosixPath
    ):
        test_data = { "name": "test", "sources": ['*.o'] }
        test_file = tmp_path / "trowel.json"
        test_file.write_text(json.dumps(test_data))

        for i in range (1, 4):
            glob_file = tmp_path / f"main{i}.c"
            glob_file.touch()
        
        with pytest.raises(Exception):
            config_service.getConfig(test_file)