import logging

logger = logging.getLogger(__name__)


def function_02(value: int) -> int:
    logger.warning("function_02 processing value=%s", value)
    return value + 2
