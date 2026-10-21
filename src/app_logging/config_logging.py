import json
import logging
from logging.config import dictConfig

from app_logging.setting import (
    LOGGING_CONFIG_JSON,
    LOGS_DIR,
    SETUP_LOGGER_LEVEL,
    SETUP_LOGGER_NAME,
    LogLevel,
    validate_level,
)

_setup_logging_done: bool = False

_logger = logging.getLogger(SETUP_LOGGER_NAME)
_logger.setLevel(SETUP_LOGGER_LEVEL)


def _setup_logging() -> None:
    global _setup_logging_done

    if _setup_logging_done:
        _logger.debug("Logging setup already done. Skipping.")
        return

    if not LOGGING_CONFIG_JSON.is_file():
        msg = f"Logging configuration file not exists: {LOGGING_CONFIG_JSON}"
        raise FileNotFoundError(msg)

    if not LOGS_DIR.exists():
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        _logger.debug(f"Created logs directory: {LOGS_DIR}")

    with open(LOGGING_CONFIG_JSON, encoding="utf-8") as file:
        config = json.load(file)
        _logger.debug(f"Loaded logging configuration from {LOGGING_CONFIG_JSON}")

    dictConfig(config)
    _setup_logging_done = True


def get_logger(name: str = "", level: LogLevel | None = None) -> logging.Logger:
    if not _setup_logging_done:
        _logger.debug("Logging setup not done yet. Setting up now.")
        _setup_logging()

    logger = logging.getLogger(name)

    if level is not None:
        validate_level(level)
        logger.setLevel(level)

    return logger
