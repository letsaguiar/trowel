import pathlib

from tests.e2e.utils.projects import Projects

def get_environment_dir(environment: Projects) -> pathlib.Path:
	return pathlib.Path(__file__).resolve().parents[2] / 'e2e' / 'environments' / environment.value