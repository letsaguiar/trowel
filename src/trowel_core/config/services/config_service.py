import click

from trowel_core.config.models import ConfigModel
from trowel_core.config.parsers import ConfigParser

class ConfigService:
    def __init__(self, parser: ConfigParser):
        self._parser = parser

    def getConfig(self, path: str) -> ConfigModel:
        data = self._parser.parse(path)
        try:
            return ConfigModel(**data)
        except Exception as err:
            click.echo("Error: Invalid Configuration. {err}")
            raise click.Abort(1)