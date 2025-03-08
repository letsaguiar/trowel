import importlib.resources

TROWEL_SRC_DIR = importlib.resources.files("trowel_core")
TROWEL_TEMPLATES_DIR = TROWEL_SRC_DIR.joinpath("resources/templates")