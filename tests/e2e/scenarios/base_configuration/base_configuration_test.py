import pathlib
import pytest
import shutil
import subprocess

from src.trowel_core.setup import TROWEL_SRC

@pytest.fixture
def environment_dir() -> pathlib.Path:
	return pathlib.Path(__file__).resolve().parents[3] / 'e2e' / 'environments' / 'base_configuration'

@pytest.fixture
def project_dir(environment_dir: pathlib.Path, tmp_path: pathlib.PosixPath) -> str:
	tmp_dir = tmp_path / 'project'
	shutil.copytree(environment_dir, tmp_dir)

	return tmp_dir


class TestBaseConfiguration:
	def test_should_successfully_build_the_project(self, project_dir: pathlib.PosixPath):
		result = subprocess.run(
			['python', TROWEL_SRC.joinpath('cli.py'), 'build'],
			capture_output=True,
			cwd=project_dir
		)

		assert result.returncode == 0
		assert pathlib.Path(project_dir / 'base')
		assert pathlib.Path(project_dir / 'main.o')