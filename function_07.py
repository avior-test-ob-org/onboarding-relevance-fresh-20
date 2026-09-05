import logging

logger = logging.getLogger(__name__)


def function_07(value: int) -> int:
    logger.debug("function_07 processing value=%s", value)
    return value + 7
