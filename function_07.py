import logging

logger = logging.getLogger(__name__)


def function_07(value: int) -> int:
    logger.info("function_07 received value=%s", value)
    return value + 7
