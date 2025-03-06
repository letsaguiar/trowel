import click

from trowel_core.config.models import ConfigModel
from trowel_core.config.parsers import ConfigParser
from trowel_core.exceptions import ConfigException

class ConfigService:
    def __init__(self, parser: ConfigParser):
        self._parser = parser

    def _step_get_raw_data(self, path: str, err: Exception) -> tuple[dict, Exception]:
        if (err):
            return None, err

        try:
            return self._parser.parse(path), None
        except Exception as e:
            return None, ConfigException("Unable to parse trowel.json", e)

    def _step_parse_raw_data(self, raw_data: dict, err: Exception) -> tuple[ConfigModel, Exception]:
        if (err):
            return None, err

        try:
            return ConfigModel(**raw_data), None
        except Exception as e:
            return None, ConfigException("Unable to create config model", e)

    def getConfig(self, path: str) -> ConfigModel:
        data, err = self._step_get_raw_data(path, None)
        data, err = self._step_parse_raw_data(data, err)

        if (err):
            raise err
        else:
            return data