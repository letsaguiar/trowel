import logging
import importlib.resources
import os

TROWEL_DEBUG_LEVEL = os.getenv("TROWEL_DEBUG_LEVEL", logging.INFO)
TROWEL_SRC_DIR = importlib.resources.files("trowel_core")
TROWEL_TEMPLATES_DIR = TROWEL_SRC_DIR.joinpath("resources/templates")