from . import BaseException

def ConfigException(message: str, err: Exception):
	return BaseException("config", message, err)