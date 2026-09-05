import logging

logger = logging.getLogger(__name__)


def function_05(value: int) -> int:
    logger.warning("function_05 processing value=%s", value)
    return value + 5
