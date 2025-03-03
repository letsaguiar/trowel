import pathlib
import shutil

from tests.e2e.utils.get_environment_dir import get_environment_dir
from tests.e2e.utils.projects import Projects

def get_project_dir(environment: Projects, tmp_path: pathlib.PosixPath):
	environment_dir = get_environment_dir(environment)
	tmp_dir = tmp_path / environment.value
	shutil.copytree(environment_dir, tmp_dir)

	return tmp_dir