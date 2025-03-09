import click
import subprocess
import tempfile

from trowel_core.logger import Logger

class BuilderStrategyMake:
    _logger = Logger().getLogger()

    @staticmethod
    def build(template: str):
        with tempfile.NamedTemporaryFile(mode="w", delete=True) as temp:
            temp.write(template)
            temp.flush()

            try:
                result = subprocess.run(['make', '-f', temp.name], check=True, capture_output=True)
                BuilderStrategyMake._logger.info(f"Builder output: {result}")
            except subprocess.CalledProcessError as e:
                print(f"Build error: {e}")
                raise click.Abort()
