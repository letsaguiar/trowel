import pathlib
import os

from src.trowel_core.setup import TROWEL_SRC

from tests.e2e.utils.project_build import project_build
from tests.e2e.utils.projects import Projects

class TestValidBaseScenario:
	def test_should_successfully_build_the_project(self, tmp_path: pathlib.PosixPath):
		project_dir, result = project_build(Projects.VALID_BASE, tmp_path)

		print(f"Directory contents: {os.listdir(project_dir)}")

		assert result.returncode == 0
		assert pathlib.Path(project_dir / 'base').exists()
		assert pathlib.Path(project_dir / 'main.o').exists()