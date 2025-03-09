import glob

from trowel_core.config.models import ConfigModel
from trowel_core.config.parsers import ConfigParser
from trowel_core.exceptions import ConfigException
from trowel_core.logger import Logger

class ConfigService:
    _logger = Logger().getLogger()

    def __init__(self, parser: ConfigParser):
        self._parser = parser

    def _step_get_raw_data(self, path: str, err: Exception) -> tuple[dict, Exception]:
        if (err):
            return None, err
        self._logger.debug("Running step: get_raw_data")

        try:
            data = self._parser.parse(path), None
            self._logger.debug("Successful step: get_raw_data")
            return data
        except Exception as e:
            return None, ConfigException("Unable to parse trowel.json", e)

    def _step_parse_raw_data(self, raw_data: dict, err: Exception) -> tuple[ConfigModel, Exception]:
        if (err):
            return None, err
        self._logger.debug("Running step: parse_raw_data")

        try:
            model = ConfigModel(**raw_data)
            self._logger.debug("Successful step: parse_raw_data")
            return model, None
        except Exception as e:
            return None, ConfigException("Unable to create config model", e)

    def _step_expand_sources(self, data: ConfigModel, err: Exception) -> tuple[ConfigModel, Exception]:
        if (err):
            return None, err
        self._logger.debug("Running step: expand_sources")
        
        try:
            sources = set()
            for source in data.sources:
                if not any(c in source for c in ['*', '?', '[', ']', '{', '}']):
                    sources.add(source)
                else:
                    sources.update(glob.glob(source))

            sources = list(map(str, sources))
            sources.sort()

            data_dict = data.model_dump()
            data_dict['sources'] = sources

            model = ConfigModel(**data_dict)
            self._logger.debug("Successful step: expand_sources")
            return model, None
        except Exception as e:
            return None, ConfigException("Unable to expand glob sources", e)

    def getConfig(self, path: str) -> ConfigModel:
        self._logger.info("Parsing config file")

        data, err = self._step_get_raw_data(path, None)
        data, err = self._step_parse_raw_data(data, err)
        data, err = self._step_expand_sources(data, err)

        if (err):
            self._logger.error("Unable to create config model")
            raise err
        else:
            self._logger.info("Successfully parsed config file")
            return data