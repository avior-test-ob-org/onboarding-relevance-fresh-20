import logging

logger = logging.getLogger(__name__)


def function_09(value: int) -> int:
    logger.info("function_09 executing with value=%s", value)
    return value + 9
