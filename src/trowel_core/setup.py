import importlib.resources

TROWEL_SRC = importlib.resources.files("trowel_core")
TROWEL_TEMPLATES = TROWEL_SRC.joinpath("resources/templates")