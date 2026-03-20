"""Logging configuration for the LoTL package."""

import logging
from typing import Optional

_configured_loggers: dict[str, logging.Logger] = {}


def configure_logging(
    level: str = "INFO",
    logger_name: str = "tools.lotl",
) -> logging.Logger:
    """Configure and return the package logger.

    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR).
        logger_name: Name of the root logger.

    Returns:
        Configured logger instance.
    """
    if logger_name in _configured_loggers:
        return _configured_loggers[logger_name]

    logger = logging.getLogger(logger_name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(handler)

    _configured_loggers[logger_name] = logger
    return logger


def get_logger(name: str) -> logging.Logger:
    """Return a child logger for the given module name.

    Args:
        name: Fully qualified logger name (e.g. tools.lotl.producer).

    Returns:
        Child logger instance.
    """
    return logging.getLogger(name)
