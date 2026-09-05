import logging

logger = logging.getLogger(__name__)


def function_01(value: int) -> int:
    logger.debug("function_01 processing value=%s", value)
    return value + 1
