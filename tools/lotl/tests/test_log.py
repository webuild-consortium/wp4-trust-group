"""Tests for log module."""

import logging

import pytest

from tools.lotl.log import configure_logging, get_logger


def test_configure_logging() -> None:
    """configure_logging sets up logger with handler."""
    logger = configure_logging(level="DEBUG", logger_name="tools.lotl.test")
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 1
    assert not logger.propagate


def test_configure_logging_idempotent() -> None:
    """Second configure_logging does not add duplicate handlers."""
    logger1 = configure_logging(level="INFO", logger_name="tools.lotl.test_idempotent")
    logger2 = configure_logging(level="INFO", logger_name="tools.lotl.test_idempotent")
    assert logger1 is logger2
    assert len(logger1.handlers) == 1


def test_get_logger() -> None:
    """get_logger returns child logger."""
    child = get_logger("tools.lotl.producer")
    assert child.name == "tools.lotl.producer"
