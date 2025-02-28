import click
import jinja2
import json
import os
import jinja2.tests
import subprocess
import tempfile

from trowel_core.config.models import ConfigModel
from trowel_core.config.parsers import ConfigParserJson
from trowel_core.config.services import ConfigService

TROWEL_PATH = os.getenv('TROWEL_PATH')
TROWEL_SRC = f"{TROWEL_PATH}/src"
TROWEL_RESOURCES = f"{TROWEL_SRC}/resources"
TROWEL_TEMPLATES = f"{TROWEL_RESOURCES}/templates"
        
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