import os
import logging
import logging_json

# structured logging in JSON.
def json_logger(logfile="{{cookiecutter.project_slug}}.log"):
    """Unified single JSON logger object for infotrace & plugins

    Returns:
        _type_: logger
    """
    # set these in the .env file
    abs_path = os.environ["LOG_DIR"]
    log_level = os.environ["LOG_LEVEL"]

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # for warning, error & critical levels
    file_handler = logging.FileHandler(abs_path + logfile)

    json_formatter = logging_json.JSONFormatter(
        fields={
            "timestamp": "asctime",
            "log_level": "levelname",
            "file": "filename",
            "function": "funcName",
            "msg": "msg",
        }
    )

    file_handler.setFormatter(json_formatter)
    logger.addHandler(file_handler)

    return logger
