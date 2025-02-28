import click
import jinja2
import json
import os
import jinja2.tests
import pydantic
import subprocess
import tempfile

TROWEL_PATH = os.getenv('TROWEL_PATH')
TROWEL_SRC = f"{TROWEL_PATH}/src"
TROWEL_RESOURCES = f"{TROWEL_SRC}/resources"
TROWEL_TEMPLATES = f"{TROWEL_RESOURCES}/templates"

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
        try:
            with open(path) as file:
                data = json.loads(file.read())
            return (data)
        except FileNotFoundError:
            click.echo("Error: trowel config not found.", err=True)
            raise click.Abort()

class ConfigService:
    def __init__(self, parser: ConfigParser):
        self._parser = parser

    def getConfig(self, path: str):
        data = self._parser.parse(path)
        return ConfigModel(**data)
        
class TemplateBuilder:
    @staticmethod
    def build(config: ConfigModel):
        raise Exception("Method not implemented.")
        
class TemplateBuilderMake:
    @staticmethod
    def build(config: ConfigModel):
        with open(f"{TROWEL_TEMPLATES}/Makefile") as file:
            template = jinja2.Template(file.read())
            output = template.render(config)

        return output
        
class TemplateService:
    def __init__(self, builder: TemplateBuilder):
        self._builder = builder

    def build(self, config: ConfigModel):
        return self._builder.build(config)

class BuilderStrategy:
    @staticmethod
    def build(template: str):
        raise Exception("Method not implemented.")

class BuilderStrategyMake:
    @staticmethod
    def build(template: str):
        with tempfile.NamedTemporaryFile(mode="w", delete=True) as temp:
            temp.write(template)
            temp.flush()

            try:
                result = subprocess.run(['make', '-f', temp.name], check=True)
                print("Build successful")
            except subprocess.CalledProcessError as e:
                print(f"Build error: {e}")

class BuilderService:
    def __init__(self, strategy: BuilderStrategy):
        self._strategy = strategy

    def run(self, template: str):
        return self._strategy.build(template)

@click.group()
def cli():
    """Trowel is a C builder and project management tool designed for simplicity and automation"""
    pass

@cli.command()
@click.option("--path", default="./trowel.json", help="Path to your trowel config file")
def build(path: str):
    config_service = ConfigService(ConfigParserJson)
    template_service = TemplateService(TemplateBuilderMake)
    builder_service = BuilderService(BuilderStrategyMake)

    config = config_service.getConfig(path)
    template = template_service.build(config)
    builder_service.run(template)