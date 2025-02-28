from trowel_core.config.models import ConfigModel
from trowel_core.template.builders import TemplateBuilder

class TemplateService:
    def __init__(self, builder: TemplateBuilder):
        self._builder = builder

    def build(self, config: ConfigModel):
        return self._builder.build(config)
