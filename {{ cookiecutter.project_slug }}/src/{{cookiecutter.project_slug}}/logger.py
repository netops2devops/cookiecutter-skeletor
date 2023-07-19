import logging
import os
from pathlib import Path

import logging_json

def mkdir_log():
    """create a logs dir and a logfile if missing"""
    basedir = Path(__file__).parent
    if not Path.is_dir(basedir / "logs"):
        Path("logs").mkdir(parents=True, exist_ok=True)
        Path("logs/app.log").touch()


def json_logger():
    """Unified single JSON logger object

    Returns:
        _type_: logger
    """
    log_level = os.environ["LOG_LEVEL"]
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    mkdir_log()
    logfile_path = str(Path(__file__).parent) + "/logs/app.log"
    file_handler = logging.FileHandler(logfile_path)

    json_formatter = logging_json.JSONFormatter(
        fields={
            "timestamp": "asctime",
            "log_level": "levelname",
            "file": "filename",
            "function": "funcName",
            "message": "msg",
        }
    )

    file_handler.setFormatter(json_formatter)
    logger.addHandler(file_handler)

    return logger

# usable as : `from mypkg.logger import logger`
logger = json_logger()
