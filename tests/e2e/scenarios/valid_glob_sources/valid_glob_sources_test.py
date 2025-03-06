import pathlib

from tests.e2e.utils.project_build import project_build
from tests.e2e.utils.projects import Projects

class TestValidGlobSourcesScenario:
	def test_should_successfully_build_the_project(self, tmp_path: pathlib.PosixPath):
		project_dir, result = project_build(Projects.VALID_GLOB_SOURCES, tmp_path)

		assert result.returncode == 0
		assert pathlib.Path(project_dir / 'glob-sources').exists()
		assert pathlib.Path(project_dir / 'main1.o').exists()
		assert pathlib.Path(project_dir / 'main2.o').exists()