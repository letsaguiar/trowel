import click
import jinja2
import json
import os
import jinja2.tests
import subprocess
import tempfile

from trowel_core.config.parsers import ConfigParserJson
from trowel_core.config.services import ConfigService
from trowel_core.template.builders import TemplateBuilderMake
from trowel_core.template.services import TemplateService
        
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