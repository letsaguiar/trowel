def BaseException(module: str, message: str, err: Exception):
	return Exception(f"{module.capitalize()} Error: {message.capitalize()}. {err}")