import pathlib
import subprocess

from src.trowel_core.setup import TROWEL_SRC

from tests.e2e.utils.get_project_dir import get_project_dir

def project_build(environment: str, tmp_path: pathlib.PosixPath):
	project_dir = get_project_dir(environment, tmp_path)
	return project_dir, subprocess.run(
		['python', TROWEL_SRC.joinpath('cli.py'), 'build'],
		capture_output=True,
		cwd=project_dir
	)