import logging

logger = logging.getLogger(__name__)


def function_01(value: int) -> int:
    logger.info("function_01 received value=%s", value)
    return value + 1
