import click
import json
import pydantic

class ConfigModel(pydantic.BaseModel):
    name: str
    sources: list[str] = pydantic.Field(min_length=1)

class ConfigParser:
    @staticmethod
    def parse(path: str):
        raise Exception("Method not implemented.")

class ConfigParserJson:
    @staticmethod
    def parse(path: str):
        with open(path) as file:
            data = json.loads(file.read())
        return (data)

class ConfigService:
    def __init__(self, parser: ConfigParser):
        self._parser = parser

    def getConfig(self, path: str):
        data = self._parser.parse(path)
        return ConfigModel(**data)
        
@click.group()
def cli():
    """Trowel is a C builder and project management tool designed for simplicity and automation"""
    pass

@cli.command()
@click.option("--path", default="./trowel.json", help="Path to your trowel config file")
def build(path: str):
    config_service = ConfigService(ConfigParserJson)

    config = config_service.getConfig(path)
    print(config)