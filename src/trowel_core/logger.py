import sys
import logging
import pythonjsonlogger
import pythonjsonlogger.jsonlogger

from trowel_core.setup import TROWEL_DEBUG_LEVEL

class Logger:
	_initialized = False
	_logger = logging.getLogger("trowel")

	def __init__(self):
		if not Logger._initialized:
			self._setupLogger()
			self._setupStdoutHandler()
			Logger._initialized = True

	def _setupLogger(self):
		Logger._logger.setLevel(TROWEL_DEBUG_LEVEL)

	def _setupStdoutHandler(self):
		handler = logging.StreamHandler(sys.stdout)
		handler.setFormatter(self._getFormatter())
		Logger._logger.addHandler(handler)

	def _getFormatter(self):
		return pythonjsonlogger.jsonlogger.JsonFormatter(
			"%(asctime)s %(levelname)s %(filename)s %(lineno)s %(message)s",
    		rename_fields={"levelname": "severity", "asctime": "timestamp"},
		)

	def getLogger(self):
		return Logger._logger