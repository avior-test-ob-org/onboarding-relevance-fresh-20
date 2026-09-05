import logging

logger = logging.getLogger(__name__)


def function_06(value: int) -> int:
    logger.info("function_06 executing with value=%s", value)
    return value + 6
