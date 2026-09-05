import logging

logger = logging.getLogger(__name__)


def function_08(value: int) -> int:
    logger.warning("function_08 processing value=%s", value)
    return value + 8
