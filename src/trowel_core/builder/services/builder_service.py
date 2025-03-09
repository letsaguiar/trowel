from trowel_core.builder.strategies import BuilderStrategy
from trowel_core.logger import Logger

class BuilderService:
    _logger = Logger().getLogger()

    def __init__(self, strategy: BuilderStrategy):
        self._strategy = strategy

    def run(self, template: str):
        try:
            self._logger.info("Starting building process")
            self._strategy.build(template)
            self._logger.info("Project build was successfull")
        except:
            self._logger.error("Error on project build")
