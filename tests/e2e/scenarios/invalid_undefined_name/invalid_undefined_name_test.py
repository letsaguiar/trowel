import pathlib

from src.trowel_core.setup import TROWEL_SRC

from tests.e2e.utils.project_build import project_build
from tests.e2e.utils.projects import Projects

class TestInvalidUndefinedNameScenario:
	def test_should_throw_error(self, tmp_path: pathlib.PosixPath):
		project_dir, result = project_build(Projects.INVALID_UNDEFINED_NAME, tmp_path)

		assert result.returncode == 1
		assert not pathlib.Path(project_dir / "main.o").exists()