import pathlib

def get_environment_dir(environment: str) -> str:
	return pathlib.Path(__file__).resolve().parents[2] / 'e2e' / 'environments' / environment