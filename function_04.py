import logging

logger = logging.getLogger(__name__)


def function_04(value: int) -> int:
    logger.debug("function_04 processing value=%s", value)
    return value + 4
