import jinja2
from trowel_core.config.models import ConfigModel
from trowel_core.setup import TROWEL_TEMPLATES_DIR

class TemplateBuilderMake:
    @staticmethod
    def build(config: ConfigModel) -> str:
        with open(f"{TROWEL_TEMPLATES_DIR}/Makefile") as file:
            template = jinja2.Template(
                file.read(),
                trim_blocks=True,
                lstrip_blocks=True
            )
            output = template.render(config)

        return output