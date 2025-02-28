from trowel_core.config.models import ConfigModel
from trowel_core.config.parsers import ConfigParser

class ConfigService:
    def __init__(self, parser: ConfigParser):
        self._parser = parser

    def getConfig(self, path: str):
        data = self._parser.parse(path)
        return ConfigModel(**data)