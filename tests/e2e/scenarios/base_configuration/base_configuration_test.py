import pathlib
import pytest
import shutil
import subprocess

from src.trowel_core.setup import TROWEL_SRC

from tests.e2e.utils.project_build import project_build
from tests.e2e.utils.projects import Projects

class TestBaseConfiguration:
	def test_should_successfully_build_the_project(self, tmp_path: pathlib.PosixPath):
		project_dir, result = project_build(Projects.BASE_CONFIGURATION, tmp_path)

		assert result.returncode == 0
		assert pathlib.Path(project_dir / 'base')
		assert pathlib.Path(project_dir / 'main.o')