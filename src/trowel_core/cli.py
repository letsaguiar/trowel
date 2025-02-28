import click

from trowel_core.config.parsers import ConfigParserJson
from trowel_core.config.services import ConfigService
from trowel_core.template.builders import TemplateBuilderMake
from trowel_core.template.services import TemplateService
from trowel_core.builder.strategies import BuilderStrategyMake
from trowel_core.builder.services import BuilderService

@click.group()
def main():
    """Trowel is a C builder and project management tool designed for simplicity and automation"""
    pass

@main.command()
@click.option("--path", default="./trowel.json", help="Path to your trowel config file")
def build(path: str):
    config_service = ConfigService(ConfigParserJson)
    template_service = TemplateService(TemplateBuilderMake)
    builder_service = BuilderService(BuilderStrategyMake)

    config = config_service.getConfig(path)
    template = template_service.build(config)
    builder_service.run(template)