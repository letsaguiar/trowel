from trowel_core.builder.strategies import BuilderStrategy

class BuilderService:
    def __init__(self, strategy: BuilderStrategy):
        self._strategy = strategy

    def run(self, template: str):
        return self._strategy.build(template)
