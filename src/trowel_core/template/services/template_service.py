from trowel_core.config.models import ConfigModel
from trowel_core.template.builders import TemplateBuilder
from trowel_core.logger import Logger

class TemplateService:
    _logger = Logger().getLogger()

    def __init__(self, builder: TemplateBuilder):
        self._builder = builder

    def build(self, config: ConfigModel) -> str:
        self._logger.info("Creating builder template")
        template = self._builder.build(config)
        self._logger.info("Seccessfully created builder template")

        return template
