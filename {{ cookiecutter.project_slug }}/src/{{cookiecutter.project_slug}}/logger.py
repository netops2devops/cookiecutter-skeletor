import logging
import os
from pathlib import Path

import logging_json
from rich.logging import RichHandler


def mkdir_log():
    """create a logs dir and a logfile if missing"""
    basedir = Path(__file__).parent
    if not Path.is_dir(basedir / "logs"):
        Path("logs").mkdir(parents=True, exist_ok=True)
        Path("logs/infotrace.log").touch()


def json_logger():
    """Unified single JSON logger object for infotrace & plugins

    Returns:
        _type_: logger
    """
    log_level = os.environ["LOG_LEVEL"]
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    mkdir_log()
    logfile_path = str(Path(__file__).parent) + "/logs/infotrace.log"
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


def set_cli_logger():
    log_level = os.environ["LOG_LEVEL"]
    cli_logger = logging.getLogger(__name__)
    cli_logger.setLevel(log_level)

    if log_level == "DEBUG":
        from rich.traceback import install

        install(show_locals=True)

    # rich logging for cli debugging
    shell_handler = RichHandler()
    shell_formatter = logging.Formatter("[ %(funcName)s() :: %(message)s ]")
    shell_handler.setFormatter(shell_formatter)
    cli_logger.addHandler(shell_handler)

    return cli_logger


logger = json_logger()
