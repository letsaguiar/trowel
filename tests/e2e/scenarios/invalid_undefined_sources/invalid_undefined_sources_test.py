import pathlib

from tests.e2e.utils.project_build import project_build
from tests.e2e.utils.projects import Projects

class TestInvalidUndefinedSourcescenario:
	def test_should_throw_error(self, tmp_path: pathlib.PosixPath):
		project_dir, result = project_build(Projects.INVALID_UNDEFINED_SOURCES, tmp_path)

		assert result.returncode == 1