import logging

logger = logging.getLogger(__name__)


def function_03(value: int) -> int:
    logger.info("function_03 received value=%s", value)
    return value + 3
